from django.urls import path
from .import views
from .views import PopularRecipe, AllRecipe

urlpatterns = [
    path('top', PopularRecipe.as_view(), name="popularRecipe"),
    path('', AllRecipe.as_view(), name="CreateRecipe"),
    path('', AllRecipe.as_view(), name="GetRecipe"),
    path('<int:recipe_id>', AllRecipe.as_view(), name="UpdateRecipe"),
    path('<int:recipe_id>', AllRecipe.as_view(), name="DeleteRecipe"),
]