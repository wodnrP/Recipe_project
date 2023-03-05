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

        recipe_image = Recipe_image.objects.filter(recipe=recipe.id)
        image_set = recipe_image.values_list('image', flat=True)
        # validated_img = validated_data.copy()
        # image_data = validated_img.pop('data', None).pop('image', None)
        print(validated_data)
        print(type(image_set))
        
        if image_set is not None:
            image_data = validated_data['data'].pop('image')
            for image_data in image_set:
                Recipe_image.objects.create(recipe=recipe, image=image_data)
        recipe.save()
        return recipe
        # validated_data의 data key 값 = image key값 포함 쿼리dict 존재 -> image값 추출
        # 3/4 validated_data 의 data key 속 쿼리 dict 발견
        # image_data=validated_data.pop('data').pop('image')
        
        # for image_data in image_set:
        #     Recipe_image.objects.update(recipe=recipe, image=image_data)
        # recipe.save()
        # return recipe
        # 이렇게 update를 구성하게 될 경우 : 각각의 이미지만 수정하는 것이 아니라 
        # 이미지 수정할 때, 다시 전체 이미지를 수정해야하는 번잡함 발생
        
        

    # def update(self, recipe, validated_data):
    #     recipe.title = validated_data.get('title', recipe.title)
    #     recipe.material = validated_data.get('material', recipe.material)
    #     recipe.cook = validated_data.get('cook', recipe.cook)
    #     recipe.category = validated_data.get('category', recipe.category)
    #     recipe.save()

    #     if 'image' in validated_data:
    #         for img in validated_data['image']:
    #             # 이미지가 존재하는 경우
    #             if Recipe_image.objects.filter(id=img.get('id', None)).exists():
    #                 print('if문 진입')
    #                 Recipe_image.objects.filter(id=img['id']).update(image=img['image'])
    #             # 새로운 이미지인 경우
    #             else:
    #                 print('else문 진입')
    #                 Recipe_image.objects.create(recipe=recipe, image=img['image'])

    #     return recipe