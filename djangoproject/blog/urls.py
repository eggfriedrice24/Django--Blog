from django.urls import path
from blog import views
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, likeview






urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.About.as_view(), name='blog-about'),
    path('contact/', views.Contact.as_view(), name='blog-contact'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('like/<int:pk>/', likeview, name='like-post'),

]


