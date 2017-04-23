from django.contrib import admin

# Register your models here.
from app.models import Content,Comment

admin.site.register(Comment)
admin.site.register(Content)