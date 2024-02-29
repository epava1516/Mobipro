from django.db import models
from django.utils import timezone
from shop.auditlog.models import AuditLog
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tag(models.Model):
    """
    A class representing a tag for products in the e-shop.

    Attributes:
        name (str): The name of the tag. (unique=True)
        created_at (DateTime): Date and time when the tag was created.
        updated_at (DateTime): Date and time when the tag was last updated.
        is_active (bool): Indicates if the tag is active.
    """
    name = models.CharField(max_length=255, unique=True, db_index=True)  
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        """
        Override the default delete method to set is_active to False instead of deleting.
        """
        user = kwargs.pop('user', None)  
        self.is_active = False
        self.save()
        action = 'delete'
        changed_fields = None  
        AuditLog.objects.create(
            model_name='Tag',
            instance_id=self.id,
            action=action,
            user=user,
            changed_fields=changed_fields
        )

@receiver(post_save, sender=Tag)
def tag_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on Tag model.
    """
    user = kwargs.pop('user', None)  
    action = 'create' if created else 'update'
    changed_fields = get_changed_fields(instance)
    AuditLog.objects.create(
        model_name='Tag',
        instance_id=instance.id,
        action=action,
        user=user,
        changed_fields=changed_fields
    )

def get_changed_fields(instance):
    """
    Helper function to get the changed fields and their values as JSON.
    """
    if instance._state.adding:
        return None
    model_class = instance.__class__
    old_instance = model_class._default_manager.get(pk=instance.pk)
    changed_fields = {}
    for field in instance._meta.fields:
        if getattr(old_instance, field.attname) != getattr(instance, field.attname):
            changed_fields[field.attname] = {
                'old_value': getattr(old_instance, field.attname),
                'new_value': getattr(instance, field.attname)
            }
    return changed_fields
