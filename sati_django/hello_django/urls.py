from django.conf.urls import include, url
from django.contrib import admin
from sati_django.sati import views

urlpatterns = [
                       # Examples:
                       # url(r'^$', 'hello_django.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       # New apps
                       url(r'^control_panel/', include('control_panel.urls')),

                       url(r'^$', views.index , name='home'),
                       # url(r'^login', 'sati.views.login', name='login'),
                       # url(r'test', 'sati.views.test', name='test'),
                       # url(r'^newLogin', 'sati.views.newLogin', name='newLogin'),
                       # url(r'^signup', 'sati.views.signup', name='signup'),
                       # url(r'^registry_person', 'sati.views.registry_person', name='registry_person')
]
