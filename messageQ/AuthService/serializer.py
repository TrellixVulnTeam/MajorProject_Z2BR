from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], first_name = validated_data['first_name'], last_name=validated_data['last_name'],email=validated_data['email'],password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username','first_name','last_name', 'email', 'password')