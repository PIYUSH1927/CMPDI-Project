from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    department_id = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.department_name

class RandomDetail(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.DateField()
    field4 = models.CharField(max_length=200)
    field5 = models.TextField()
    field6 = models.BooleanField()
    field7 = models.DecimalField(max_digits=10, decimal_places=2)
    field8 = models.EmailField()
    field9 = models.URLField()
    field10 = models.TimeField()

    def __str__(self):
        return f"{self.field1} - {self.field2}"