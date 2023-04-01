from django.db import models
from django.contrib.auth.models import User

class Clip(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title