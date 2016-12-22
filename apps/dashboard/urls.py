from django.conf.urls import url
from sati.ViewController import user_session_controller as session, event_controller, participant_controller

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edition/', views.edition, name='edition'),
    url(r'^participant/', views.participant, name='participant'),
    url(r'^event/', views.event, name='event'),
    url(r'^logout/', session.user_logout, name='logout'),
    url(r'^create_event/', event_controller.create_event, name='create_event' ),
    url(r'^get_all_participants/', participant_controller.get_all_participants, name='get-events-n-participants'),
    url(r'^confirm_participant/', participant_controller.confirm_participant, name='confirm-participant')
]