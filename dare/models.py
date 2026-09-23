from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy" , "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard")
    ]
    
    title = models.CharField(max_length= 50)
    description = models.CharField(max_length= 225)
    difficulty = models.CharField(max_length= 10, choices=DIFFICULTY_CHOICES, default= "Easy")
    time_limit = models.IntegerField(help_text= "In miniutes")
    points = models.IntegerField(default= 0)
    
class UserChallenge(models.Model):
    STATUS_CHOICES = [
        ('IN_PROGRESS', 'In_Progress'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed')
    ]
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete= models.CASCADE)
    status = models.CharField(max_length= 20, choices= STATUS_CHOICES, default= "IN_PROGRESS")
    active_at = models.DateTimeField(auto_now_add= True)
    