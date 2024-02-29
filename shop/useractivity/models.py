from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserActivity(models.Model):
    """
    A class representing user activity in the e-shop.

    Attributes:
        user (ForeignKey to User): The user who performed the activity.
        activity_type (str): The type of activity performed.
        description (str): A description of the activity.
        timestamp (DateTime): The timestamp when the activity occurred.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    # description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} - {self.timestamp}"
