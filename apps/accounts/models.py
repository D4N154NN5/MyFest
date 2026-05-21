from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        TEAMLEADER = "teamleader", "Teamleiter"
        HELPER = "helper", "Helfer"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.HELPER,
    )
    phone = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_teamleader(self):
        return self.role in (self.Role.ADMIN, self.Role.TEAMLEADER)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"
