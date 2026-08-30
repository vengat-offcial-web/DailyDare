from django.db import models


class Challenge(models.Model):
    
    title = models.CharField(max_length= 225)
    description = models.TextField(max_length= 225)
    category = models.CharField(max_length= 100)
    difficulty = models.CharField(max_length= 50)
    time_limit = models.IntegerField(default= 15)
    points = models.IntegerField(default=10)
    
    def __str__(self):
        return self.title


class UserChallenge(models.Model):
    challenge = models.ForeignKey (Challenge, on_delete= models.CASCADE)
    
    STATUS_CHOICES = [
       ('IN_PROGRESS','In Progress'),
        ('COMPLETED','Completed'),
        ('FAILED','Failed')
    ]
    
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default= "IN_PROGRESS")
    active_at = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f"{self.challenge.title} - {self.status} "  