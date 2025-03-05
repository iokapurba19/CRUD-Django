from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Item, Image
from .forms import ItemForm, ImageForm
from .serializers import ItemSerializer, ImageSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# Views untuk Item
def default(request):
    return render(request, 'base/base.html')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'myapp/item_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'myapp/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'myapp/item_confirm_delete.html', {'item': item})

# Views untuk Image
def image_list(request):
    images = Image.objects.all()
    return render(request, 'myapp/image_list.html', {'images': images})

def image_create(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)  # Menambahkan request.FILES untuk mengupload file
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'myapp/image_form.html', {'form': form})

def image_update(request, pk):
    image = get_object_or_404(Image, pk=pk)
    images = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm(instance=image)
    return render(request, 'myapp/image_form.html', {'form': form, 'images': images})

def image_delete(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'myapp/image_confirm_delete.html', {'image': image})