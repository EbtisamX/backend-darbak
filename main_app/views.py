from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JobApplication,Note,Skill
from .serializers import JobApplicationSerializer,NoteSerializer,SkillSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied


class JobApplicationListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        jobs = JobApplication.objects.filter(user=request.user)
        serializer = JobApplicationSerializer(jobs, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
#This class handle update and delete for single job

class JobApplicationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        job = get_object_or_404(JobApplication, pk=pk)
        if job.user != user:
            raise PermissionDenied("You do not have permission to access this job.")
        return job

    def get(self, request, pk):
        job = self.get_object(pk, request.user)
        serializer = JobApplicationSerializer(job)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        job = self.get_object(pk, request.user)
        job.delete()
        return Response(status=204)

    def patch(self, request, pk):
        job = self.get_object(pk, request.user)
        serializer = JobApplicationSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class NoteListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = Note.objects.filter(job__user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    

class NoteDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        note = get_object_or_404(Note, pk=pk)
        if note.job.user != user:
            raise PermissionDenied("You do not have permission to access this note.")
        return note

    def get(self, request, pk):
        note = self.get_object(pk, request.user)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=200)
    
    def patch(self, request, pk):
        note = self.get_object(pk, request.user)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        note = self.get_object(pk, request.user)
        note.delete()
        return Response(status=204)
    
class SkillListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        skills = Skill.objects.filter(job__user=request.user)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class SignUpView(APIView):
    permission_classes = [AllowAny]
    # When we recieve a POST request with username, email, and password. Create a new user.
    def post(self, request):
        # Using .get will not error if there's no username
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        # Actually create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # create an access and refresh token for the user and send this in a response
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )
    