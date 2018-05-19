from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel
)
from wagtail.snippets.models import register_snippet


class AdvertPlacement(models.Model):
    page = ParentalKey(
        'wagtailcore.Page',
        related_name='advert_placements',
        on_delete=models.CASCADE,
    )
    advert = models.ForeignKey(
        'core.Advert',
        related_name='+',
        on_delete=models.CASCADE,
    )


@register_snippet
class Advert(models.Model):
    page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='adverts',
        null=True,
        blank=True,
        verbose_name=_('Page'),
        on_delete=models.CASCADE,
    )
    url = models.URLField(_('Link'), null=True, blank=True)
    text = models.CharField(_('Text'), max_length=255)

    class Meta:
        verbose_name_plural = _('Alerts')
        verbose_name = _('Alert')

    panels = [
        PageChooserPanel('page'),
        FieldPanel('url'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text
