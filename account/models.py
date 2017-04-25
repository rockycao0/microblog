from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    followed_user = models.ManyToManyField('User',related_name='follow',default="")
    follower_user = models.ManyToManyField('User',related_name='follower',default="")

    def __str__(self):
        return self.name
