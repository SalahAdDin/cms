from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailgeowidget.edit_handlers import GeoPanel

from condensedinlinepanel.edit_handlers import CondensedInlinePanel

from core.abstracts import RelatedLink


class AboutPageRelatedLinkButton(Orderable, RelatedLink):
    page = ParentalKey('about.AboutPage', related_name='related_link_buttons')


class AboutPageOffice(Orderable):
    page = ParentalKey('about.AboutPage', related_name='offices')
    title = models.TextField(_('Title'))
    svg = models.TextField(_('SVG icon'), null=True)
    address = models.CharField(_('Address'), help_text=_("Location's address"), max_length=250)
    map = models.CharField(_('Map'), null=True, max_length=250)

    panels = [
        FieldPanel('title'),
        MultiFieldPanel([
            FieldPanel('address'),
            GeoPanel('map', address_field='address'),
        ], _('Location details')),
        FieldPanel('svg')
    ]


class AboutPageContentBlock(Orderable):
    page = ParentalKey('about.AboutPage', related_name='content_blocks')
    year = models.IntegerField(_('Year'))
    title = models.TextField(_('Title'))
    description = models.TextField(_('Description'))
    image = models.ForeignKey(
        'core.CMSImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Image')
    )

    panels = [
        FieldPanel('year'),
        FieldPanel('title'),
        FieldPanel('description'),
        ImageChooserPanel('image')
    ]


class AboutPage(Page):
    main_image = models.ForeignKey(
        'core.CMSImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Main image')
    )
    heading = models.TextField(_('Heading'), blank=True)
    # intro = models.TextField(_('Introduction'), blank=True)
    body = RichTextField(_('Body'))
    # involvement_title = models.TextField(_('Involvement title'), blank=True)

    content_panels = [
        FieldPanel('title', classname='full title'),
        ImageChooserPanel('main_image'),
        FieldPanel('heading', classname='full'),
        # FieldPanel('intro', classname='full'),
        FieldPanel('body', classname='full'),
        CondensedInlinePanel('content_blocks', label=_('Content blocks')),
        CondensedInlinePanel('related_link_buttons', label=_('Header buttons')),
        CondensedInlinePanel('offices', label=_('Offices')),
        # FieldPanel('involvement_title'),
    ]
