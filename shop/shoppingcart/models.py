from django.db import models
from django.contrib.auth.models import User
from shop.product.models import Product

class ShoppingCart(models.Model):
    """
    A class representing a user's shopping cart in the e-shop.

    Attributes:
        user (ForeignKey to User): The user who owns the shopping cart.
        created_at (DateTime): The datetime when the shopping cart was created.
        updated_at (DateTime): The datetime when the shopping cart was last updated.
        is_active (bool): Indicates if the shopping cart is active.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Shopping Cart for {self.user.username}"

class ShoppingCartItem(models.Model):
    """
    A class representing an item in a user's shopping cart.

    Attributes:
        shopping_cart (ForeignKey to ShoppingCart): The shopping cart to which the item belongs.
        product (ForeignKey to Product): The product in the shopping cart.
        quantity (PositiveIntegerField): The quantity of the product in the shopping cart.
    """
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Default quantity is 1

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
