from django.db import models
from django.utils import timezone

class Client(models.Model):
    """
    A class representing a client in the e-shop.

    Attributes:
        first_name (str): The first name of the client.
        last_name (str): The last name of the client.
        email (str): The email address of the client. (unique=True)
        phone_number (str, optional): The phone number of the client.
        date_of_birth (Date, optional): The date of birth of the client.
        gender (str, optional): The gender of the client.
        shipping_address (str, optional): The shipping address of the client.
        billing_address (str, optional): The billing address of the client.
        card_number (str, optional): The credit card number of the client.
        account_status (str, choices=['Active', 'Inactive', 'Suspended']): The status of the client's account.
        balance_due (Decimal): The balance due from the client.
        payment_history (OneToMany to Payment): The payment history of the client.
        last_interaction_date (DateTime, optional): The date of the last interaction with the client.
        follow_up_notes (TextField, optional): Notes for follow-up interactions with the client.
        customer_segment (str, choices=['Potential', 'Regular', 'VIP']): The segment/category of the client.
        customer_behavior_score (Decimal, optional): The behavior score of the client.
        source_of_reference (str, choices=['Referral', 'Advertising', 'Online Search', 'Other']): The source of reference for the client.
        customer_goals (TextField, optional): The goals and expectations of the client.
        financial_notes (TextField, optional): Additional financial notes related to the client.
        created_at (DateTime): The datetime when the client was created.
        updated_at (DateTime): The datetime when the client was last updated.
        deleted_at (DateTime, optional): The datetime when the client was soft deleted.
        is_active (bool): Indicates if the client is active.
    """
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    ACCOUNT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Suspended', 'Suspended'),
    ]

    SOURCE_OF_REFERENCE_CHOICES = [
        ('Referral', 'Referral'),
        ('Advertising', 'Advertising'),
        ('Online Search', 'Online Search'),
        ('Other', 'Other'),
    ]

    CUSTOMER_SEGMENT_CHOICES = [
        ('Potential', 'Potential'),
        ('Regular', 'Regular'),
        ('VIP', 'VIP'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Restricción unique=True para evitar correos duplicados
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    shipping_address = models.CharField(max_length=500, blank=True, null=True)
    billing_address = models.CharField(max_length=500, blank=True, null=True)
    card_number = models.CharField(max_length=20, blank=True, null=True)
    account_status = models.CharField(max_length=10, choices=ACCOUNT_STATUS_CHOICES, default='Active')
    balance_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_history = models.OneToMany('Payment', related_name='client')  # Relación con el historial de pagos del cliente
    last_interaction_date = models.DateTimeField(blank=True, null=True)
    follow_up_notes = models.TextField(blank=True, null=True)
    customer_segment = models.CharField(max_length=10, choices=CUSTOMER_SEGMENT_CHOICES, blank=True, null=True)
    customer_behavior_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    source_of_reference = models.CharField(max_length=20, choices=SOURCE_OF_REFERENCE_CHOICES, blank=True, null=True)
    customer_goals = models.TextField(blank=True, null=True)
    financial_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
