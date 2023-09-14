# from django.db import models

# # Create your models here.
# class Profile(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/', 
#                               blank=True, null=True)  

from django.db import models

# Create your models here.
class Profile(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.name), filename])
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=nameFile, 
                              blank=True, null=True) 
