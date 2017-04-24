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
        mod = 'user'
    except:
        mod = 'passenger'
    if(mod=='user'):
        user = User.objects.get(name=name)
        star =user.follow.all()
        star = star | User.objects.filter(name=name)
        content_list=[]
        for x in star:
            content_list.append(x.owner.all())
    else:
        content = Content.objects.order_by()[:10]

    return render_to_response('main.html',{'user':name,'content_list':content_list})

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
            return HttpResponseRedirect("main.html")
        else:
            return HttpResponse("<p>invalid input</p>")
    else:
        cont = blog()
        return render_to_response("publish.html",{'comm':cont})

