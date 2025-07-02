from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import MyUser
# from .utils import Utils

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            # body = "Click Here!"
            # data = {
            #     'subject' :"HI",
            #     'body': body,
            #     'to_email': email
                
            # }
            # Utils.send_email(data)
            if not user:
                raise serializers.ValidationError("Invalid Credentials")
        else:
            raise serializers.ValidationError("Must include email and password")

        data["user"] = user
        return data