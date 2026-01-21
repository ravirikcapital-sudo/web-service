

from rest_framework import serializers
from .models import UserRegistration
from django.contrib.auth.hashers import make_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = [
            'id', 'name', 'email', 'mobile', 'city', 'gender',
            'password', 'hashed_password', 'profile_image', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']  
        extra_kwargs = {
            'password': {'write_only': True},          
            'hashed_password': {'write_only': True},   
        }

    def validate_password(self, value):
        """Ensure password rules are enforced"""
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if '@' not in value:
            raise serializers.ValidationError("Password must contain the '@' character.")
        return value

    def create(self, validated_data):
        
        plain_password = validated_data.get("password")
        validated_data["hashed_password"] = make_password(plain_password)
        return super().create(validated_data)
