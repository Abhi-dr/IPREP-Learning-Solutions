from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



