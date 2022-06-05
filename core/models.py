from django.db import models
from django.utils import timezone

# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', blank=True,null=True)
    caption=models.TextField()
    created_date=(models.DateTimeField(default=timezone.now))

    def __str__(self):
        return self.caption


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