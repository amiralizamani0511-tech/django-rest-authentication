from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate



class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password =serializers.CharField()

    def validate(self, data):
        username_shoma = data.get("username")
        password_shoma = data.get("password")

        user = authenticate(username=username_shoma,password=password_shoma)
        if user is None:
            raise serializers.ValidationError("رمز یا نام کاربری شما درست نیست لطفا دوباره تلاش فرمایید ")
        
        if not user.is_active:
            raise serializers.ValidationError("کاربر مورد نظر فعال نیست لطفا دوباره بسازید تمام ")
        
        data["user"] = user
        return data
