from django.urls import path
from . import views

urlpatterns = [
    path('',views.challenge_list, name = "challenge_list"),
    path('accept/<int:challenge_id>/',views.accept_dare, name= 'accept_dare'),
    path('complete/<int:user_challenge_id>/',views.complete_dare, name= 'complete_dare'),
    path('giveup/<int:user_challenge_id>/', views.giveup_dare, name= 'giveup_dare'),
]