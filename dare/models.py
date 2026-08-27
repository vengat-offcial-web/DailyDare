from django.db import models

# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length= 225)
    description = models.TextField()
    category = models.CharField(max_length= 100)
    difficulty = models.CharField(max_length= 20)
    time_limit = models.IntegerField()
    points = models.IntegerField(default=10)
    
    def __str__(self):
        return self.title
    
class UserChallenge(models.Model):
    STATUS_CHOICES = [
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED','Completed'),
        ('FAILED','Failed'),
    ]
    
    challenge = models.ForeignKey(Challenge, on_delete = models.CASCADE)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='IN_PROGRESS')
    accepted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.challenge.title} - {self.status}"