from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .models import Kala
from .serializers import KalaSerializers


class KalaView(ModelViewSet):
    queryset = Kala.objects.all()
    serializer_class = KalaSerializers
    def get_permissions(self):
        if self.request.method in ["GET","HEAD","OPTIONS"]:
            return[AllowAny()]
        return[IsAdminUser()]
