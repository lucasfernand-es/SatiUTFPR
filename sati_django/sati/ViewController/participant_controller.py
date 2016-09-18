from sati.models import Person, Session, Participant, Event
from django.http import JsonResponse, HttpResponse


def get_event_info(event_id):
    events = Event.objects.all()

    if not len(events):
        return {}
    else:
        event = events[0]
        sessions = Session.objects.filter(event_id=event.id, is_active=True)
        session_array = []

        available_spots_event = 0

        event_has_session = False
        event_has_occurrence = False

        for session in sessions:
            event_has_session = True
            occurrences = Occurrence.objects.filter(session_id=session.id, is_active=True)
            occurrences_array = []
            for occurrence in occurrences:
                event_has_occurrence = True

                occurrences_json = {
                    'room_name': occurrence.room.name,
                    'begin_date_time': occurrence.begin_date_time,
                    'end_date_time': occurrence.end_date_time,
                }
                occurrences_array.append(occurrences_json)

            available_spots_session = session_available_spots(session.id)
            available_spots_event += available_spots_session
            session_json = {
                'instructor_name': session.instructor.name,
                'spots': session.spots,
                'occurrences': occurrences_array,
                'available_spots': available_spots_session,
                'has_spots': available_spots_session > 0,
            }
            # print session_json
            session_array.append(session_json)

        category = Category.objects.get(pk=event.category_id)

        event_category = {'name': category.name, 'image': category.image.url}

        event_json = {
            'id': event.id,
            'category': event_category,
            'edition': event.edition.name,
            'name': event.name,
            'fee': event.fee,
            'workload': event.workload,
            'description': event.description,
            'available_spots': available_spots_event,
            'has_spots': available_spots_event > 0,
            'has_session': event_has_session,
            'has_occurrence': event_has_occurrence,
            'sessions': session_array,
        }

        return event_json

# def get_all_participants(request):
#     persons = Person.objects.all()
#
#     if persons:
#         persons_array = []
#         for person in persons:
#             participate = Participant.objects.filter(person_id=person.id)
#             if not len(participate):
#                 continue
#             sessions_array = []
#             for registry in participate:
#                 session = Session.objects.filter(id=registry.session.id)
#                 sessions_array.append(create_session_json(session))
#             participate_json ={
#                 'sessions': sessions_array
#             }
#
# def create_session_json(session):
#     return {
#         'event_id' : session.event_id
#     }
#
# def create_person_dict(person):
#     return {
#         'cpf': person.cpf,
#         'name': person.name,
#         'academic_registry': person.academic_registry
#     }
#
#
# def create_json_response(response_key, response_dict, error, error_messages):
#     return {
#         response_key : response_dict,
#         'error': error,
#         'error_messages': error_messages
#     }


def session_available_spots(session_id):
    participants = Participant.objects.filter(is_confirmed=True, session_id=session_id)
    session = Session.objects.get(id=session_id)

    response = 0

    if session:
        available_spots_session = session.spots - len(participants)
        if available_spots_session > 0:
            response = available_spots_session

    return response


def event_available_spots(event_id):
    sessions = Session.objects.filter(event_id=event_id)

    response = 0

    if sessions:
        available_spots_event = 0
        for session in sessions:
            available_spots_event += session_available_spots(session.id)

        if event_available_spots > 0:
            response = available_spots_event

    return response

