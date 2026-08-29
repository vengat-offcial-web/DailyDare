
from .models import Challenge,UserChallenge
from django.shortcuts import render

def challenge_list(request):
    all_challenges = Challenge.objects.all()
    
    context = {'challenges':all_challenges}
    
    return render (request, 'home.html',context)
    
    