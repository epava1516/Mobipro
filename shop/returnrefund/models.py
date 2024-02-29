from django.db import models
from django.utils import timezone
from shop.auditlog.models import AuditLog
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.order.models import Order

class ReturnRefund(models.Model):
    """
    A class representing return and refund information for orders in the e-shop.

    Attributes:
        order (ForeignKey to Order): The order associated with the return/refund.
        reason (str): The reason for the return/refund.
        status (str): The current status of the return/refund.
        return_date (DateTime): The date when the return was initiated.
        refund_date (DateTime, optional): The date when the refund was processed.
        amount_refunded (Decimal, optional): The amount refunded for the return.
        is_active (bool): Indicates if the return/refund information is active.
        created_at (DateTime): The datetime when the return/refund information was created.
        updated_at (DateTime): The datetime when the return/refund information was last updated.
    """
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=255)
    return_date = models.DateTimeField(default=timezone.now)
    refund_date = models.DateTimeField(blank=True, null=True)
    amount_refunded = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Return/Refund for Order {self.order.order_number}"

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
            model_name='ReturnRefund',
            instance_id=self.id,
            action=action,
            user=user,
            changed_fields=changed_fields
        )

@receiver(post_save, sender=ReturnRefund)
def return_refund_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on ReturnRefund model.
    """
    user = kwargs.pop('user', None)
    action = 'create' if created else 'update'
    changed_fields = get_changed_fields(instance)
    AuditLog.objects.create(
        model_name='ReturnRefund',
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
