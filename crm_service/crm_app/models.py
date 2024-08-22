from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

import uuid

class Customer(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=250)

    updated_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    photo = models.ImageField(upload_to="customer_photos")




class CustomUser(AbstractUser):
    pass