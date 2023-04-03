from django.db import models
from user.models import User

# Create your models here.

# 레시피 DB모델
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("user.User", related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    material = models.TextField()
    cook = models.TextField()
    recommend = models.IntegerField(blank=True, null=True, default=0)
    hits = models.IntegerField(blank=True, null=True, default=0)
    share = models.IntegerField(blank=True, null=True, default=0) 
    
    CategoryType = models.TextChoices('CookType', '전체 회/샐러드 구이 튀김 찜/탕 면')
    category = models.CharField(blank=True, choices=CategoryType.choices, max_length=10, default='전체')

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.title

# 레시피 image 업로드 경로 함수 
def image_upload_path(instance, filename):
    print('success')
    return f'{instance}/{filename}'

# 레시피 image DB모델
class Recipe_image(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to = image_upload_path)
    
    def __str__(self):
        return self.recipe.title

    class Meta:
        db_table = 'recipe_image'


