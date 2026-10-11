from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name= 'home'),
    path('accept<int:dare_id>', views.accept_dare, name='accept_dare'),
    path('active<challenge_id>', views.active_dare, name = 'active_dare'),
]