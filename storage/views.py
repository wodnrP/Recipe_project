from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from recipe.serializer import RecipeSerializer, RecipeImageSerializer
from recipe.models import Recipe, Recipe_image
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


# Create your views here.
# @login_required
# def add_cart(request, product_pk):
# 	# 상품을 담기 위해 해당 상품 객체를 product 변수에 할당
#     product = Product.objects.get(pk=product_pk)

#     try:
#     	# 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
#         cart = CartItem.objects.get(product__id=product.pk, user__id=request.user.pk)
#         if cart:
#             if cart.product.name == product.name:
#                 cart.quantity += 1
#                 cart.save()
#     except CartItem.DoesNotExist:
#         user = User.objects.get(pk=request.user.pk)
#         cart = CartItem(
#             user=user,
#             product=product,
#             quantity=1,
#         )
#         cart.save()
#     return redirect('product:my-cart')