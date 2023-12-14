from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'image', 'video', 'like_count']
        read_only_fields = ['like_count', 'user']
    
    def save(self, **kwargs):
        user = kwargs.pop('user', None)
        post = Post(**self.validated_data, user=user)
        post.save()
        return post