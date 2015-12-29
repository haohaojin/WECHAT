from django.conf.urls import patterns, include, url
from WECHAT.views import WeixinInterfaceView
from django.views.decorators.csrf import csrf_exempt    #remove csrf
urlpatterns = patterns('',
    url(r'^$', csrf_exempt(WeixinInterfaceView.as_view())),
)