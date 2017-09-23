from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Event(models.Model):
    ONCE = 'ON'
    YEARLY = 'YE'
    FREQUENCY_CHOICES = (
        ('ON', 'once'),
        ('YE', 'yearly'),
    )

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, unique=True)
    description = models.TextField(max_length=25, null=True, blank=True)
    date = models.DateField()
    frequency = models.CharField(
        max_length=2,
        choices=FREQUENCY_CHOICES,
        default=YEARLY,
    )

    # Meta
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True),
