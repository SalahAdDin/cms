from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.core.blocks import (
    FieldBlock,
    StructBlock,
    CharBlock,
    RichTextBlock,
    RawHTMLBlock,
    StreamBlock
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from wagtail_embed_videos.blocks import EmbedVideoChooserBlock
from wagtailgeowidget.blocks import GeoBlock

"""
    StreamField blocks definition and configuration

        First, we'll create a few block for the content pages, they all enable
        us to use a more complex content page without much problems.
"""

alignment_choices = [
    ('left', _('Wrap left')),
    ('right', _('Wrap right')),
    ('half', _('Half width')),
    ('full', _('Full width')),
]


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=alignment_choices)


class ImageBlock(StructBlock):
    image = ImageChooserBlock(label=_('Image'))
    alignment = ImageFormatChoiceBlock(label=_('Alignment'))
    caption = CharBlock(label=_('Caption'))
    attribution = CharBlock(label=_('Attribution'), required=False)

    class Meta:
        icon = 'image'
        template = 'blocks/aligned_image.html'


class EmbedVideoFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=alignment_choices)


class EmbedVideoBlock(StructBlock):
    video = EmbedVideoChooserBlock(label=_('Video'))
    alignment = ImageFormatChoiceBlock(label=_('Alignment'))
    caption = CharBlock(label=_('Caption'))
    attribution = CharBlock(required=False, label=_('Attribution'))

    class Meta:
        icon = 'media'
        template = 'blocks/aligned_video.html'


class BustOutBlock(StructBlock):
    image = ImageChooserBlock(label=_('Image'))
    text = RichTextBlock(label=_('Text'))

    class Meta:
        icon = 'pick'
        template = 'blocks/bust_out.html'


class WideImage(StructBlock):
    image = ImageChooserBlock(label=_('Image'))

    class Meta:
        icon = "image"
        template = 'blocks/wide_image.html'


class GMapBlock(StructBlock):
    address = CharBlock(label=_('Address'), help_text=_("Location's address"), required=False)
    map = GeoBlock(address_field='address', label=_('Map'))

    class Meta:
        icon = 'site'
        template = 'blocks/address.html'


class StoryBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow", label=_('Intro'))
    paragraph = RichTextBlock(icon="pilcrow", label=_('Paragraph'))
    aligned_image = ImageBlock(label=_('Aligned image'))
    aligned_video = EmbedVideoBlock(label=_('Aligned video'))
    wide_image = WideImage(label=_('Wide Image'))
    bust_out = BustOutBlock(label=_('Bust out'))
    raw_html = RawHTMLBlock(label=_('Raw HTML'), icon="code")
    embed = EmbedBlock(icon="code", label=_('Embed'))
    address = GMapBlock(label=_('Address'))
