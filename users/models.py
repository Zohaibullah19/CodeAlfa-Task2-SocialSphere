# users/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(
        blank=True,
        max_length=500,
        help_text="Tell us about yourself!"
    )
    profile_picture = models.ImageField(
        upload_to='profiles/',
        default='profiles/default.png',
        blank=True
    )
    cover_photo = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True
    )
    # The updated_at field is essential; ensure you run 'makemigrations' and 'migrate' after adding this
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'