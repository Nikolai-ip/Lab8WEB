from django.urls import path, include, re_path
from . import views

app_name='auto'
urlpatterns=[
    path('',views.index),
    re_path(r'^liked/$',views.like_unlike_post),
    re_path(r'^likedShow/$', views.likeShow),
    # re_path(r'^CheckerDocker/$', views.CheckerDocker, name='CheckerDocker'),
    # re_path(r'^Cat/$', views.Cat, name='Cat'),
]