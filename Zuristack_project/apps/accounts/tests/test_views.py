from django.test import TestCase
from django.contrib.auth import get_user_model

class  CustomUserManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        pass

    def test_create_superuser(self):
        pass