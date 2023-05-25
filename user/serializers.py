from rest_framework import serializers
from user import models
from django.contrib.auth.models import User


class Helloserializer(serializers.Serializer):
    """Serializes a name field for testing our APIView """
    name = serializers.CharField(max_length=64)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes User Profile Object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validate_data):
        """Create and Return A User"""
        user = models.UserProfile.objects.create_user(
            email=validate_data['email'],
            name=validate_data['name'],
            password=validate_data['password']
        )
        return user


class ProfileFeedSerializer(serializers.Serializer):
    """Serializes Profile Feed Item"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }

        }


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)