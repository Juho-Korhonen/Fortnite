from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(auto_now_add=False)
    medications = models.CharField(max_length=10000)
    emergency_number = models.CharField(max_length=20,blank=True)
    extra_info = models.TextField()
    location = models.CharField(max_length=200)
    inside_facility = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Staff_member(models.Model):
    name = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    work_time = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
