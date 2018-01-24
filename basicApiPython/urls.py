from django.conf.urls import include, url
from django.contrib import admin
from albumes import views
from songs import views as views1

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^songs/$', views1.get_songs, name="get_songs"),
    url(r'^songs/(?P<pk>[0-9]+)/$', views1.song, name="song"),
    url(r'^albumes/$', views.get_albumes, name="get_albumes"),
    url(r'^albumes/(?P<pk>[0-9]+)/$', views.remove_album, name="remove_album"),
]
