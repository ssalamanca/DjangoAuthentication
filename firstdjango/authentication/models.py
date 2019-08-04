from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        """A string representation of the model."""
        return self.user