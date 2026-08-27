from django.shortcuts import render, redirect, get_object_or_404
from .models import Challenge, UserChallenge

def challenge_list(request):
    challenge = Challenge.objects.order_by('?').first()
    
    context = {'challenge' : challenge}
    
    return render(request, "challenge.html", context)


# Accept Dare View

def accept_dare(request,challenge_id):
    challenge = get_object_or_404(Challenge, id = challenge_id)
    
    UserChallenge.objects.create(
        challenge = challenge,
        status = 'IN_PROGRESS',
    )
    
    return redirect('challenge_list')
