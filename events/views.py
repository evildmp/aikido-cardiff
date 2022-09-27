import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Event

from django.http import HttpResponse
from django.views import View

class EventsView(View):
    template_name = 'events/base.html'

    def get(self, request):
        current_events = Event.objects.filter(published=True, end_date__gt=datetime.datetime.now()).order_by('start_date')
        previous_events = Event.objects.filter(published=True, end_date__lt=datetime.datetime.now()).order_by('start_date').reverse()
        return render(request, 'events/base.html', {
            'current_events': current_events,
            'previous_events': previous_events,
        })

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


