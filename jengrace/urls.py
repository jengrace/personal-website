from django.conf.urls import include, url
from django.contrib import admin
import mainpage.views as v

admin.autodiscover()

urlpatterns = [
    url(r'^blog/$', v.blog),
    url(r'^reset/$', v.reset),
    url(r'^comments/$', v.comments),
    url(r'^home/$', v.homepage),
    url(r'^$', v.homepage),
]
