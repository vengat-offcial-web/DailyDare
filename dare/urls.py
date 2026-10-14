from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name= 'home'),
    path('accept<int:dare_id>/', views.accept_dare, name='accept_dare'),
    path('active<int:challenge_id>/', views.active_dare, name = 'active_dare'),
    path('complete/<int:challenge_id/', views.complete_dare, name='complete_dare'),
    path('giveup/<int:challenge_id>/', views.giveup_dare, name= 'giveup_dare')
]