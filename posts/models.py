from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    content = models.TextField()
    
    image = models.ImageField(
        upload_to='posts/images/',
        blank=True,
        null=True
    )

    # Added native video streaming upload capability
    video = models.FileField(
        upload_to='posts/videos/',
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.text[:20]


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"


class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User,
        related_name='followers',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.follower} follows {self.following}"


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.user.username} | From: {self.sender.username} | Type: {self.notification_type}"