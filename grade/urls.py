from django.urls import path, include
from dots_va.api import api
from rest_framework import routers
from grade import views
from .views import (
    CourseViewSet, CourseListView, CourseCreateView,
    CourseUpdateView, CourseDeleteView, CourseDetailView
)

app_name = 'grade'

router = routers.DefaultRouter()
router.register(r'course', views.CourseViewSet)

urlpatterns = [
	path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # HTML CRUD
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/create/', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]