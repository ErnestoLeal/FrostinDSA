from django.urls import path
from . import views  # Importing views from the current app

urlpatterns = [
    path('', views.home, name='homepage'),  # URL pattern for the homepage
    path('list/', views.challenge_list, name='challenge_list'),  # URL pattern for listing challenges
    path('submission/', views.submit_attempt, name='submit_attempt'),  # URL pattern for submitting attempts
    path('progress/', views.progress_tracking, name='progress_tracking')
]
