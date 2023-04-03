from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StorageSerializer
from recipe.serializer import RecipeSerializer, RecipeImageSerializer
from recipe.models import Recipe, Recipe_image
from .models import Storage
from user.models import User
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
import math
from rest_framework.authentication import get_authorization_header
from user.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token, access_token_exp
from user.views import token_decode
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from operator import itemgetter

# 유저 로그인 확인, 해당 유저와 레시피 데이터셋 리스트로 반환 (post, delete)
def user_recipe(request, recipe_id):
    auth = get_authorization_header(request).split()
    if auth and len(auth) == 2:
        user_token = token_decode(auth)
        user = User.objects.get(id=user_token)

        recipe = get_object_or_404(Recipe, id=recipe_id)
        
        return [user, recipe]

# 이미 저장한 레시피인지 확인
def storage_check(user_recipe):
    storage_check = Storage.objects.filter(user=user_recipe[0], recipe=user_recipe[1], active=True).exists()
    return storage_check


class MyRecipe(APIView):
    def get(self, request):
        # http://~/storage/?sort="category"
        sort = request.GET.get('sort', None)

        paginator = PageNumberPagination()
        paginator.page_size = 10

        if sort is None:
            sort = "전체"

        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            user_token = token_decode(auth)
            # 유저 객체 생성
            user = User.objects.get(id=user_token)

            # 해당 유저가 storage에 저장한 레시피 fk를 리스트 형식으로 필터
            storage = Storage.objects.filter(user=user).values_list('recipe', flat=True)
            
            # recipe fk로 Recipe모델의 데이터를 category기준, 해당 sort 쿼리로 필터 
            categoryFilter = Recipe.objects.filter(id__in=storage, category__icontains=sort)

            # 필터된 데이터 셋을 최신순으로 정렬 및 반환
            resultRecipe = categoryFilter.order_by('-create_time')
            result = paginator.paginate_queryset(resultRecipe, request)
            serializer = RecipeSerializer(result, many=True, context={"request" : request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message' : "로그인이 필요한 서비스 입니다"})
            

    def post(self, request, recipe_id):
        userRecipe = user_recipe(request, recipe_id)
        storageCheck = storage_check(userRecipe)
        recipe = Recipe.objects.get(id=userRecipe[1].id)

        if storageCheck is False:
            try:
                storage = Storage(user=userRecipe[0], recipe=userRecipe[1], active=True)
                if storage.recipe.title == userRecipe[1].title:
                    storage.save()
            except Storage.DoesNotExist:
                storage = Storage(
                    user=userRecipe[0],
                    recipe=userRecipe[1],
                    active=True
                )
                storage.save()
            # share 수 증가
            recipe.share += 1 
            recipe.save()
            
            serializer = Storage.get_serializer(storage)
            return Response(serializer.data)
        # 이미 저장한 경우 message 반환
        elif storageCheck is True:
            return Response({'message': "이미 저장한 레시피 입니다."})

    
    def delete(self, request, recipe_id):
            userRecipe = user_recipe(request, recipe_id)
            storageCheck = storage_check(userRecipe)
            recipe = Recipe.objects.get(id=userRecipe[1].id)
            # 이미 저장한 레시피일 경우 삭제
            if storageCheck is True:
                storage = Storage.objects.get(user=userRecipe[0], recipe=userRecipe[1])
                storage.delete()
                # share 수 감소
                recipe.share -= 1
                recipe.save()
                return Response({'message' : 'sucess', 'code' : 200})
        
        
        
        
        
        
        