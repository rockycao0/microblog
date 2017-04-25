from django.db import models
from account.models import User
# Create your models here.

class Content(models.Model):
    text = models.CharField(max_length=140)
    date = models.DateField(auto_now_add=True)
    up_num = models.IntegerField(default=0)
    UID = models.ForeignKey('account.User',on_delete=models.CASCADE,related_name='owner')
    UP = models.ManyToManyField('account.User',related_name='con_up')
    def __str__(self):
        return self.text

class  Comment(models.Model):
    UID = models.ForeignKey('account.User',on_delete=models.CASCADE)
    text = models.CharField(max_length= 100)
    date = models.DateField(auto_now_add=True)
    up_num = models.IntegerField(default=0)
    CID = models.ForeignKey('Content',on_delete=models.CASCADE,related_name='owner')
    UP = models.ManyToManyField('account.User',related_name='com_up')
    def __str__(self):
        return self.text


