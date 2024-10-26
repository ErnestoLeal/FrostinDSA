"""
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ChallengeAttemptForm

# Create your views here.
from .models import Challenge

def challenge_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/challenge_list.html', {'challenges': challenges})


def submit_attempt(request):
    if request.method == 'POST':
        form = ChallengeAttemptForm(request.POST)
        if form.is_valid():
            attempt = form.save(commit=False)
            attempt.user = request.user
            attempt.save()
            return redirect('challenge_list')
    else:
        form = ChallengeAttemptForm()
    return render(request, 'challenges/submit_attempt.html', {'form': form})
"""
"""from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ChallengeAttemptForm
from .models import Challenge"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ChallengeAttemptForm
from .models import Challenge




def home(request):
    return render(request, 'challenges/home.html')  # Ensure you create this template

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
def progress_tracking(request):
    
    context = {}
    
    return render(request, 'challenges/progress_tracking.html', context)
