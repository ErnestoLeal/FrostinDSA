"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),             # List of challenges
    path('submit_attempt/', views.submit_attempt, name='submit_attempt'),  # Submission route
]
"""

"""from django.urls import path
from . import views  # Importing views from the current app

urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),  # URL pattern for listing challenges
    path('submit_attempt/', views.submit_attempt, name='submit_attempt'),  # URL pattern for submitting attempts
]
"""
"""
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ChallengeAttemptForm
from .models import Challenge

def homepage(request):
    return render(request, 'challenges/homepage.html')  # Ensure you create this template

def challenge_list(request):
    challenges = Challenge.objects.all()  # Fetch all challenges from the database
    return render(request, 'challenges/challenge_list.html', {'challenges': challenges})  # Render the list template with challenges

@login_required  # Require users to be logged in to submit attempts
def submit_attempt(request):
    if request.method == 'POST':
        form = ChallengeAttemptForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            attempt = form.save(commit=False)  # Save form data without committing to the database yet
            attempt.user = request.user  # Associate the attempt with the logged-in user
            attempt.save()  # Save the attempt to the database
            messages.success(request, 'Your attempt has been submitted successfully!')  # Success message
            return redirect('challenge_list')  # Redirect to the challenge list page
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')  # Error message
    else:
        form = ChallengeAttemptForm()  # Create a new form instance for GET requests

    return render(request, 'challenges/submit_attempt.html', {'form': form})  # Render the submission template with the form

"""
from django.urls import path
from . import views  # Importing views from the current app

urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),  # URL pattern for listing challenges
    path('submit_attempt/', views.submit_attempt, name='submit_attempt'),  # URL pattern for submitting attempts
    path('homepage/', views.homepage, name='homepage'),  # URL pattern for the homepage
]
