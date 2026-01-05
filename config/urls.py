from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("core.urls")),
    path("auth-login/",include("rest_framework.urls")),
    path("token",TokenObtainPairView.as_view()),
    path("Refresh/",TokenRefreshView.as_view()),
    path("register/",include("Register.urls")),
    path("login/",include("login.urls")),
]
