from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JobApplication
from .serializers import JobApplicationSerializer

class JobApplicationListCreate(APIView):
    def get(self, request):
        jobs = JobApplication.objects.all()
        serializer = JobApplicationSerializer(jobs, many=True)
        return Response(serializer.data, status=200)