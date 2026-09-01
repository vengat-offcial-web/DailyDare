from .models import Challenge,UserChallenge
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone

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
    
    return redirect('active_dare',userchallenge_id = user_challenge.id)

def active_dare(request, userchallenge_id):
    user_challenge = get_object_or_404(UserChallenge, id=userchallenge_id)
    
    # Total seconds
    total_seconds = user_challenge.challenge.time_limit * 60
    
    # Elapsed seconds
    elapsed_seconds = (timezone.now() - user_challenge.active_at).total_seconds()
    
    # Remaining seconds
    remaining_seconds = int(total_seconds - elapsed_seconds)
    if remaining_seconds <= 0:
        remaining_seconds = 0
        
    context = {
        'user_challenge': user_challenge,
        'remaining_seconds': remaining_seconds
    }
    
    return render(request, "active_dare.html", context)

def complete_dare(request, task_id):
    task = get_object_or_404(UserChallenge, id=task_id)
    
    if task.status == "IN_PROGRESS":
        total_seconds = task.challenge.time_limit * 60
        elapsed_seconds = (timezone.now() - task.active_at).total_seconds()
        
        if elapsed_seconds > total_seconds:
            task.status = "FAILED"
        else:
            task.status = "COMPLETED"
            
        task.save()
        
    return redirect('home')
def giveup_dare(request,task_id):
    
    task = get_object_or_404(UserChallenge, id = task_id)
    
    if task.status == "IN_PROGRESS":
        
        task.status = "FAILED"
        task.save()
        
    return redirect('home')
    