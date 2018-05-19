from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    ObjectList,
    PageChooserPanel,
    TabbedInterface
)
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.images.models import (
    AbstractImage,
    AbstractRendition,
    Image
)


class CMSImage(AbstractImage):
    """
        Extends AbstractImage model for add some functions and fields in new Image model.
    """
    credit = models.CharField(max_length=255, blank=True, verbose_name=_('Credit'))

    admin_form_fields = Image.admin_form_fields + (
        'credit',
    )

    @property
    def credit_text(self):
        return self.credit


class CMSRendition(AbstractRendition):
    """
        Create a new Image Rendition for the new Image model.
    """
    image = models.ForeignKey(
        'CMSImage',
        related_name='renditions',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )


"""
    Settings
"""


@register_setting(icon='site')
class GlobalSettings(BaseSetting):
    contact_telephone = models.CharField(max_length=255, verbose_name=_('Telephone'))
    contact_email = models.EmailField(max_length=255, verbose_name=_('Email address'))
    contact_twitter = models.CharField(max_length=255, verbose_name=_('Twitter'))
    contact_facebook = models.CharField(max_length=255, verbose_name=_('Facebook'))
    contact_linked_in = models.CharField(max_length=255, verbose_name=_('Linked In'))
    contact_google_plus = models.CharField(max_length=255, verbose_name=_('Google Plus'))
    contact_youtube = models.CharField(max_length=255, verbose_name=_('YouTube'))
    email_newsletter_teaser = models.CharField(
        verbose_name=_('News letter teaser'),
        max_length=255,
        help_text=_('Text that sits above the email newsletter')
    )
    email_mailing_list = models.CharField(
        verbose_name=_('Mailing list e-mail'),
        max_length=255,
    )
    office_address_title = models.CharField(
        verbose_name=_('Office address title'),
        max_length=255,
        help_text=_('Address title')
    )
    office_address = models.CharField(
        verbose_name=_('Office address'),
        max_length=255,
        help_text=_('Full address')
    )
    office_address_link = models.URLField(
        verbose_name=_('Office address link'),
        max_length=255,
        help_text=_('Link to google maps')
    )

    office_tab_panels = [
        FieldPanel('office_address_title'),
        FieldPanel('office_address'),
        FieldPanel('office_address_link'),
    ]
    email_tab_panels = [
        FieldPanel('email_newsletter_teaser'),
        FieldPanel('email_mailing_list'),
    ]
    contact_tab_panels = [
        FieldPanel('contact_telephone'),
        FieldPanel('contact_email'),
        FieldPanel('contact_twitter'),
        FieldPanel('contact_facebook'),
        FieldPanel('contact_linked_in'),
        FieldPanel('contact_google_plus'),
        FieldPanel('contact_youtube'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(contact_tab_panels, heading=_('Contact tab')),
        ObjectList(email_tab_panels, heading=_('Mailing list tab')),
        ObjectList(office_tab_panels, heading=_('Office tab')),
    ])

    class Meta:
        verbose_name = _('Global Setting')
        verbose_name_plural = _('Global Settings')
