"""mobiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import  settings
from mobile_app.views import base,xiaomi,apple,samsung,oneplus,poco,oppo,iqoo,realme,login,signup,logout_user,contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login),
    # path("contact/",contact,name="contact"),
    path("base", base, name="base"),
    path("xiaomi/", xiaomi, name="xiaomi"),
    path("apple/", apple, name="apple"),
    path("samsung/", samsung, name="samsung"),
    path("oneplus/",oneplus, name="oneplus"),
    path("poco/", poco, name="poco"),
    path("oppo/", oppo, name="oppo"),
    path("iqoo/",iqoo, name="iqoo"),
    path("realme/", realme, name="realme"),

    path("signup/",signup,name="signup"),
    path("logout/",logout_user,name="logout"),
    
]
