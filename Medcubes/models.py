from django.db import models

# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=300)
    contact = models.CharField(max_length=100)
    body= models.TextField(
        max_length=2000,
   
        help_text="Write your message here!")

    def __str__(self):
        return self.name