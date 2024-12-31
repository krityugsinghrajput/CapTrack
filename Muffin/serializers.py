# serializers.py
from rest_framework import serializers
from .models import Item  # Adjust the import to point to your actual model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'category']  # Adjust this according to your model fields
