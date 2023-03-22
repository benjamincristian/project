from django.urls import path

from post import views

urlpatterns = [
    path('new_blog/', views.PostCreateView.as_view(), name='new-blog'),
    path('new_post/', views.PostListView.as_view(), name='view-blog'),
    path('update_post/<int:pk>/', views.PostUpdateView.as_view(), name='update-blog'),
    path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete-blog')
    ]
