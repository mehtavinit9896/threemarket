from django.db import models

# Create your models here.
class Event(models.Model):
    event_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    heading = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    image = models.FileField(upload_to='marketeers\static\marketeers\images\Events')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.event_type+' '+self.name

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.FileField(upload_to='marketeers\static\marketeers\images\Team')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
        
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='marketeers\static\marketeers\images\Client')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name        