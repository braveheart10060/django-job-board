from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
JOB_TYPE =(
    ('full time','full time'),
    ('part time','part time'),
)
class job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15 , choices = JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField( auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiance = models.IntegerField(default=1)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
