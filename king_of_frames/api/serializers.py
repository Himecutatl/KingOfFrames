from rest_framework import serializers
from .models import Character, MoveList
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()


class MoveListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveList
        fields = '__all__'


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    move_list = MoveListSerializer(many=True)
    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Character
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError(
                {'password_confirmation': 'Passwords do not match'})

        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)
