from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.dispatch import receiver
from django.db.models.signals import post_save

import uuid

from .managers import UserManager

sex_choices = [
    ("male", "Male"), 
    ("female", "Femal"),
    ("other", "Other"),
    ]

class User(AbstractUser):
    """
    User model for authentication
    """
    
    id = models.BigAutoField(primary_key=True, editable=False)

    implicit_id = models.UUIDField(
        default = uuid.uuid4,
        unique=True,
        editable = False
    )

    username = None
    email = models.EmailField(_("email address"), unique=True, blank=False, null=False, default="")

    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_user_with_id (self, s: str) -> "User":
        """
        Get user with UUID string
        """

        return User.objects.get(implicit_id=s)

class UserSettings(models.Model):
    """
    User settings model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")

    # Language
    language = models.CharField(max_length=8, default="en")

    # Age
    age = models.PositiveIntegerField(default=25)

    # Sex
    sex = models.CharField(choices=sex_choices, default="other")

    class Meta:
        verbose_name = "User Settings"
        verbose_name_plural = "User Settings"
        
    def __str__(self):
        return f"Settings for {self.user.email}"
    
    def get_user_settings (self, user: User) -> "UserSettings":
        return UserSettings.objects.get(user=user)
    
@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        UserSettings.objects.create(user=instance)
