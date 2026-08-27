from django.shortcuts import render
from .models import Challenge

def challenge_list(request):
    challenge = Challenge.objects.order_by('?').first()
    
    context = {'challenge' : challenge}
    
    return render(request, "challenge.html", context)

