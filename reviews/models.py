from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Review(models.Model):
    """
    A single review
    """
    written_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    
    def __unicode__(self):
        return self.title
        
class Comment(models.Model):
    """
    Allows a user to comment on a review
    """
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    comment = models.TextField()
    created_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    
    def __unicode__(self):
        return self.comment