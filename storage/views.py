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

# user, recipe, active, created_at
class MyRecipe(APIView):
    def get(self, request):
        pass
    
    def post(self, request, recipe_id):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            user_token = token_decode(auth)
            user = User.objects.get(id=user_token)

            # -----request에서 recipe_id를 받아오는 경우 / 현재는 url-----
            # recipe_id = request.data.get('recipe_id')
    
            recipe = get_object_or_404(Recipe, id=recipe_id)
            
            # 이미 저장한 레시피인지 확인 
            storage_check = Storage.objects.filter(user=user, recipe=recipe, active=True).exists()
            if storage_check is False:
                try:
                    storage = Storage(user=user, recipe=recipe, active=True)
                    if storage.recipe.title == recipe.title:
                        storage.save()
                except Storage.DoesNotExist:
                    storage = Storage(
                        user=user,
                        recipe=recipe,
                        active=True
                    )
                    storage.save()
                serializer = Storage.get_serializer(storage)
                return Response(serializer.data)
            
            # 이미 저장한 경우 message 반환
            elif storage_check is True:
                return Response({'message': "이미 저장한 레시피 입니다."})
        
        
        
        
        
        
        
        
        
        