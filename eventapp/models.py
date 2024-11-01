from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ppicture(models.Model):
    p_image = models.ImageField(upload_to='media')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class EventCatorogy(models.Model):
    catName = models.CharField(max_length=100, unique=True, null=True)

class eventModel(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=100)
    event_descriptions = models.TextField(max_length=300)
    user  = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(EventCatorogy, on_delete=models.CASCADE,  null=True)
    
    def __str__(self):
        return self.event_name 

class BookedUser(models.Model):
    book_status = models.BooleanField(default=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_data = models.ForeignKey(eventModel, on_delete=models.CASCADE, null=True)

