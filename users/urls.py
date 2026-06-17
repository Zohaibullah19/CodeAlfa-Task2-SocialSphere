# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Auth routing paths
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile & Management Subsystems
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    
    # Clickable Stats List Routes (Names matching template tags)
    path('profile/<int:user_id>/followers/', views.followers_list_view, name='followers_list'),
    path('profile/<int:user_id>/following/', views.following_list_view, name='following_list'),
]