from django.contrib import admin
from .models import Event, Team, Client
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = ('id', 'type', 'name', 'heading', 'desc','image','created')
    
class TeamAdmin(admin.ModelAdmin):
	list_display = ('id', 'name','role','image','created')
    
class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'name','image','created')

admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Client)