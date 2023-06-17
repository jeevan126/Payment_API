from django.contrib.auth.models import User
from django.db import models

class Wallet(models.Model):
    coins = models.IntegerField(default=1000)
    start_time = models.DateTimeField(null=True, blank=True)

    