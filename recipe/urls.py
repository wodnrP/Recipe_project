from django.urls import path
from .import views
from .views import PopularRecipe, AllRecipe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('top', PopularRecipe.as_view(), name="popularRecipe"),
    path('', AllRecipe.as_view(), name="CreateRecipe"),
    path('', AllRecipe.as_view(), name="GetRecipe"),
    path('<int:recipe_id>', AllRecipe.as_view(), name="UpdateRecipe"),
    path('<int:recipe_id>', AllRecipe.as_view(), name="DeleteRecipe"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)