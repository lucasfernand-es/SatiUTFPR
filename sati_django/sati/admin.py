from django.contrib import admin

from sati.models import Person, Edition, Event
# Register your models here.

admin.site.register(Person)
admin.site.register(Edition)
admin.site.register(Event)
