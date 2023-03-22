from django.urls import path

from userextend import views

urlpatterns = [
    path('sign_in/', views.UserExtendCreateView.as_view(), name='sign-in'),
    path('view_user/', views.UserListView.as_view(), name='view')
]
