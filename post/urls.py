from django.urls import path

from post import views

urlpatterns = [
    path('create_post/', views.PostCreateView.as_view(), name='new-blog'),
    path('all_posts/', views.PostListView.as_view(), name='view-blog'),
    path('update_post/<int:pk>/', views.PostUpdateView.as_view(), name='update-blog'),
    path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete-blog'),
    path('detail_view_post/<int:pk>/', views.PostDetailView.as_view(), name='detail-blog')
    ]
