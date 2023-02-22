from rest_framework import serializers

from .models import Notes

from django.contrib.auth.models import User


class NotesSerializer(serializers.ModelSerializer):
 
    class Meta:

        model = Notes
        fields = ['id', 'title', 'text']
    
class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        
        data = super().validate(attrs)
        """
        Check that the password fields match
        """
        password = data['password']
        password2 = data['password2']

        if password != password2:
            raise serializers.ValidationError({'password2': ['Sorry, the passwords do not match']})
        
        data.pop('password2')
        return data

    def create(self, validated_data):
        """
        Create and return a new user instance
        """
        user = User.objects.create_user(**validated_data)
        return user
