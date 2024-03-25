from django.db import models
class File(models.Model):
    file = models.FileField(upload_to="files")
    email = models.EmailField(null=True,max_length=250)
class Company(models.Model):
    company_name = models.CharField(max_length=250)
    year_founded = models.CharField(max_length=100)
    industry = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    current_emp = models.CharField(null=True,max_length=100)
    total_emp = models.CharField(null=True,max_length=100)
    email = models.EmailField(null=True,max_length=250)
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
class Query(models.Model):
    keyword = models.CharField(max_length=250)
    industry = models.CharField(max_length=250)
    year_founded = models.CharField(max_length=100)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    total_emp = models.CharField(max_length=250)
    current_emp = models.CharField(max_length=250)