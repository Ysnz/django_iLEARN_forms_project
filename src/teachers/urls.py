from django.urls import path
from . import views
from .views import TeacherListView, TeacherDetailView

urlpatterns = [
    path('', TeacherListView.as_view(), name="teachers"),
    path('teacher/<int:pk>', TeacherDetailView.as_view(), name="teacher_detail"),
    
]