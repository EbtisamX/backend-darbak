from django.urls import path
from .views import JobApplicationListCreate,JobApplicationDetailView

urlpatterns = [
    path('jobs/', JobApplicationListCreate.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobApplicationDetailView.as_view(), name='job-detail'),
]
