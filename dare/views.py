from .models import Challenge, UserChallenge
from django.shortcuts import redirect,render,get_object_or_404

def home(request):
    
    challenge = Challenge.objects.order_by('?').first()
    context = {'dare' : challenge}
    return render(request,'home.html', context)

def accept_dare(request, dare_id):
    
    challenge = get_object_or_404(Challenge, id = dare_id)
    
    user_challenge = UserChallenge.objects.create(
        
        user = request.user,
        challenge = challenge,
        status = 'IN_PROGRESS'
    )
    
    return redirect('active_challenge', challenge_id = user_challenge.id)
    
    