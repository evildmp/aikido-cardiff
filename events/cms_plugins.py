import datetime

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import ForthcomingEvents, Event


@plugin_pool.register_plugin
class ForthcomingEventsPlugin(CMSPluginBase):
    model = ForthcomingEvents
    name = _("Forthcoming events Plugin")
    render_template = "events/plugins/forthcomingevents.html"
    cache = False

    def render(self, context, instance, placeholder):
        events = Event.objects.order_by('start_date').filter(
            published=True, listed=True, end_date__gte=datetime.date.today()
        )
        if instance.limit:
            events = events[:instance.limit]
        context['events'] = events
        context = super(ForthcomingEventsPlugin, self).render(context, instance, placeholder)
        return context

# from cms.models.pluginmodel import CMSPlugin
#
# @plugin_pool.register_plugin
# class HelloPlugin(CMSPluginBase):
#     model = CMSPlugin
#     render_template = "hello.html"
#     cache = False
