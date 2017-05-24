from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from account.models import User
from .models import Content, Comment
# Create your views here.


class blog(forms.Form):
    text = forms.CharField(label='正文',max_length=139, widget=forms.Textarea(attrs={'style': 'height: 200px;width:800px'}))
class comm(forms.Form):
    text = forms.CharField(label='正文',max_length=100, widget=forms.Textarea(attrs={'style': 'height: 50px;width:800px'}))


def main(request):
    try :
        name=request.session.get('UID')
        user = User.objects.get(name=name)
        mod = 'user'
    except:
        mod = 'passenger'

    request.session['frompage']='/main/'
    if(mod == 'user'):
        if request.method == "POST":
            cont = blog(request.POST)
            if cont.is_valid():
                text = cont.cleaned_data["text"]
                Content.objects.create(text=text, UID=user)
                return HttpResponseRedirect("/main/")
            else:
                return HttpResponse("<p>invalid input</p>")
        else:
            cont = blog()
        star =user.follow.all()
        star = star | User.objects.filter(name=name)
        content_list=User.objects.none()
        for x in star:
            content_list = content_list | x.owner.all()

        content_list = content_list.distinct()
        return render_to_response('blog.html',
                                  {'user': user, 'content_list': content_list.order_by('-id'), 'comm': cont})
    else:
        return HttpResponseRedirect("/hot/")

def hot(request):
    content_list = Content.objects.all()
    content_list=content_list.order_by('-up_num')
    request.session['frompage'] = '/hot/'
    try:
        name=request.session.get('UID')
        user = User.objects.get(name=name)
        return render_to_response('hot.html', {'user': user, 'content_list': content_list})
    except:
        return render_to_response('hot.html', {'content_list': content_list})


def up(request,CID):
    try:
        name = request.session.get('UID')
    except:
        return HttpResponseRedirect("Userlogin.html")
    user = User.objects.get(name=name)
    content =  Content.objects.get(id= CID)
    if content.UID!=user:
        content.UP.add(user)
    return HttpResponseRedirect(request.session['frompage'])


def follow(request,favor):
    try:
        name = request.session.get('UID')
    except:
        HttpResponseRedirect("login.html")
    user = User.objects.get(name=name)
    target = User.objects.get(name = favor)
    user.follow.add(target)
    target.follower.add(user)
    return HttpResponseRedirect(request.session['frompage'])


def unfollow(request,favor):
    try:
        name = request.session.get('UID')
    except:
        HttpResponseRedirect("login.html")
    user = User.objects.get(name=name)
    target = User.objects.get(name = favor)
    user.follow.remove(target)
    target.follower.remove(user)
    return HttpResponseRedirect(request.session['frompage'])


def comment(request,CID):
    try:
        name = request.session.get('UID')
        user = User.objects.get(name=name)
    except:
        HttpResponseRedirect("/login/")
    content = Content.objects.get(id=CID)
    request.session['frompage'] = ('/main/%s/comment/' % CID)
    if request.method == "POST":
        com = comm(request.POST)
        if com.is_valid():
            user = User.objects.get(name=name)
            text = com.cleaned_data["text"]
            Comment.objects.create(text=text, UID=user, CID=content)
            com = comm()
            return render_to_response("article.html", {'comm': com, 'content': content, 'user': user})
        else:
            return HttpResponse("<p>invalid input</p>")
    else:
        com = comm()
        return render_to_response("article.html", {'comm': com, 'content': content, 'user': user})


def home(request,uid):
    try:
        name = request.session.get('UID')
        user = User.objects.get(name=name)
    except:
        user = User.objects.none()
    request.session['frompage'] = ('/%s/home/' % uid)
    host = User.objects.get(id=uid)
    content_list = host.owner.all()
    return render_to_response('home.html', {'user': user, 'host': host, 'content_list': content_list.order_by('-id')})


def delete(request, CID):
    try:
        name = request.session.get('UID')
    except:
        HttpResponseRedirect("login.html")
    content = Content.objects.get(id=CID)
    user = User.objects.get(name=name)
    if user==content.UID:
        content.delete()
    return HttpResponseRedirect(request.session['frompage'])


def search(request):
    type = 'search'
    text = request.GET['text']
    content_list=[]
    try:
        name = request.session.get('UID')
        user = User.objects.get(name=name)
    except:
        user = User.objects.none

    for content in Content.objects.all():
        if (content.text.find(text) or (content.UID.name == text))>= 0 :
            content_list.append(content)

    return render_to_response('blog.html', {'content_list': content_list, 'user': user, 'type': type, 'text':text})

def page_not_found (request):
    return render(request, "404.html")