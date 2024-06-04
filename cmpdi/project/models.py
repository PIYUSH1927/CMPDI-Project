from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    department_id = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.department_name