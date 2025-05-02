from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JobApplication,Note
from .serializers import JobApplicationSerializer,NoteSerializer
from django.shortcuts import get_object_or_404


class JobApplicationListCreate(APIView):
    def get(self, request): #get all jobs application
        jobs = JobApplication.objects.all()
        serializer = JobApplicationSerializer(jobs, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request): #add new job application
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
#This class handle update and delete for single job
class JobApplicationDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(JobApplication, pk=pk)

    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobApplicationSerializer(job)
        return Response(serializer.data, status=200)
    
    def delete(self, request, pk): # get and delete the job
        job = self.get_object(pk)
        job.delete()
        return Response(status=204)

    def patch(self, request, pk): # Get the job to update
        job = self.get_object(pk)
        serializer = JobApplicationSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class NoteListCreate(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
class NoteDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Note, pk=pk)
    
    def get(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=200)
    
    def patch(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        note = self.get_object(pk)
        note.delete()
        return Response(status=204)
    
