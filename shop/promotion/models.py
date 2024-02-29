from django.db import models
from django.utils import timezone
from shop.auditlog.models import AuditLog
from django.db.models.signals import post_save
from django.dispatch import receiver

class Promotion(models.Model):
    """
    A class representing a promotion in the e-shop.

    Attributes:
        name (str): The name of the promotion. (unique=True)
        description (str): The description of the promotion.
        discount_percent (Decimal): The discount percentage of the promotion.
        start_date (DateTime): The start date of the promotion.
        end_date (DateTime): The end date of the promotion.
        created_at (DateTime): The datetime when the promotion was created.
        updated_at (DateTime): The datetime when the promotion was last updated.
        is_active (bool): Indicates if the promotion is active.
    """
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.TextField(max_length=1000)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)  # Representing discount as percentage
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
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
            model_name='Promotion',
            instance_id=self.id,
            action=action,
            user=user,
            changed_fields = changed_fields
        )

@receiver(post_save, sender=Promotion)
def promotion_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on Promotion model.
    """
    user = kwargs.pop('user', None)  # Obtener el usuario pasado como parámetro
    action = 'create' if created else 'update'
    changed_fields = get_changed_fields(instance)
    AuditLog.objects.create(
        model_name='Promotion',
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
