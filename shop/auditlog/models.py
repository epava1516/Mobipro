from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import JSONField

class AuditLog(models.Model):
    """
    A class representing an audit log for tracking changes to models.

    Attributes:
        model_name (str): The name of the model being audited.
        instance_id (int): The ID of the instance being audited.
        action (str): The action performed (create, update, delete).
        user (ForeignKey to User): The user who performed the action.
        changed_fields (JSONField): JSON containing the fields that were changed and their old/new values.
        timestamp (DateTime): The datetime when the action was performed.
    """
    model_name = models.CharField(max_length=255)
    instance_id = models.PositiveIntegerField()
    action = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    changed_fields = JSONField()
    timestamp = models.DateTimeField(default=timezone.now)
