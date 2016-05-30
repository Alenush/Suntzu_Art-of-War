from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book$', views.all_book, name='book'),
    url(r'^chapter/(?P<chapter>[0-9]+)/$', views.chapter, name='mychapter')
]