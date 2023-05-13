from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RecipeSerializer, RecipeImageSerializer
from .models import Recipe, Recipe_image
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
import math
from rest_framework.authentication import get_authorization_header
from user.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token, access_token_exp
from user.views import token_decode
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from operator import itemgetter
# Create your views here.

# 조회수와 추천수 공유수가 높은 레시피 10개의 데이터 조회
class PopularRecipe(APIView):
    def get(self, request):
        # Recipe Deserializer - json 데이터화 -> django 딕셔너리 형태로 변형
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        json = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(json)
        data=JSONParser().parse(stream)

        # popular 계산 및 key로 추가
        for i in range(len(data)):
            popular = (data[i]["hits"]+data[i]["recommend"]*data[i]["share"])
            data[i]['popular']=int(popular)

        # popular 기준 내림차순 정렬
        sort_data = sorted(data, key=itemgetter('popular'), reverse=True)

        # 정렬된 결과 값 json 재정의
        response_data=[]
        for i in range(len(sort_data)):
            result = {
                'id' : sort_data[i]['id'],
                'title' : sort_data[i]['title'],
                'recommend' : sort_data[i]['recommend'],
                'share' : sort_data[i]['share'],
                'images' : sort_data[i]['images']
            }
            response_data.append(result)
        return Response(response_data, status=status.HTTP_200_OK)

# 전체 레시피 데이터 : 레시피 items 수 제한, 각 레시피 이미지, 디테일 링크 리턴
# API test - url ex : http://127.0.0.1:8000/?search=타이틀&items=2
class AllRecipe(APIView):
    def get(self, request):
        # 객체 수(items), 검색어(search) pagination 정의
        items = request.GET.get('items', None)
        search = request.GET.get('search', None)
        
        # 전체 페이지 사이즈 정의 : 10 제한
        paginator = PageNumberPagination()
        paginator.page_size = 10

        # items가 있을 경우, search가 없을 경우 정의
        if items is not None:
            paginator.page_size = int(items)
        if search is None:
            search = ""
        
        # Recipe.title을 기준으로 검색 필터링
        search_filter = Recipe.objects.filter(title__icontains=search)
        
        # 검색된 레시피 데이터 최신순으로 정렬
        recipe = search_filter.order_by('-create_time')
        result = paginator.paginate_queryset(recipe, request)
        serializer = RecipeSerializer(result, many=True, context={"request" : request})
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)

    # 레시피 작성 - 로그인된 유저만 가능
    def post(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            recipe_image = request.GET.getlist('image', None)
            recipe_data = {
                "user" : token_decode(auth),
                "title" : request.data["title"],
                "material" : request.data["material"],
                "cook" : request.data["cook"],
                "category" : request.data["category"],
                "image" : recipe_image,
            }
            serializer = RecipeSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(data=recipe_data, request=request)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 레시피 수정 - 로그인된 유저만 가능
    def patch(self, request, recipe_id):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            recipe = Recipe.objects.get(pk = recipe_id)
            serializer = RecipeSerializer(recipe, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save(data = request.data, request = request)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 레시피 삭제
    def delete(self, request, recipe_id):
        recipe = Recipe.objects.get(pk = recipe_id)
        recipe.delete()
        return Response({'message' : 'sucess', 'code' : 200})

# recommend add (임시)
class RecommendAPIView(APIView):
    def post(self, request, recipe_id):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            recipe = Recipe.objects.get(id=recipe_id)
            if request.data['like_add'] == 'true':
                recipe.recommend += 1
                recipe.save()
                return Response({'message' : "like"})

            elif recipe.recommend > 0 and request.data['like_add'] == 'false':
                recipe.recommend -= 1
                recipe.save()
                return Response({'message' : "unlike"})
            
            else:
                return Response({'message' : "like Error"})