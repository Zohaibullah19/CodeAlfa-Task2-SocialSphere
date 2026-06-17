# posts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import (
    Post,
    Like,
    Comment,
    Notification,
    Follow
)


@login_required(login_url='login')
def feed(request):

    posts = Post.objects.all().order_by('-created_at')

    unread_notifications_count = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).count()

    return render(
        request,
        'feed.html',
        {
            'posts': posts,
            'unread_notifications_count': unread_notifications_count
        }
    )


@login_required(login_url='login')
def create_post(request):

    if request.method == 'POST':

        content = request.POST.get('content')
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        Post.objects.create(
            user=request.user,
            content=content,
            image=image,
            video=video
        )

        return redirect('feed')

    return render(
        request,
        'create_post.html'
    )


@login_required(login_url='login')
def like_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    like = Like.objects.filter(
        user=request.user,
        post=post
    ).first()

    liked = False

    if like:

        like.delete()

    else:

        Like.objects.create(
            user=request.user,
            post=post
        )

        liked = True

        if post.user != request.user:

            Notification.objects.create(
                user=post.user,
                sender=request.user,
                notification_type='like',
                post=post
            )

    return JsonResponse({
        'likes': post.like_set.count(),
        'liked': liked
    })


@login_required(login_url='login')
def add_comment(request, post_id):

    if request.method == 'POST':

        post = get_object_or_404(
            Post,
            id=post_id
        )

        text = request.POST.get('comment')

        Comment.objects.create(
            post=post,
            user=request.user,
            text=text
        )

        if post.user != request.user:

            Notification.objects.create(
                user=post.user,
                sender=request.user,
                notification_type='comment',
                post=post
            )




@login_required(login_url='login')
def notifications_view(request):

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    notifications.filter(
        is_read=False
    ).update(
        is_read=True
    )

    return render(
        request,
        'notifications.html',
        {
            'notifications': notifications
        }
    )


@login_required(login_url='login')
def post_detail(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    unread_notifications_count = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).count()

    return render(
        request,
        'post_detail.html',
        {
            'post': post,
            'unread_notifications_count': unread_notifications_count
        }
    )


@login_required(login_url='login')
def follow_user(request, user_id):

    target_user = get_object_or_404(
        User,
        id=user_id
    )

    if target_user != request.user:

        follow_relation = Follow.objects.filter(
            follower=request.user,
            following=target_user
        ).first()

        if follow_relation:

            follow_relation.delete()

        else:

            Follow.objects.create(
                follower=request.user,
                following=target_user
            )

            Notification.objects.create(
                user=target_user,
                sender=request.user,
                notification_type='follow'
            )

    return redirect(
        f'/profile/{user_id}/'
    )