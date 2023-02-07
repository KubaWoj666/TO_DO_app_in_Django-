from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=100, null=True)
    # category
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name