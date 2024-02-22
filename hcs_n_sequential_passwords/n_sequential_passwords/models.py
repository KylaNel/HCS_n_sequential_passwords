from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField(blank=True)
    pattern_lock = models.JSONField(blank=True)
    pin = models.PositiveSmallIntegerField(blank=True)
    password = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return self.username