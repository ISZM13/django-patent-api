from django.db import models

# Create your models here.
class Patent(models.Model):
    patent_id = models.CharField(max_length=16)
    country_code = models.CharField(max_length=2)
    title = models.TextField()
    assigne = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    priority_date = models.DateField()
    creation_date = models.DateField()
    publ_date = models.DateField()
    grant_date= models.DateField()
    result_link= models.URLField()
    fig_link=models.URLField()
    
    def __str__(self):
        return self.id
    
