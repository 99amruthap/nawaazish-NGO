from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=60, default='Your Name')
    text = models.CharField(max_length=300)
    subject = models.CharField(max_length=80)
    email_id = models.EmailField()

    def __str__(self):
        return self.name



