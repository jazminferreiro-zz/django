from django.conf.urls import url

from . import views

#url(regex para matchear con la url, view que va a llamr, nombre)

urlpatterns = [
    url(r'^$', views.index, name='index'),
]