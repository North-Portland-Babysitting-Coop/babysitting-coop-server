from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("Bob", "bob@bob.net", "asdfbob")
        user.last_name = "McBob"
        user.save()

    def authenticateBob(self):
        return authenticate(username="Bob", password="asdfbob")

    def testAuthentication(self):
        user = self.authenticateBob()
        self.assertTrue(user is not None)

    def testUserAttribute(self):
        user = self.authenticateBob()
        self.assertEquals(user.last_name, "McBob")
