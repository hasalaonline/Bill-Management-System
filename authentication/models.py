from django.db import models

# Create your models here.
from django.db import models

class WaitingList(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='')
    # Add more fields as needed

class ApprovedUser(models.Model):
    email = models.EmailField(default='')

