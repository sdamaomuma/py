"""Backstage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from doshow import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bxslider/',views.bxslider),
    path('home/',views.home),
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout),
    path('modify/',views.modify),
    path('one_one/',views.one_one),
    path('three_one/',views.three_one),
]
# 部分views的get需要跳转到login
# 订单管理在页面里有查询限制，由于数据量不大，所以用了js分页
# 如果使用django分页，前端的页面标签要在后端生成，而且如果使用ajax发送页码和更新数据会比较麻烦。每次接收到换页的请求都要从数据库里取全部数据，然后返回给前端该页的部分数据