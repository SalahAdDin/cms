from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
    PageChooserPanel
)
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail_embed_videos.edit_handlers import EmbedVideoChooserPanel

"""
    Abstracts Models

        A few abstract classes that contain commonly used fields.
"""


class LinkFields(models.Model):
    """
        An object which will be a link in every page.
    """
    link_external = models.URLField(_('External Link'), blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        verbose_name=_("Page's Link"),
        on_delete=models.SET_NULL,
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+',
        verbose_name=_("File's link"),
        on_delete=models.SET_NULL,
    )
    link_email = models.EmailField(
        _("E-mail's link"),
        blank=True,
        null=True,
    )
    link_phone = models.CharField(
        _("Phone's link"),
        max_length=20,
        blank=True,
        null=True,
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        elif self.link_email:
            return 'mailto:%s' % self.link_email
        elif self.link_phone:
            return 'tel:%s' % self.link_phone.strip()
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
        FieldPanel('link_email'),
        FieldPanel('link_phone'),
    ]

    class Meta:
        abstract = True


class ContactFields(models.Model):
    """
        Add basic contact card with common fields.
    """
    name = models.CharField(max_length=100, blank=True, verbose_name=_('Name'), )
    telephone = models.CharField(max_length=20, blank=True, verbose_name=_('Phone'), )
    email = models.EmailField(blank=True, verbose_name=_('E-mail'), )
    address_1 = models.CharField(max_length=255, blank=True, verbose_name=_('Address 1'), )
    address_2 = models.CharField(max_length=255, blank=True, verbose_name=_('Address 2'), )
    district = models.CharField(max_length=255, blank=True, verbose_name=_('Neighborhood'), )
    city = models.CharField(max_length=255, blank=True, verbose_name=_('City'), )
    country = models.CharField(max_length=255, blank=True, verbose_name=_('Country'), )
    post_code = models.CharField(max_length=10, blank=True, verbose_name=_('Postal Code'), )
    facebook_url = models.URLField(blank=True, verbose_name=_('Facebook Profile URL'))
    google_plus_url = models.URLField(blank=True, verbose_name=_('Google + Profile URL'))
    twitter_url = models.URLField(blank=True, verbose_name=_('Twitter Profile URL'))

    panels = [
        FieldPanel('name'),
        FieldRowPanel([
            FieldPanel('telephone', classname="col6"),
            FieldPanel('email', classname="col6"),
        ]),
        FieldRowPanel([
            FieldPanel('address_1', classname="col6"),
            FieldPanel('address_2', classname="col6"),
        ]),
        FieldRowPanel([
            FieldPanel('post_code', classname="col4"),
            FieldPanel('district', classname="col6"),
        ]),
        FieldRowPanel([
            FieldPanel('city', classname="col6"),
            FieldPanel('country', classname="col6"),
        ]),
        FieldRowPanel([
            FieldPanel('facebook_url', classname="col12"),
            FieldPanel('google_plus_url', classname="col12"),
            FieldPanel('twitter_url', classname="col12"),
        ]),
    ]

    class Meta:
        abstract = True


class CarouselItem(LinkFields):
    """
        Add items for compose a Carousel.

        items: Objects LinkField type.
    """
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Image'),
    )
    video = models.ForeignKey(
        'wagtail_embed_videos.EmbedVideo',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Video')
    )
    embed_url = models.URLField(_('Embed URL'), blank=True)
    caption = models.CharField(_('Caption'), max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        EmbedVideoChooserPanel('video'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class RelatedLink(LinkFields):
    """
        Add related links in page.

        link: One object LinkField type.
    """
    title = models.CharField(_('Title'), max_length=255, help_text=_("Link's title."), )

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, _('Link')),
    ]

    class Meta:
        abstract = True
