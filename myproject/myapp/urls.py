from django.urls import path
from .views import item_list, item_create, item_update, item_delete, image_list, image_create, image_update, image_delete, default
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', default, name='default'),
    path('item/', item_list, name='item_list'),
    path('item/new/', item_create, name='item_create'),
    path('item/<int:pk>/edit/', item_update, name='item_update'),
    path('item/<int:pk>/delete/', item_delete, name='item_delete'),
    path('image/', image_list, name='image_list'),
    path('image/new/', image_create, name='image_create'),
    path('image/<int:pk>/edit/', image_update, name='image_update'),
    path('image/<int:pk>/delete/', image_delete, name='image_delete'),
    path('api/', include(router.urls)),
]