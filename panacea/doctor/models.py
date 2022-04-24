from django.db import models
from django.urls import reverse

# Create your models here.
class AddressDb(models.Model):   
    doc_id = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    pin_code = models.IntegerField()
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    class Meta:
        db_table = "addressdb"

class SpecialityDb(models.Model):   
    doc_id = models.CharField(max_length=10)
    speciality = models.CharField(max_length=20, default="None")
    class Meta:
        db_table = "specialitydb"

class PostDb(models.Model):
    doc_id = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    post_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = "postdb"