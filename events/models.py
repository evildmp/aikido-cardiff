from django.db import models

from cms.models.fields import PlaceholderField

from filer.fields.image import FilerImageField


class Event(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    image = FilerImageField(null=True, blank=True, related_name='event_images', on_delete=models.SET_NULL)
    start_date = models.DateField('starts')
    end_date = models.DateField('ends', null=True, blank=True)
    published = models.BooleanField(default=False)
    listed = models.BooleanField(default=False)
    slug = models.SlugField()
    body = PlaceholderField('body')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["start_date"]


from cms.models.pluginmodel import CMSPlugin

class ForthcomingEvents(CMSPlugin):
    limit = models.PositiveIntegerField(default=0)

    STYLES = [
        ('SIMPLE', 'Simple'),
        ('FANCY', 'Fancy'),
    ]
    style = models.CharField(
        max_length=10,
        choices=STYLES,
        default='SIMPLE',
    )


# from cms.models import CMSPlugin
# from events.models import Event
#
#
# class PollPluginModel(CMSPlugin):
#     poll = models.ForeignKey(Poll)
#
#     def __str__(self):
#         return self.poll.question
