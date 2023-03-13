from django.urls import path
from .import views
from .views import MyRecipe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:recipe_id>', MyRecipe.as_view(), name="Recipe_add_Storage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)