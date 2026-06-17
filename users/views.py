from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post, Follow
from .models import Profile

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
            
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('/feed/')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/feed/')
        messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def profile_view(request, user_id):
    user_profile = get_object_or_404(User.objects.prefetch_related('profile'), id=user_id)
    posts = Post.objects.filter(user=user_profile).select_related('user__profile').order_by('-created_at')

    followers_count = Follow.objects.filter(following=user_profile).count()
    following_count = Follow.objects.filter(follower=user_profile).count()

    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(follower=request.user, following=user_profile).exists()

    return render(request, 'profile.html', {
        'user_profile': user_profile,
        'posts': posts,
        'followers_count': followers_count,
        'following_count': following_count,
        'is_following': is_following
    })

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.bio = request.POST.get('bio', profile.bio)
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        if 'cover_photo' in request.FILES:
            profile.cover_photo = request.FILES['cover_photo']
        profile.save()
        return redirect(f'/profile/{request.user.id}/')
    return render(request, 'profile_edit.html', {'profile': profile})

def followers_list_view(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    relations = Follow.objects.filter(following=user_profile).select_related('follower__profile')
    
    # Correctly defining the connections variable
    connections = [rel.follower.profile for rel in relations]
    
    return render(request, 'follow_list.html', {
        'user_profile': user_profile,
        'connections': connections,
        'is_following_page': False
    })

def following_list_view(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    relations = Follow.objects.filter(follower=user_profile).select_related('following__profile')
    
    # Correctly defining the connections variable
    connections = [rel.following.profile for rel in relations]
    
    return render(request, 'follow_list.html', {
        'user_profile': user_profile,
        'connections': connections,
        'is_following_page': True
    })