from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Follow


def follow_user(request, user_id):

    user_to_follow = User.objects.get(
        id=user_id
    )

    follow = Follow.objects.filter(
        follower=request.user,
        following=user_to_follow
    ).first()

    if follow:
        follow.delete()

    else:
        Follow.objects.create(
            follower=request.user,
            following=user_to_follow
        )

    return redirect(
        f'/profile/{user_id}/'
    )