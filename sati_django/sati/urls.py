from sati import views
from sati.views import *

from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Edition
    url(r'^api/edition/$', EditionList.as_view(), name='edition-list'),
    url(r'^api/edition/(?P<pk>\d+)/$', EditionDetail.as_view(), name='edition-detail'),

    # Event
    url(r'^api/event/$', EventList.as_view(), name='event-list'),
    url(r'^api/event/(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),

    # Person
    url(r'^api/person/$', PersonList.as_view(), name='person-list'),
    url(r'^api/person/(?P<pk>\d+)/$', PersonDetail.as_view(), name='person-detail'),

    # Session
    url(r'^api/session/$', SessionList.as_view(), name='session-list'),
    url(r'^api/session/(?P<pk>\d+)/$', SessionDetail.as_view(), name='session-detail'),
]
