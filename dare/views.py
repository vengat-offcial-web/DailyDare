from django.shortcuts import render, redirect, get_object_or_404
from .models import Challenge, UserChallenge

def challenge_list(request):
    challenge = Challenge.objects.order_by('?').first()
    
    context = {'challenge' : challenge}
    
    return render(request, "challenge.html", context)


# 1. Accept Dare View

def accept_dare(request,challenge_id):
    challenge = get_object_or_404(Challenge, id = challenge_id)
    
    UserChallenge.objects.create(
        challenge = challenge,
        status = 'IN_PROGRESS',
    )
    
    return redirect('challenge_list')

# 2. Complete Dare View

def complete_dare(request, user_challenge_id):
    user_challenge = get_object_or_404(UserChallenge, id= user_challenge_id)
    user_challenge.status = 'COMPLETED'
    user_challenge.save()
    return redirect('challenge_list')

def giveup_dare(request, user_challenge_id):
    user_challenge = get_object_or_404(UserChallenge, id = user_challenge_id)
    user_challenge.status = 'FAILED'
    user_challenge.save()
    return redirect('challenge_list')