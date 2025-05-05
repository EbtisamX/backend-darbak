from django.urls import path
from .views import JobApplicationListCreate,JobApplicationDetailView,NoteListCreate,NoteDetailView,SkillListCreateView,SignUpView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('jobs/', JobApplicationListCreate.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobApplicationDetailView.as_view(), name='job-detail'),
    path('notes/', NoteListCreate.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup')

]
    
    