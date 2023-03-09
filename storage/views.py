from django.shortcuts import render
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
        
        recipe = Recipe.objects.get(pk=recipe_id)
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            user_token = token_decode(auth)
            try:
                storage = Storage.objects.get(recipe_id=recipe.id, user_id=user_token)
                
                if storage.recipe.title == recipe.title:
                    storage.save()
            except Storage.DoesNotExist:
                user = User.objects.get(pk=user_token)
                storage = Storage(
                    # id=Storage.id,
                    user=user,
                    recipe=recipe,
                    # created_at=Storage.created_at,
                )
                
                storage.save()
            
            serializer = StorageSerializer(data=storage, partial=True)
            print(serializer, "+", type(serializer))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
# @login_required
# def add_cart(request, recipe_id):
# 	# 상품을 담기 위해 해당 상품 객체를 product 변수에 할당
#     recipe = Recipe.objects.get(pk=recipe_id)

#     try:
#     	# 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
#         cart = CartItem.objects.get(recipe__id=recipe.pk, user__id=request.user.pk)
#         if cart:
#             if cart.recipe.name == recipe.name:
#                 cart.quantity += 1
#                 cart.save()
#     except CartItem.DoesNotExist:
#         user = User.objects.get(pk=request.user.pk)
#         cart = CartItem(
#             user=user,
#             recipe=recipe,
#             quantity=1,
#         )
#         cart.save()
#     return redirect('recipe:my-cart')