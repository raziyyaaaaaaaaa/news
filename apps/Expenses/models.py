from django.db import models

# Create your models here.

class Expense(models.Model):
    category = models. CharField(max_length=100)
    amount= models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    def _str_(self):
        return f"{self.category} - {self.amount}"
