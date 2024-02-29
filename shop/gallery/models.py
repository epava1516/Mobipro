from django.db import models
from django.utils import timezone
from shop.auditlog.models import AuditLog
from django.db.models.signals import post_save
from django.dispatch import receiver

class Gallery(models.Model):
    """
    A class representing a gallery for images in the e-shop.

    Attributes:
        name (str): The name of the gallery. (unique=True)
        description (str, optional): Description of the gallery.
        main_image (ForeignKey to Image, optional): The main image for the gallery.
        created_at (DateTime): Date and time when the gallery was created.
        updated_at (DateTime): Date and time when the gallery was last updated.
        is_active (bool): Indicates if the gallery is active.
    """
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    main_image = models.ForeignKey('image.Image', on_delete=models.SET_NULL, blank=True, null=True, related_name='main_image')
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
            model_name='Gallery',
            instance_id=self.id,
            action=action,
            user=user,
            changed_fields = changed_fields
        )

@receiver(post_save, sender=Gallery)
def gallery_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on Gallery model.
    """
    user = kwargs.pop('user', None)  # Obtener el usuario pasado como parámetro
    action = 'create' if created else 'update'
    changed_fields = get_changed_fields(instance)
    AuditLog.objects.create(
        model_name='Gallery',
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
