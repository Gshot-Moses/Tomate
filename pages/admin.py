# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserInfo, Post, Comment, Like, Adress, Chat


admin.site.register(UserInfo)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Adress)
admin.site.register(Chat)
