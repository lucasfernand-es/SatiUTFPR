from sati.models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class EditionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    begin_date = serializers.DateField()
    end_date = serializers.DateField()
    is_active = serializers.BooleanField()
    theme = serializers.CharField()
    description = serializers.CharField()
    # events = serializers.StringRelatedField(read_only=True)
    events = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='event-detail')

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


class EventSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    edition = serializers.PrimaryKeyRelatedField(queryset=Edition.objects.all())
    name = serializers.CharField()
    type = serializers.CharField()
    fee = serializers.FloatField()
    workload = serializers.IntegerField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    class Meta:
        model = Event
        ordering = ['name']
        fields = ('id', 'edition', 'name', 'type', 'fee', 'workload', 'description', 'is_active')

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_edition = validated_data.get('id_edition', instance.id_edition)
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.fee = validated_data.get('fee', instance.fee)
        instance.workload = validated_data.get('workload', instance.workload)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
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
    academicRegistry = serializers.CharField()
    role = serializers.CharField()
    is_active = serializers.BooleanField()

    class Meta:
        model = Person
        ordering = ['name']
        fields = ('id', 'name', 'email', 'institution',
                  'cpf', 'academicRegistry', 'role', 'is_active') # 'password',

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.institution = validated_data.get('institution', instance.institution)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.academicRegistry = validated_data.get('academicRegistryacademicRegistry', instance.cpf)
        instance.role = validated_data.get('role', instance.role)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        return instance
