from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import KalaView


router = DefaultRouter()
router.register(r"",KalaView)
urlpatterns = []
urlpatterns = router.urls
