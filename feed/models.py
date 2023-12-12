
from django.db import models
from model_utils.models import TimeStampedModel
from users.models import User  

class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.URLField(blank=True) 
    video = models.URLField(blank=True)  
    liked_by = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Post by {self.user.name}"

    @property
    def like_count(self):
        return self.liked_by.count()


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='nested_comments')
    content = models.TextField()
    liked_by = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    
    def __str__(self):
        return f"Comment by {self.user.name} on {self.post.id}"
    
    @property
    def like_count(self):
        return self.liked_by.count()
