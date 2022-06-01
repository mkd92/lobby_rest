from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Property

class PropertySerializer(ModelSerializer):
    property_name = serializers.CharField()
    address = serializers.CharField()
    user_id = serializers.SerializerMethodField()
    class Meta:
        model=Property
        fields = ['property_name','address', 'user_id']
        
    def get_user(self,obj):
        return str(obj['pk'])