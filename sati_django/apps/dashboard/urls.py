from django.conf.urls import url
from sati import session

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edition/', views.edition, name='edition'),
    url(r'^logout/', session.user_logout, name='logout'),
]