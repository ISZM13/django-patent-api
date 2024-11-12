from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Patent
from .serializers import PatentSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Avg, Min, Max, Count
import numpy as np
from datetime import datetime
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
    
    
# Summary endpoint
class SummaryStatistics(APIView):
    def get(self, request, *args, **kwargs):
        summary_data = {
            "priority_date": {
                "min": Patent.objects.aggregate(Min('priority_date'))['priority_date__min'],
                "max": Patent.objects.aggregate(Max('priority_date'))['priority_date__max']
            },
            "creation_date": {
                "min": Patent.objects.aggregate(Min('creation_date'))['creation_date__min'],
                "max": Patent.objects.aggregate(Max('creation_date'))['creation_date__max']
            },
            # Add more fields as needed
        }
        return Response(summary_data, status=status.HTTP_200_OK)

# Query endpoint
class QueryPatentData(APIView):
    def get(self, request, *args, **kwargs):
        query_params = {}
        if 'patent_year' in request.query_params:
            query_params['creation_date__year'] = int(request.query_params['patent_year'])
        if 'assignee' in request.query_params:
            query_params['assigne__icontains'] = request.query_params['assignee']
        
        queryset = Patent.objects.filter(**query_params)
        serializer = PatentSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)