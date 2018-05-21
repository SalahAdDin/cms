from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    InlinePanel,
    FieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

from core.abstracts import RelatedLink


class AboutPageRelatedLinkButton(Orderable, RelatedLink):
    page = ParentalKey('about.AboutPage', related_name='related_link_buttons')


class AboutPageOffice(Orderable):
    page = ParentalKey('about.AboutPage', related_name='offices')
    title = models.TextField(_('Title'))
    svg = models.TextField(_('SVG icon'), null=True)
    description = models.TextField(_('Description'))

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
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
        'cms.CMSImage',
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
        InlinePanel('content_blocks', label=_('Content blocks')),
        InlinePanel('related_link_buttons', label=_('Header buttons')),
        InlinePanel('offices', label=_('Offices')),
        # FieldPanel('involvement_title'),
    ]
