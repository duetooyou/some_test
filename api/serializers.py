from rest_framework import serializers
from .inspectmodel import Users, Houses


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserSerializerForHouse(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = ('salary', 'date')


class HouseSerializer(serializers.ModelSerializer):

    user = UserSerializerForHouse()

    class Meta:
        model = Houses
        fields = '__all__'
