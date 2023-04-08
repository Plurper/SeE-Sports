from django.db import models
from django.contrib.auth.models import User

#This model defines a clip with a title, description, URL, 
# author, and creation date. The author field is a foreign key to 
# the built-in User model, which will allow you to associate clips 
# with specific users.
class Clip(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title