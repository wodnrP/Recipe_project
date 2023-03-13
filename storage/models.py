from django.db import models
from user.models import User
from recipe.models import Recipe

# Create your models here.

class Storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'MyRecipe_Storage'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-pk']

    def __str__(self):
        return self.recipe.title

    def get_serializer(self):
        from .serializer import StorageSerializer
        return StorageSerializer(self)