from django.conf.urls import url
from . import views

urlpatterns = [
    # 定义url，移动端通过这个url访问服务端
    url(r'^users/$', views.user_api),
    # username就是之前views中another_user_api方法中的参数
    url(r'^users/(?P<username>[A-Za-z0-9]+)/$', views.another_user_api),
    # 安卓端用api
    url(r'^android_user/$', views.android_user_api)
]