from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from account.models import User
from .models import Content, Comment
# Create your views here.


class blog(forms.Form):
    text = forms.CharField(label='正文',max_length=140)


class comment(forms.Form):
    text = forms.CharField(label='评论',max_length=100)


def main(request):
    try :
        name=request.session.get('UID')
        user = User.objects.get(name=name)
        mod = 'user'
    except:
        mod = 'passenger'
    if(mod == 'user'):
        star =user.follow.all()
        star = star | User.objects.filter(name=name)
        content_list=User.objects.none()
        for x in star:
            content_list = content_list | x.owner.all()
        if len(content_list)<10:
            t = 10-len(content_list)
            content_list = content_list | Content.objects.order_by()[:t]
            print(content_list)
        content_list = content_list.distinct()
    else:
        content_list = Content.objects.order_by()[:10]

    #return render_to_response('main.html', {'user' : user, 'content_list' : content_list.order_by('-id')})
    return render_to_response('blog.html', {'user': user, 'content_list': content_list.order_by('-id')})


def publish(request):
    try:
        name = request.session.get('UID')
    except:
        return HttpResponseRedirect("Userlogin.html")
    if request.method == "POST":
        cont = blog(request.POST)
        if cont.is_valid():
            user = User.objects.get(name = name)
            text = cont.cleaned_data["text"]
            Content.objects.create(text=text,UID = user)
            return HttpResponseRedirect("/main/")
        else:
            return HttpResponse("<p>invalid input</p>")
    else:
        cont = blog()
        return render_to_response("publish.html",{'comm':cont})


def up(request,CID):
    try:
        name = request.session.get('UID')
    except:
        return HttpResponseRedirect("Userlogin.html")
    user = User.objects.get(name=name)
    content =  Content.objects.get(id= CID)
    content.UP.add(user)
    return HttpResponse("well done")

def follow(request,favor):
    try:
        name = request.session.get('UID')
    except:
        HttpResponseRedirect("Userlogin.html")
    user = User.objects.get(name=name)
    target = User.objects.get(name = favor)
    user.follow.add(target)
    target.follower.add(user)
    return HttpResponse("well done")

def comment(request,CID):
    try:
        name = request.session.get('UID')
    except:
        HttpResponseRedirect("Userlogin.html")
    content = Content.objects.get(id = CID)
    if request.method == "POST":
        com = blog(request.POST)
        if com.is_valid():
            user = User.objects.get(name = name)
            text = com.cleaned_data["text"]
            Comment.objects.create(text=text,UID = user,CID = content)
            return HttpResponseRedirect("/main/")
        else:
            return HttpResponse("<p>invalid input</p>")
    else:
        com = blog()
        return render_to_response("publish.html",{'comm':com})
    return HttpResponse("well done")