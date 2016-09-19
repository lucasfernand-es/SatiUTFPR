from django.conf.urls import url
from sati.ViewController import user_session_controller as session, session_controller
from sati.ViewController import event_controller, session_controller

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),

    url(r'^signup/', views.signup, name='signup'),
    url(r'^user_login/', session.user_login, name='user_login'),
    url(r'^user_signup/', session.user_signup, name='user_signup'),

    # methods to update list of participants
    url(r'^get_sessions_user/$', session.get_user_participant, name='user-participant'),
    url(r'^update_participant/$', session.user_update_participant, name='update-participant'),



    # Events
    url(r'^events', views.events_list, name='event-list'),
    # url(r'^events/card_detail', views.event_card_detail, name='event-card-detail'),

    url(r'^event/(?P<event_id>[0-9]+)/$', views.event_detail, name='event-detail'),

    # url(r'^event/all/$', get_public_events, name='event-public-list'),

    # url(r'^event/(?P<event_id>[0-9]+)/spots_event/$', session_controller.get_events_spots,
    #   name='event-spots'),

    # url(r'^event/(?P<event_id>[0-9]+)/(?P<session_id>[0-9]+)/spots_session/$', session_controller.get_session_spots,
    #    name='session-spots'),

    url(r'^event/(?P<event_id>[0-9]+)/spots_event_available/$',
        session_controller.get_events_spots_available,
        name='event-spots-available'),

    url(r'^session/(?P<session_id>[0-9]+)/spots_session_available/$',
        session_controller.get_session_available_spots,
        name='session-spots-available'),

    # Get event spots
    url(r'^event/(?P<event_id>[0-9]+)/spots_event/$', session_controller.get_events_spots,
        name='event-spots'),
    url(r'^event/(?P<event_id>[0-9]+)/spots_event_available/$', session_controller.get_events_spots_available,
        name='event-spots-available'),

    # Get session spots
    url(r'^event/(?P<event_id>[0-9]+)/(?P<session_id>[0-9]+)/spots_session/$', session_controller.get_session_spots,
        name='session-spots'),
    url(r'^event/(?P<event_id>[0-9]+)/(?P<session_id>[0-9]+)/spots_session_available/$',
        session_controller.get_session_available_spots, name='session-spots-available'),

    # Get event by id and all events

    url(r'^event/(?P<event_id>[0-9]+)/get_event/$', event_controller.get_event_by_id,
        name='events'),
    url(r'^event/get_all_events/$', event_controller.get_all_events,
        name='events'),

    # Get all sessions
    url(r'^session/get_all/$', session_controller.get_all_sessions,
        name='sessions-list'),
]
