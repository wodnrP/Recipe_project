from rest_framework import serializers
from .models import Storage
from recipe.models import Recipe, Recipe_image
from user.models import User 

class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = ('id', 'user', 'recipe', 'active', 'created_at')


    # def create(self, request, **validated_data):
    #     print(request)
    #     user_instance = User.objects.filter(id = request['data']['user']).first()
    #     storage_obj = Storage.objects.create(recipe=request["recipe"], user=user_instance)
    #     return storage_obj