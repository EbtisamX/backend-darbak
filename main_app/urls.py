from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Helloo, world!"})
urlpatterns = [
    path('api/hello/', hello_world),
]