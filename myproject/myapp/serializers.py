from rest_framework import serializers
from .models import Item, Image

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',