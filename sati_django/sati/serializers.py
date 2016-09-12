from sati.models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class OccurrenceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    begin_date_time = serializers.DateTimeField()
    end_date_time = serializers.DateTimeField()
    session = serializers.PrimaryKeyRelatedField(queryset=Session.objects.all())
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    is_active = serializers.BooleanField()

    class Meta:
        model = Occurrence
        fields = ('id', 'begin_date_time', 'end_date_time', 'session', 'room', 'is_active')

    def create(self, validated_data):
        return Occurrence.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.begin_date_time = validated_data.get('begin_date_time', instance.begin_date_time)
        instance.end_date_time = validated_data.get('end_date_time', instance.end_date_time)
        instance.session = validated_data.get('session', instance.session)
        instance.room = validated_data.get('session', instance.room)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    instructor = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    is_active = serializers.BooleanField()

    # Foreign
    occurrences = OccurrenceSerializer(many=True, read_only=True)
    # occurrences = serializers.StringRelatedField(many=True, read_only=True)
    # occurrences = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='occurrence-detail')

    class Meta:
        model = Session
        fields = ('id', 'event', 'instructor', 'is_active', 'occurrences')

    def create(self, validated_data):
        return Session.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.event = validated_data.get('event', instance.event)
        instance.instructor = validated_data.get('instructor', instance.instructor)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance


class EventSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    edition = serializers.PrimaryKeyRelatedField(queryset=Edition.objects.all())
    name = serializers.CharField()
    type = serializers.CharField()
    fee = serializers.FloatField()
    workload = serializers.IntegerField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    # Foreign
    sessions = SessionSerializer(many=True, read_only=True)
    # sessions = serializers.StringRelatedField(many=True, read_only=True)
    # sessions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='session-detail')

    class Meta:
        model = Event
        ordering = ['name']
        fields = ('id', 'edition', 'name', 'type', 'fee', 'workload', 'description', 'is_active', 'sessions')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.edition = validated_data.get('edition', instance.edition)
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.fee = validated_data.get('fee', instance.fee)
        instance.workload = validated_data.get('workload', instance.workload)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.save()

        return instance


class EditionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    begin_date = serializers.DateField()
    end_date = serializers.DateField()
    is_active = serializers.BooleanField()
    theme = serializers.CharField()
    description = serializers.CharField()
    # Foreign
    events = EventSerializer(many=True, read_only=True)
    # events = serializers.StringRelatedField(read_only=True)
    # events = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='event-detail')

    class Meta:
        model = Edition
        ordering = ['begin_date']
        fields = ('id', 'name', 'begin_date', 'end_date', 'is_active', 'theme', 'description', 'events')

    def create(self, validated_data):
        return Edition.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.begin_date = validated_data.get('begin_date', instance.begin_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.theme = validated_data.get('theme', instance.theme)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    name = serializers.CharField()
    email = serializers.CharField()
    # password = serializers.CharField(style={'input_type': 'password'})
    institution = serializers.CharField()
    cpf = serializers.CharField()
    academic_registry = serializers.CharField()
    role = serializers.CharField()
    is_active = serializers.BooleanField()

    # Foreign
    sessions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='session-detail')

    class Meta:
        model = Person
        ordering = ['name']
        fields = ('id', 'name', 'email', 'institution',
                  'cpf', 'academic_registry', 'role', 'is_active', 'sessions')  # 'password',

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.institution = validated_data.get('institution', instance.institution)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.academic_registry = validated_data.get('academic_registry', instance.cpf)
        instance.role = validated_data.get('role', instance.role)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    occupancy = serializers.IntegerField()
    number = serializers.IntegerField()
    type = serializers.CharField()
    is_active = serializers.BooleanField()

    # Foreign
    occurrences = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='occurrence-detail')

    class Meta:
        model = Room
        fields = ('id', 'name', 'occupancy', 'number', 'type', 'is_active', 'occurrences')

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.occupancy = validated_data.get('occupancy', instance.occupancy)
        instance.number = validated_data.get('number', instance.number)
        instance.type = validated_data.get('type', instance.type)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance

