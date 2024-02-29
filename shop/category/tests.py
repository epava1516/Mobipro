import unittest
from django.test import TestCase
from shop.category.models import Category

class CategoryModelTestCase(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')
