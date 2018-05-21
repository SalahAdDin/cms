from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    FieldBlock,
    ListBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock
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


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', _('Select a header size')),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class PhotoGridBlock(StructBlock):
    images = ListBlock(ImageChooserBlock())

    class Meta:
        icon = "grip"
        template = "blocks/photo_grid_block.html"


class PullQuoteBlock(StructBlock):
    attribution = CharBlock(label=_('Attribution'))
    quote = RichTextBlock(label=_('Quote'), classname='quote title')

    class Meta:
        template = 'blocks/pull_quote.html'  # TODO: Review this for template and "blockquote" richtextfield implementation
        icon = 'openquote'


class StoryBlock(StreamBlock):
    header = HeadingBlock(classname="title")
    intro = RichTextBlock(icon="pilcrow", label=_('Intro'))
    paragraph = RichTextBlock(icon="pilcrow", label=_('Paragraph'))
    aligned_image = ImageBlock(label=_('Aligned image'))
    aligned_video = EmbedVideoBlock(label=_('Aligned video'))
    wide_image = WideImage(label=_('Wide Image'))
    bust_out = BustOutBlock(label=_('Bust out'))
    pull_quote = PullQuoteBlock(label=_('Pull Quote'))
    raw_html = RawHTMLBlock(label=_('Raw HTML'), icon="code")
    embed = EmbedBlock(icon="code", label=_('Embed'))
    address = GMapBlock(label=_('Address'))
    photo_grid = PhotoGridBlock(label=_('Photo Grid'))
