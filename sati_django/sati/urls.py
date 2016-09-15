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

    # Category
    url(r'^api/category/$', CategoryList.as_view(), name='category-list'),
    url(r'^api/category/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category-detail'),

    # Event
    url(r'^api/event/$', EventList.as_view(), name='event-list'),
    url(r'^api/event/(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),

    # Person
    url(r'^api/person/$', PersonList.as_view(), name='person-list'),
    url(r'^api/person/(?P<pk>\d+)/$', PersonDetail.as_view(), name='person-detail'),
    url(r'^api/public_person/(?P<pk>\d+)/$', PersonDetailPublic.as_view(), name='person-detail-public'),

    # Session
    url(r'^api/session/$', SessionList.as_view(), name='session-list'),
    url(r'^api/session/(?P<pk>\d+)/$', SessionDetail.as_view(), name='session-detail'),

    # Room
    url(r'^api/room/$', RoomList.as_view(), name='room-list'),
    url(r'^api/room/(?P<pk>\d+)/$', RoomDetail.as_view(), name='room-detail'),

    # Session
    url(r'^api/occurrence/$', OccurrenceList.as_view(), name='occurrence-list'),
    url(r'^api/occurrence/(?P<pk>\d+)/$', OccurrenceDetail.as_view(), name='occurrence-detail'),

]
