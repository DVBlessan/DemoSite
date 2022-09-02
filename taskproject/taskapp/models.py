from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
class Team(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=200)
    dec=models.TextField()

    def __str__(self):
        return self.name