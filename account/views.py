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
 username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': "用户名"}))
 pw = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "密码"}))


class UserForm(forms.Form):
 username = forms.CharField(label='用户名', max_length=100, widget=forms.TextInput(attrs={'class':"form-control", 'placeholder': "用户名"}))
 password1 = forms.CharField(label='密码', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "密码"}))
 password2 = forms.CharField(label='确认密码', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "确认密码"}))


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
                return HttpResponseRedirect('/main/')
            else:
                return HttpResponse("wrong password")
        else:

            return HttpResponse("invalid user")
    else:
        try:
            del request.session['UID']
            request.session['status'] = False
        except:
            request.session['status'] = False
        uf = UserFormLogin()
        return render_to_response('login.html',{'uf':uf})

def register(request):
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
                    user = User.objects.create(name=user,password=password)
                    user.save()
                    return HttpResponseRedirect('/login/')

    else:
        uf=UserForm()
    return render_to_response('register.html',{'uf':uf})