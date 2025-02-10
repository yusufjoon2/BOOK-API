from django.urls import path,include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),  # Add this line to include the router urls
]