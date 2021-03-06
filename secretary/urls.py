"""secretary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.views.static import serve
from . import view
from . import settings

urlpatterns = [
    url(r'^$', view.SignIn),
    url(r'^user-api/report/register$', view.Register),
    url(r'^user-api/report$', view.SignIn),
    url(r'^user-api/report/index$', view.Index),
    url(r'^user-api/report/home$', view.Home),
    url(r'^user-api/report/add$', view.AddReport),
    url(r'^user-api/report/view$', view.ViewReport),
    url(r'^user-api/report/edit$', view.EditReport),
]
