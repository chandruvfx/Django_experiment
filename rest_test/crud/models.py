from django.db import models

# Create your models here.
class GenListItem(models.Model):
    items = models.CharField(max_length=100)
    
    def __str__(self):
        return self.items
