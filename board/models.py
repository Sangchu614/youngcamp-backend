from django.db import models
from .validators import validate_no_profanity

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(validators=[validate_no_profanity])
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(validators=[validate_no_profanity])
    
    def __str__(self):
        return f'댓글 on {self.post.id}'