from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Patent
from .serializers import PatentSerializer

# Create your views here.
class PatentListCreate(generics.ListCreateAPIView):
    queryset = Patent.objects.all()
    serializer_class = PatentSerializer
    
    def delete(self, request, *args, **kwargs):
        Patent.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patent.objects.all()
    serializer_class = PatentSerializer
    lookup_field = 'patent_id'  
