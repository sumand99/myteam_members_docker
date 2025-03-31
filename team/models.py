from django.db import models

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('regular', 'Regular - Can’t delete members'),
        ('admin', 'Admin - Can delete members'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='regular'
    )

    def __str__(self):
        return f"{self.name} ({self.role})"
