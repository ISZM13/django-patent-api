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
from rest_framework.exceptions import ValidationError
# from django.core.cache import cache
import re
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
        # Generate a cache key based on query parameters
        # cache_key = f"query_patents_{request.get_full_path()}"
        # cached_data = cache.get(cache_key)

        # if cached_data:
        #     # Return cached data if available
        #     return Response(cached_data, status=status.HTTP_200_OK)

        query_params = {}

        # Validate patent_id
        patent_id = request.query_params.get('patent_id', None)
        if patent_id and not re.match(r'^[A-Za-z0-9\-]+$', patent_id):
            raise ValidationError({'patent_id': 'Invalid patent_id format. It should contain only alphanumeric characters and dashes.'})
        if patent_id:
            query_params['patent_id__icontains'] = patent_id

        # Validate assignee
        assignee = request.query_params.get('assignee', None)
        if assignee:
            query_params['assigne__icontains'] = assignee

        # Validate country_code (length should not be greater than 2 characters)
        country_code = request.query_params.get('country_code', None)
        if country_code:
            if len(country_code) > 2:
                raise ValidationError({'country_code': 'Invalid country_code. The length should not exceed 2 characters.'})
            query_params['country_code__iexact'] = country_code

        # If any query parameter exists, filter data
        queryset = Patent.objects.filter(**query_params)
        serializer = PatentSerializer(queryset, many=True)

        # cache.set(cache_key, serializer.data, timeout=900)

        return Response(serializer.data, status=status.HTTP_200_OK)
