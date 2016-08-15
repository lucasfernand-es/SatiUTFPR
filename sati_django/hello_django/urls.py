from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
    # url(r'^$', 'hello_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'satiUTFPR.views.index', name='home'),
                       url(r'^login', 'satiUTFPR.views.login', name='login'),
                       url(r'test', 'satiUTFPR.views.test', name='test'),
                       url(r'^newLogin', 'satiUTFPR.views.newLogin', name='newLogin'),
                       )
