# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('beginDate', models.DateField()),
                ('endDate', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('theme', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('charge', models.FloatField()),
                ('workload', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('idEdicao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Edition')),
            ],
        ),
        migrations.CreateModel(
            name='Ocurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('datePayment', models.DateField()),
                ('allowance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=63)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('institution', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=15, unique=True)),
                ('academicRegistry', models.CharField(max_length=15)),
                ('role', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryTime', models.DateTimeField()),
                ('exitTime', models.DateTimeField()),
                ('idOcurrence', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Ocurrence')),
                ('idParticipant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Raffle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize', models.CharField(max_length=255)),
                ('raffleDate', models.DateTimeField()),
                ('idOcurrence', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Ocurrence')),
                ('idParticipant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Edition')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('space', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('idEvent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Event')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Person')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Person'),
        ),
        migrations.AddField(
            model_name='participant',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Session'),
        ),
        migrations.AddField(
            model_name='ocurrence',
            name='idRoom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Room'),
        ),
        migrations.AddField(
            model_name='ocurrence',
            name='idSession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sati.Session'),
        ),
    ]
