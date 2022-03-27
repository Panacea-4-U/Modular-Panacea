from django.db import models
from django.urls import reverse

# Create your models here.
class TempDb(models.Model):   
    name = models.CharField(max_length=50)
    email = models.EmailField()
    ph_no = models.CharField(max_length=15)
    class Meta:
        db_table = "tempdb"

class Patient(models.Model):   
    pat_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "patient"
        
class Doctor(models.Model):   
    doc_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    licence_no = models.CharField(max_length=50)
    speciality = models.CharField(max_length=20, default="None")
    class Meta:
        db_table = "doctor"
    def get_absolute_url(self):
            return reverse('services', kwargs={'pk': self.pk})