from rest_framework import serializers
from .models import Storage
from recipe.models import Recipe, Recipe_image
from user.models import User 

class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = ('id', 'user', 'recipe', 'active', 'created_at')