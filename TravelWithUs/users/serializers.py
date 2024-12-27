from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)  # Add confirm_password

    class Meta:
        model = User
        fields = ('email', 'password',  'is_traveler')


    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password field from validated_data
        user = User.objects.create(
            email=validated_data['email'],
            is_traveler=validated_data['is_traveler'],
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['name'] = user.name
        return token
