from rest_framework import serializers
from .models import Comment, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'image', 'video', 'like_count']
        read_only_fields = ['like_count', 'user']
    
    # def save(self, **kwargs):
    #     user = kwargs.pop('user', None)
    #     post = Post(**self.validated_data, user=user)
    #     post.save()
    #     return post
    def create(self, validated_data):
        # Access the user from the serializer context
        user = self.context['request'].user
        return Post.objects.create(user=user, **validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'parent_comment', 'content', 'like_count']
        read_only_fields = ['user', 'like_count']

    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(user=user, **validated_data)
