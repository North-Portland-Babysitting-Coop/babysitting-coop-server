from django.db import models
from django.contrib.auth.models import User
from .family import Family

class Adult(User):
    family = models.OneToOneField(Family, on_delete=models.PROTECT)
