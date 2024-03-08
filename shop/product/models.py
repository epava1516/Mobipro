from enum import auto
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.auditlog.models import AuditLog
from shop.gallery.models import Gallery
from shop.category.models import Category
from shop.tag.models import Tag

class Product(models.Model):
    """
    A class representing a product in the e-shop.

    Attributes:
        name (str): The name of the product. (unique=True)
        description (str): The description of the product.
        price (Decimal): The price of the product.
        stock (PositiveIntegerField): The quantity of the product available.
        gallery (Galeria, optional): The gallery to which the product belongs.
        category (Category, optional): The category to which the product belongs.
        tags (ManyToManyField of Etiqueta, optional): The tags associated with the product.
        created_at (DateTime): The datetime when the product was created.
        updated_at (DateTime): The datetime when the product was last updated.
        is_active (bool): Indicates if the product is active.
    """
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    stock = models.PositiveIntegerField()
    gallery = models.ForeignKey(Gallery, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, db_index=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

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
            model_name='Product',
            instance_id=self.id,
            action=action,
            user=user,
            changed_fields = changed_fields
        )

@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on Product model.
    """
    user = kwargs.pop('user', None)  # Obtener el usuario pasado como parámetro
    action = 'create' if created else 'update'
    changed_fields = get_changed_fields(instance)
    AuditLog.objects.create(
        model_name='Product',
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