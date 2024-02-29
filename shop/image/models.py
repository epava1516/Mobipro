from django.db import models
from django.utils import timezone
from shop.auditlog.models import AuditLog
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
# from shop.gallery.models import Gallery

# Create your models here.
class Image(models.Model):
    """
    A class representing an image in the e-shop.

    Attributes:
        gallery (ForeignKey to Gallery): The gallery to which the image belongs.
        image (ImageField): The image file.
        description (str, optional): Description of the image.
        created_at (DateTime): Date and time when the image was created.
        updated_at (DateTime): Date and time when the image was last updated.
        is_active (bool): Indicates if the image is active.
        sha256 (str): SHA256 hash of the image file content.
    """
    gallery = models.ForeignKey('gallery.Gallery', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sha256 = models.CharField(max_length=64, blank=True, editable=False)

    def __str__(self):
        return f"Image {self.id} in {self.gallery}"

    def save(self, *args, **kwargs):
        if not self.pk:
            # Calculate the SHA256 hash when the image is being saved for the first time
            self.sha256 = self.calculate_sha256()
        super().save(*args, **kwargs)

    def calculate_sha256(self):
        """
        Calculate the SHA256 hash of the image file content.
        """
        with self.image.open('rb') as f:
            return hashlib.sha256(f.read()).hexdigest()

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
            model_name='Image',
            instance_id=self.id,
            action=action,
            user=user,
            changed_fields=changed_fields
        )

@receiver(post_save, sender=Image)
def image_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on Image model.
    """
    user = kwargs.pop('user', None)
    action = 'create' if created else 'update'
    changed_fields = get_changed_fields(instance)
    AuditLog.objects.create(
        model_name='Image',
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
