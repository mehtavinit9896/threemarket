from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Team, Client

# Create your views here.

def index(request):
    events = Event.objects.filter(event_type='Event').order_by('-created')
    medias = Event.objects.filter(event_type='Media').order_by('-created')
    ads = Event.objects.filter(event_type='Ad').order_by('-created')
    team_members = Team.objects.filter().order_by('-created')
    clients = Client.objects.filter().order_by('-created')
    for event in events:
        event.desc=('<p style="word-break: break-word;">'+'</p><p style="word-break: break-word;">'.join(event.desc.split('\n'))+'</p>')
    context = {
		"events": events,
        "medias" :  medias,
        "ads": ads,
        "team_members" : team_members,
        "clients" : clients
        
	}
    return render(request, 'marketeers/index.html', context)
    
def left(request):
    context = {            
	}
    return render(request, 'marketeers/left.html', context)
