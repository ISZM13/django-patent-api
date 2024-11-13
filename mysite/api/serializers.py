from rest_framework import serializers
from .models import Patent

class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = ['patent_id','country_code', 'title', 'assigne', 'author', 'priority_date', 'creation_date', 'publ_date', 'grant_date', 'result_link', 'fig_link']
        