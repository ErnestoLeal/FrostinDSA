from django.db import models
from django.contrib.auth.models import User

# Challenge model to represent coding problems
class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    tags = models.CharField(max_length=200)  # For topics, e.g., "arrays, dynamic programming"

    def __str__(self):
        return self.title

# ChallengeAttempt model to track user's performance on each attempt
class ChallengeAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    score = models.IntegerField()  # Use a metric for scoring
    time_taken = models.DurationField()
    attempt_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failure', 'Failure')])

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"