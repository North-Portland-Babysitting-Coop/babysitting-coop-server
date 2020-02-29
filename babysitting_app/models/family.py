from django.db import models

class Family(models.Model):

    @classmethod
    def select_options(cls):
        cls.objects.all()
