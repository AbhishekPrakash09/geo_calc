from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data['email']
        user = User(
            email=email,
            username=email  # Set the username to the email
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    def validate(self, attrs):
        email = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "User with this email does not exist."})

        attrs['username'] = user.username

        return super().validate(attrs)

