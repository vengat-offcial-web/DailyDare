from .models import Challenge,UserChallenge
from django.shortcuts import render,redirect,get_object_or_404

def challenge_list(request):
    random_challenges = Challenge.objects.order_by('?').first()
    
    context = {'dare':random_challenges}
    
    return render (request, 'home.html',context)


def accept_dare(request,dare_id):
    
    challenge = get_object_or_404(Challenge, id = dare_id)
    
    user_challenge = UserChallenge.objects.create(
        challenge = challenge,
        status = "IN_PROGRESS"
    )
    
    return redirect('active_dare',user_challenge = user_challenge.id)