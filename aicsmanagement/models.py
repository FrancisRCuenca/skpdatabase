from django.db import models

class Beneficiary(models.Model):
    lname = models.CharField(max_length = 30)
    fname = models.CharField(max_length = 30)
    mname = models.CharField(max_length = 30, null=True, blank=True)
    mobilenum = models.CharField(max_length = 11,null=True, blank=True)
    barangay = models.CharField(max_length = 30,null=True, blank=True)
    city = models.CharField(max_length = 30)
    assistance = models.CharField(max_length = 30)
    amount = models.IntegerField()
