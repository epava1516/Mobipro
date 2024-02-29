from django.db import models
from django.utils import timezone
from shop.auditlog.models import AuditLog
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.product.models import Product

class Comment(models.Model):
    """
    A class representing a comment in the e-shop.

    Attributes:
        user (ForeignKey to User): The user who posted the comment.
        product (ForeignKey to Product): The product the comment belongs to.
        text (str): The content of the comment.
        created_at (DateTime): The datetime when the comment was posted.
        updated_at (DateTime): The datetime when the comment was last updated.
        is_active (bool): Indicates if the comment is active.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.name}"
    
    def delete(self, *args, **kwargs):
        """
        Override the default delete method to set is_active to False instead of deleting.
        """
        user = kwargs.pop('user', None)  # Obtener el usuario pasado como parámetro
        self.is_active = False
        self.save()
        action = 'delete'
        changed_fields = None  # Since the instance is not being deleted, no fields are changed
        AuditLog.objects.create(
            model_name='Comment',
            instance_id=self.id,
            action=action,
            user=user,
            changed_fields = changed_fields
        )

@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on Comment model.
    """
    user = kwargs.pop('user', None)  # Obtener el usuario pasado como parámetro
    action = 'create' if created else 'update'
    changed_fields = get_changed_fields(instance)
    AuditLog.objects.create(
        model_name='Comment',
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
