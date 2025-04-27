from rest_framework import serializers
from .models import Client, Program, User

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    programs = ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'age', 'contact']

class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'roles']

    def get_roles(self, obj):
        return [group.name for group in obj.groups.all()]