from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # category = models.ForeignKey('Post', on_delete=models.SET_DEFAULT(None))
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    

class HashTag(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return self.name