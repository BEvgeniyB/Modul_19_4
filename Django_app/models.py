from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title