from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from . serializers import Registerserializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated

class KalaViewser(APIView):
    def get_permissions(self):
        if self.request.method in ["POST"]:
            return[AllowAny()]
        return[IsAdminUser()]
    def post(self,request):
        serializer = Registerserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "عملیات با موفقیت  انجام شد "})
        return Response({"message" : "عملیات با موفیت انجام نشد "})
    def get(self,request):
        user = User.objects.all().values()
        return Response(user)
