from django.db import models
from account.models import User
# Create your models here.

class Content(models.Model):
    text = models.CharField(max_length=140)
    date = models.DateField(auto_now_add=True)
    up_num = models.IntegerField(default=0)
    UID = models.ForeignKey('account.User',on_delete=models.CASCADE,related_name='owner')
    UP = models.ForeignKey('account.User',related_name="uop_cer",null=True)
    def __str__(self):
        return self.text

class  Comment(models.Model):
    UID = models.ForeignKey('account.User',on_delete=models.CASCADE)
    text = models.CharField(max_length= 100)
    date = models.DateField(auto_now_add=True)
    up_num = models.IntegerField(default=0)
    CID = models.ForeignKey('Content',on_delete=models.CASCADE,related_name='owner')
    UP = models.ForeignKey('account.User',null=True,on_delete=models.CASCADE,related_name="up_co")
    def __str__(self):
        return self.text


