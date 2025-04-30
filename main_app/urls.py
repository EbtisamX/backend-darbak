from django.urls import path
from .views import JobApplicationListCreate

urlpatterns = [
    path('jobs/', JobApplicationListCreate.as_view(), name='job-list-create'),
]