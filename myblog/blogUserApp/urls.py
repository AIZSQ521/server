# coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url(r'^rescUserMsg/$',views.recvUserMsgs,name='rescUserMsg'),
    url(r'^pwd_reset/$',views.pwd_reset,name="pwd_reset"),
    url(r'^recv_reset_pwd/$',views.recv_reset_pwd,name='recv_reset_pwd'),
]