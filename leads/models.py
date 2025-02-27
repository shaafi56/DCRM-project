from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Agent(models.Model): # is a foreignkey model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #uma bahnin first_name and user_name waxa no qabilsan AbstractUser
    def __str__(self):
        return self.user.email
	
# Create your models here named lead
class lead(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}"
    