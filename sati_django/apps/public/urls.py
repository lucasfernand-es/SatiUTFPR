from django.conf.urls import url
from sati.ViewController import user_session_controller as session, session_controller

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^user_login', session.user_login, name='user_login'),
    url(r'^user_signup', session.user_signup, name='user_signup'),

    # Events
    url(r'^events', views.events_list, name='event-list'),
    # url(r'^events/card_detail', views.event_card_detail, name='event-card-detail'),

    url(r'^event/(?P<event_id>[0-9]+)/$', views.event_detail, name='event-detail'),
    url(r'^event/(?P<event_id>[0-9]+)/spots_event/$', session_controller.get_events_spots , name='event-spots'),
    url(r'^event/(?P<event_id>[0-9]+)/(?P<session_id>[0-9]+)/spots_session/$', session_controller.get_session_spots, name='session-spots'),
    url(r'^event/(?P<event_id>[0-9]+)/(?P<session_id>[0-9]+)/spots_session_available/$',
        session_controller.get_session_available_spots, name='session-spots-available')

]
