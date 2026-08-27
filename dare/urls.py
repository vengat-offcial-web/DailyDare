from django.urls import path
from . import views

urlpatterns = [
    path('',views.challenge_list, name = "challenge_list"),
    path('accept/<int:challenge_id>/',views.accept_dare, name= 'accept_dare'),
]