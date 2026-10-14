from .models import Challenge, UserChallenge
from django.shortcuts import redirect,render,get_object_or_404

def home(request):
    
    challenge = Challenge.objects.order_by('?').first()
    context = {'dare' : challenge}
    return render(request,'home.html', context)

def accept_dare(request, dare_id):
    
    challenge =get_object_or_404(Challenge, id = dare_id)
    
    user_challenge = UserChallenge.objects.create(
        
        user = request.user,
        challenge = challenge,
        status = "IN_PROGRESS"    
    )
    
    return redirect('active_dare', challenge_id = user_challenge.id)

def active_dare(request, challenge_id):
    
    user_challenge = get_object_or_404(UserChallenge, id = challenge_id)
    context = {
        'user_challenge' : user_challenge
    }
    
    return render(request,'active_dare.html',context)

def complete_dare(request, challenge_id):
    
    user_challenge = get_object_or_404(UserChallenge, id = challenge_id)
    
    user_challenge.status = "COMPLETED"
    user_challenge.save()
    
    return redirect('home')

def giveup_dare(request, challenge_id):
    
    user_challenge = get_object_or_404(UserChallenge, id = challenge_id)
    
    user_challenge.status = "FAILED"
    user_challenge.save()
    
    return redirect('home')
    
    
    