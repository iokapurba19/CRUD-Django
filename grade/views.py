from .models import Course
from rest_framework import viewsets
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from grade.serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# List View
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'course_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = context['course_list']
        context['title'] = 'Daftar Mata Kuliah'

        total_credits = sum(course.credits for course in courses)
        grade_point_map = {
            'A': 4.0,
            'AB': 3.5,
            'B': 3.0,
            'BC': 2.5,
            'C': 2.0,
            'D': 1.0,
            'E': 0.0
        }
        total_grade_points = sum(
            course.credits * grade_point_map.get(course.grade.upper(), 0.0) for course in courses
        )
        total_ipk = round((total_grade_points / total_credits), 2) if total_credits > 0 else 0.0

        context['total_credits'] = total_credits
        context['total_ipk'] = total_ipk

        if total_ipk > 3.5:
            context['recommended_sks'] = 24
        elif 3.0 <= total_ipk <= 3.49:
            context['recommended_sks'] = 22
        else:
            context['recommended_sks'] = 20

        return context

# Create View
class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'course_form.html'
    fields = ['course_name', 'credits', 'grade']
    success_url = reverse_lazy('grade:course-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tambah Mata Kuliah'
        return context

# Update View
class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'course_form.html'
    fields = ['course_name', 'credits', 'grade']
    success_url = reverse_lazy('grade:course-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Mata Kuliah'
        return context

# Delete View
class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('grade:course-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hapus Mata Kuliah'
        return context

# Detail View
class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail Mata Kuliah'
        return context