from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='nt.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', blank=True,null=True)
    caption=models.TextField()
    created_date=(models.DateTimeField(default=timezone.now))

    def __str__(self):
        return self.caption
        
class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
# class Comment(models.Model):
#     content = models.TextField()
#     image = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


#     def __str__(self) -> str:
#         return f"{self.content}"


# class Like(models.Model):
#     image = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


#     def __str__(self) -> str:
#         return f"{self.user.username} Likes"


# #Create followers and follow
# class Follow(models.Model):
#     account_following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', null=True)
#     follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', null=True)

#     def __str__(self) -> str:
#         return f"{self.follower}"        