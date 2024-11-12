from django.db import models

# Create your models here.
class Patent(models.Model):
    patent_id = models.CharField(max_length=16, primary_key=True)
    country_code = models.CharField(max_length=2)
    title = models.TextField()
    assigne = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    priority_date = models.DateTimeField()
    creation_date = models.DateTimeField()
    publ_date = models.DateTimeField()
    grant_date= models.DateTimeField()
    result_link= models.URLField()
    fig_link=models.URLField()

    def __str__(self):
        return self.patent_id 
