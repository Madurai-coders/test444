from dataclasses import field
from rest_framework import serializers
from base.models import Team
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id','name','created')

class addTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user