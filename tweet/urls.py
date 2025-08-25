from django.urls import path
from . import views

urlpatterns = [
    path('index1/', views.index1, name='index1'),
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('tweets/create/', views.tweet_create, name='tweet_create'),
    path('tweets/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweets/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('tweets/personal/create/', views.tweet_personal_list, name='tweet_personal_create'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('alert/', views.alert, name='alert'),
    # Add more URL patterns as needed
    
]
