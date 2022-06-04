from email.mime import image
from django.db import models
from pytz import timezone

# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True,null=True)
    caption=models.TextField()
    created_date=(models.DateTimeField(default=timezone.now))

    def __str__(self):
        return self.title