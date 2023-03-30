from django.urls import path
from post import views
from post.views import like_view, dislike_view, comment_like_view

urlpatterns = [
    path('create_post/', views.PostCreateView.as_view(), name='new-blog'),
    path('all_posts/', views.PostListView.as_view(), name='view-blog'),
    path('update_post/<int:pk>/', views.PostUpdateView.as_view(), name='update-blog'),
    path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete-blog'),
    path('detail_view_post/<int:pk>/', views.PostDetailView.as_view(), name='detail-blog'),
    path('like/<int:pk>/', like_view, name='like_post'),
    path('dislike/<int:pk>/', dislike_view, name='dislike_post'),
    path('search/', views.search_bar, name='search'),
    path('comment_like/<int:pk>/', comment_like_view, name='comment-like')
]
