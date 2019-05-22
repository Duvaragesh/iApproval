#
# Author Duvaragesh Kannan
#
from django.db import models

# Create your models here.

class Emp_details(models.Model):
    Empid = models.CharField(max_length=30)
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.CharField(max_length=60)
    Team_Name = models.CharField(max_length=50)
    Request_Number = models.CharField(max_length=50, blank=True)
    Request_Status = models.CharField(max_length=50, blank=True) 
    Sub_Request_Number = models.CharField(max_length=50, blank=True)
    Sub_Request_Status = models.CharField(max_length=50, blank=True) 