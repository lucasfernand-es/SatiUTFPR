from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edition/', views.edition, name='edition'),
    # url(r'^'),
]