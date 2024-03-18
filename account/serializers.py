from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=221)
    username = serializers.CharField(max_length=212)
    password = serializers.CharField(max_length=211)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("Email already registered")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
