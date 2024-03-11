from django.db import models
class Works(models.Model):
    person_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)  # Add this line for the company name
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Lives(models.Model):
    person_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
