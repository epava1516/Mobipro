import unittest
from django.test import TestCase
from shop.product.models import Product

# Create your tests here.
class ProductModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', description='Test Description', price=10.0, stock=100)

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.price, 10.0)
        self.assertEqual(self.product.stock, 100)
