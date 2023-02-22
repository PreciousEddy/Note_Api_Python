from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.





from django.test import TestCase


class Notes(models.Model):

    title = models.CharField(max_length=200)

    text = models.TextField()


    def __str__(self):
        return self.title # returns the title of each notes
    
    
@receiver(post_save, sender=User)
def generate_auth_token(sender, instance=None, created=False, **kwargs):
    
    if created:
        
        Token.objects.create(user=instance)
    
