from django.conf.urls import url
from sati_system import session
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^user_login', session.user_login, name='user_login'),
    url(r'^user_signup', session.user_signup, name='user_signup')
]
