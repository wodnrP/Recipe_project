from rest_framework import serializers
from .models import Recipe, Recipe_image
from user.models import User 

class RecipeImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Recipe_image
        fields = ['image']

class RecipeSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        image = obj.image.all()
        return RecipeImageSerializer(image, many=True, context=self.context).data
    
    class Meta:
        model = Recipe
        fields = ('id', 'user', 'title', 'material', 'cook', 'category', 'recommend', 'hits', 'share', 'create_time', 'update_time', 'images')
    
    def create(self, instance, **validated_data):
        user_instance = User.objects.filter(id = instance['data']['user']).first()
        recipe_obj = Recipe.objects.create(title = instance["title"], material=instance["material"], cook=instance["cook"], 
        category=instance["category"], user=user_instance)

        # 각각의 image를 하나의 images 객체로 생성
        image_set = instance['request'].FILES
        print(image_set)
        for image_data in image_set.getlist('image'):
            Recipe_image.objects.create(recipe=recipe_obj, image=image_data)
        
        return recipe_obj
    
    def update(self, recipe, validated_data):
        recipe.title = validated_data.get('title', recipe.title)
        recipe.material = validated_data.get('material', recipe.material)
        recipe.cook = validated_data.get('cook', recipe.cook)
        recipe.category = validated_data.get('category', recipe.category)
        # 이미지 업데이트 (이미지 업데이트 요청시 해당 이미지 추가)
        # QueryDict에서 'data' key 해당 값 추출
        validated_img = validated_data.pop('data', None)      
        # 추출한 데이터에서 'image' key가 있는 경우 
        if 'image' in validated_img:                            
            images_data = validated_img.pop('image', None)
        # 없는 경우
        else:
            images_data = None
        # images_data가 있을 경우 Recipe_image에 해당 image추가
        if images_data is not None:
            for image_data in images_data:
                Recipe_image.objects.create(recipe=recipe, image=image_data)
        recipe.save()
        return recipe
    
        # validated_data의 data key 값 = image key값 포함 쿼리dict 존재 -> image값 추출
        # 3/4 validated_data 의 data key 속 쿼리 dict 발견
        # image_data=validated_data.pop('data').pop('image')
        # 이렇게 update를 구성하게 될 경우 : 각각의 이미지만 수정하는 것이 아니라 
        # 이미지 수정시 이미지 추가만 가능
