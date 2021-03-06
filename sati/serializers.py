
# -*- coding: utf-8 -*-
# from aenum import unique
from sati.models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db import Error
import re


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

    def validate(self, data):
        """
        Check if end date is after begin date
        """
        if data['begin_date_time'] > data['end_date_time']:
            raise serializers.ValidationError('Data final precisa ser depois da inicial.')
        return data

    def create(self, validated_data):
        return Occurrence.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.begin_date_time = validated_data.get('begin_date_time', instance.begin_date_time)
        instance.end_date_time = validated_data.get('end_date_time', instance.end_date_time)
        instance.session = validated_data.get('session', instance.session)
        instance.room = validated_data.get('room', instance.room)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    instructor = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    spots = serializers.IntegerField()
    is_active = serializers.BooleanField()

    # Foreign
    occurrences = OccurrenceSerializer(many=True, read_only=True)
    # occurrences = serializers.StringRelatedField(many=True, read_only=True)
    # occurrences = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='occurrence-detail')

    class Meta:
        model = Session
        fields = ('id', 'event', 'instructor', 'is_active', 'spots', 'occurrences')

    def create(self, validated_data):
        return Session.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.event = validated_data.get('event', instance.event)
        instance.instructor = validated_data.get('instructor', instance.instructor)
        instance.spots = validated_data.get('spots', instance.spots)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance


class EventSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    edition = serializers.PrimaryKeyRelatedField(queryset=Edition.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    name = serializers.CharField(validators=[UniqueValidator(queryset=Event.objects.all(), message='Nome já existente')])
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
        fields = ('id', 'edition', 'category', 'name', 'fee', 'workload', 'description', 'is_active', 'sessions')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.edition = validated_data.get('edition', instance.edition)
        instance.category = validated_data.get('category', instance.category)
        instance.name = validated_data.get('name', instance.name)
        instance.fee = validated_data.get('fee', instance.fee)
        instance.workload = validated_data.get('workload', instance.workload)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.save()

        return instance


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    image = serializers.ImageField()

    events = EventSerializer(many=True, read_only=True)

    # Foreign
    # occurrences = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='occurrence-detail')

    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'events')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance


class EditionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[UniqueValidator(queryset=Edition.objects.all(), message='Nome ja existente')])
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
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=100, validators=[UniqueValidator(queryset=Person.objects.all(), message='E-mail já cadastrado')])
    password = serializers.CharField(style={'input_type': 'password'})
    institution = serializers.CharField(allow_blank=True, required=False)
    cpf = serializers.CharField(validators=[UniqueValidator(queryset=Person.objects.all(), message='CPF já cadastrado.')])
    academic_registry = serializers.CharField(allow_null=True, required=False)
    role = serializers.CharField()
    is_active = serializers.BooleanField()

    # Foreign
    #sessions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='session-detail')

    class Meta:
        model = Person
        ordering = ['name']
        fields = ('id', 'name', 'email', 'password', 'institution',
                  'cpf', 'academic_registry', 'role', 'is_active')# 'sessions')  # 'password',

    def validate_cpf(self, value):
        cpf_value = ''.join(re.findall('\d', str(value)))

        if (not cpf_value) or (len(cpf_value) < 11):
            raise serializers.ValidationError('CPF Inválido.')

        inteiros = map(int, cpf_value)
        novo = inteiros[:9]

        while len(novo) < 11:
            r = sum([(len(novo) + 1 - i) * v for i, v in enumerate(novo)]) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            novo.append(f)

        if novo == inteiros:
            return cpf_value
        else:
            raise serializers.ValidationError('CPF Invalido.')

    def create(self, validated_data):
        password = validated_data.get('password')
        username = validated_data.get('email')
        firstname = validated_data.get('name')
        try:
            person = Person.objects.create(**validated_data)
        except Error:
            return person
        User.objects.create_user(username=username, first_name=firstname, email=username, password=password)
        return person

    def validate_name(self, value):
        return value

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.institution = validated_data.get('institution', instance.institution)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.academic_registry = validated_data.get('academic_registry', instance.academic_registry)
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


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    session = serializers.PrimaryKeyRelatedField(queryset=Session.objects.all())
    person = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    is_confirmed = serializers.BooleanField()
    status = serializers.BooleanField()

    class Meta:
        model = Participant
        fields = ('id', 'session', 'person', 'is_confirmed', 'status')

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.session = validated_data.get('session', instance.session)
        instance.person = validated_data.get('person', instance.person)
        instance.is_confirmed = validated_data.get('is_confirmed', instance.is_confirmed)
        instance.status = validated_data.get('status', instance.status)
        return instance