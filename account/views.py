from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from account.models import User
import time
import pdb

# Create your views here.
class UserFormLogin(forms.Form):
 username = forms.CharField(label='用户名',max_length=100)
 pw = forms.CharField(label='密码',max_length=16)

class UserForm(forms.Form):
 username = forms.CharField(label='用户名',max_length=100)
 password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
 password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())
 email = forms.EmailField(label='电子邮件')

def login(request):
    if request.method == 'POST':
        uf = UserFormLogin(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['pw']
            userResult = User.objects.filter(name = username,password=password)
            if(len(userResult)>0):
                request.session['UID'] = username
                request.session['status']= True
                return render_to_response('success.html',{'operatiorn':'Login'})
            else:
                return HttpResponse("wrong password")
        else:
            return HttpResponse("invalid user")
    else:
        uf = UserFormLogin()
        return render_to_response('Userlogin.html',{'uf':uf})

def register(request):
    curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    if request.method=='POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            user = uf.cleaned_data['username']
            filterResult = User.objects.filter(name = user)
            if len(filterResult)>0:
                return render_to_response('register.html',{"errors":"user has already existed"})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                errors = []
                if (password1!=password2) :
                    errors.append("different password!")
                    return render_to_response('register.html',{'errors':errors})
                else:
                    password = password1
                    email = uf.cleaned_data['email']
                    user = User.objects.create(name=user,password=password)
                    user.save()
                    return render_to_response('success.html',{'username':user,'operation':"rigester"})

    else:
        uf=UserForm()
    return render_to_response('register.html',{'uf':uf})