"""rbs_app URL Configuration
** do not add new pages here - go to the urls.py in rbs_application
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rbs_application import views


urlpatterns = [
    # url(r'^$', include('rbs_application.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    # admin username: rbs
    # admin password: rbs_pass
]
