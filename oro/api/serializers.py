from rest_framework import serializers
from oro.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        # inherits Item model attributes
        model = Item
        # __all__ specifies all fields
        fields = '__all__'