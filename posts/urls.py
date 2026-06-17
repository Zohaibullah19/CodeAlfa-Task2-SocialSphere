from django.urls import path
from . import views
from .follow_views import follow_user

urlpatterns = [
    # Maps the empty root path directly to the feed view
    path('', views.feed, name='root_feed'),
    
    # Keeps your existing explicit feed path intact
    path('feed/', views.feed, name='feed'),

    path(
        'create-post/',
        views.create_post,
        name='create_post'
    ),

    path(
        'like/<int:post_id>/',
        views.like_post,
        name='like_post'
    ),

    path(
        'comment/<int:post_id>/',
        views.add_comment,
        name='add_comment'
    ),

    # New route: Links directly to a specific photo, video, or post layout
    path(
        'post/<int:post_id>/', 
        views.post_detail, 
        name='post_detail'
    ),

    path(
        'follow/<int:user_id>/',
        follow_user,
        name='follow_user'
    ),
    
    path('notifications/', views.notifications_view, name='notifications'),
]