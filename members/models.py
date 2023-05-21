from django.db import models

# Create your models here.
class Members(models.Model):
    email = models.CharField(max_length=66, primary_key=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Name")
    last_name = models.CharField(max_length=255, default="doe")
    GENDER_CHOISES=(
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other")
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES, default="M")
