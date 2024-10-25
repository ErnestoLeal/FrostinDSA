from django import forms
from .models import ChallengeAttempt

class ChallengeAttemptForm(forms.ModelForm):
    class Meta:
        model = ChallengeAttempt
        fields = ['challenge', 'score', 'time_taken', 'status']
