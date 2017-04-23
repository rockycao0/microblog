from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    email = models.EmailField(default='123@123.com')
    followed_user = models.ForeignKey('User',on_delete=models.CASCADE,related_name='follower',null=True)
    follower_user = models.ForeignKey('User',on_delete=models.CASCADE,related_name='follow',null=True)

    def __str__(self):
        return self.name
