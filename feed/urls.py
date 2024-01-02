from django.urls import path
from .views import AddCommentView, CreatePostView, LikeCommentView, LikePostView

urlpatterns = [
    path('create-post/', CreatePostView.as_view(), name='create-post'),
    path('add-comment/', AddCommentView.as_view(), name='add-comment'),
    path('like-post/<int:post_id>/', LikePostView.as_view(), name='like-post'),
    path('like-comment/<int:comment_id>/', LikeCommentView.as_view(), name='like-comment'),
]
