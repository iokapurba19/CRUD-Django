from django import forms
from .models import Item, Image

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image_file']