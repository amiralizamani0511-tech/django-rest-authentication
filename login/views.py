from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .serializers import LoginSerializers
from django.contrib.auth import login
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated


class LoginView(APIView):
    def get_permissions(self):
        if self.request.method in ["POST"]:
            return[AllowAny()]
        return[IsAdminUser()]
    def post(self,request):
        serializer = LoginSerializers(data = request.data,context={"request":request})
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request,user)
            return Response({"message" : "عملیات با موفقیت انجام شد ","username" : user.username})
        return Response({"message" : "عملیات با شکست برخورد شد "})
