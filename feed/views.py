from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from authentication.authentication import TokenAuthentication
from feed.models import Comment, Post
from .serializers import CommentSerializer, PostSerializer

class CreatePostView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LikePostView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id, format=None):
        post = Post.objects.get(id=post_id)
        if request.user in post.liked_by.all():
            post.liked_by.remove(request.user)
            action = 'disliked'
        else:
            post.liked_by.add(request.user)
            action = 'liked'
        return Response({"message": f"Post {action}"}, status=status.HTTP_200_OK)

class AddCommentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Comment added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LikeCommentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, comment_id, format=None):
        comment = Comment.objects.get(id=comment_id)
        if request.user in comment.liked_by.all():
            comment.liked_by.remove(request.user)
            action = 'disliked'
        else:
            comment.liked_by.add(request.user)
            action = 'liked'
        return Response({"message": f"Comment {action}"}, status=status.HTTP_200_OK)
