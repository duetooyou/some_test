from rest_framework import serializers
from .models import User, House


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializerForHouse(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = ('salary', 'date')


class HouseSerializer(serializers.ModelSerializer):

    owner = UserSerializerForHouse()

    class Meta:
        model = House
        fields = '__all__'
