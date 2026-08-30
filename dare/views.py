from .models import Challenge,UserChallenge
from django.shortcuts import render

def challenge_list(request):
    random_challenges = Challenge.objects.order_by('?').first()
    
    context = {'dare':random_challenges}
    
    return render (request, 'home.html',context)

