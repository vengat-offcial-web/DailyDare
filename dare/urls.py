from django.urls import path
from . import views

urlpatterns = [
    path('',views.challenge_list, name= 'home'),
    path('accept/<int:dare_id>', views.accept_dare , name= 'accept_dare'),
    path('active/<int:userchallenge_id>',views.active_dare, name= 'active_dare'),
    
]