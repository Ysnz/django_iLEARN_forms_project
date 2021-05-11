from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    phone = models.CharField(max_length=45)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return self.email
    