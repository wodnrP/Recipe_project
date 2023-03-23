from django.contrib import admin
from .models import Recipe, Recipe_image
# admin : recipeadmin 20230219

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Recipe_image)