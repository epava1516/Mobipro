from django.db import models
from django.utils import timezone
from shop.auditlog.models import AuditLog
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.order.models import Order

class Shipping(models.Model):
    """
    A class representing shipping information for orders in the e-shop.

    Attributes:
        order (ForeignKey to Order): The order associated with the shipping.
        carrier (str): The carrier or shipping company.
        tracking_number (str): The tracking number for the shipment.
        shipping_date (DateTime): The date when the shipment was shipped.
        estimated_delivery_date (DateTime): The estimated delivery date of the shipment.
        actual_delivery_date (DateTime, optional): The actual delivery date of the shipment.
        status (str): The current status of the shipment.
        address (str): The shipping address.
        is_active (bool): Indicates if the shipping information is active.
        created_at (DateTime): The datetime when the shipping information was created.
        updated_at (DateTime): The datetime when the shipping information was last updated.
    """
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    carrier = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    shipping_date = models.DateTimeField()
    estimated_delivery_date = models.DateTimeField()
    actual_delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shipping for Order {self.order.order_number}"

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
            model_name='Shipping',
            instance_id=self.id,
            action=action,
            user=user,
            changed_fields=changed_fields
        )

@receiver(post_save, sender=Shipping)
def shipping_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on Shipping model.
    """
    user = kwargs.pop('user', None)
    action = 'create' if created else 'update'
    changed_fields = get_changed_fields(instance)
    AuditLog.objects.create(
        model_name='Shipping',
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
