from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]