from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Event


class IndexView(generic.ListView):
    template_name = 'events/base.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """Return the last five published events."""
        return Event.objects.filter(published=True).order_by('start_date')[:5]


class PreviousIndexView(generic.ListView):
    template_name = 'events/base.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """Return the last five published events."""
        return Event.objects.filter(published=True).order_by('start_date')


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


