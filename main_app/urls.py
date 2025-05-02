from django.urls import path
from .views import JobApplicationListCreate,JobApplicationDetailView,NoteListCreate

urlpatterns = [
    path('jobs/', JobApplicationListCreate.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobApplicationDetailView.as_view(), name='job-detail'),
    path('notes/', NoteListCreate.as_view(), name='note-list-create'),
    

]
