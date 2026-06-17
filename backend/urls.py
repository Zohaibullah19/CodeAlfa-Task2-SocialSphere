# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView  # Added for root path redirection

urlpatterns = [
    # Root Redirect: Bounces http://127.0.0.1:8000/ directly to /feed/
    path('', RedirectView.as_view(url='feed/', permanent=True)),

    # Main Django Administrative Gateway
    path('admin/', admin.site.urls),

    # Authentication & User Management Pipeline (login, register, profile, edit-profile)
    path('', include('users.urls')),

    # Core Timeline Feed, Content Posting, and Interactions (likes, comments)
    path('', include('posts.urls')),
]

# Server Media Asset Pipelines (Enabled under Development Flags)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )