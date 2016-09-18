from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sati_django.apps.dashboard import views as dashboardviews

urlpatterns = [
                # Examples:
                # url(r'^$', 'hello_django.views.home', name='home'),
                # url(r'^blog/', include('blog.urls')),

                url(r'^admin/', include(admin.site.urls)),

                # Dashboard
                url(r'^dashboard/', include('apps.dashboard.urls'), name='dashboard'),

                # public
                url(r'^', include('apps.public.urls')),

                # CRUD
                url(r'^', include('sati.urls')),



                # url(r'^$', views.index, name='home'),
                # url(r'^login', views.login, name='login'),
                # url(r'test', 'sati.views.test', name='test'),
                # url(r'^newLogin', 'sati.views.newLogin', name='newLogin'),
                # url(r'^signup', 'sati.views.signup', name='signup'),
                # url(r'^registry_person', 'sati.views.registry_person', name='registry_person')
] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

