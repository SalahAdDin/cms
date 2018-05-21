from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import (
    Page,
    Orderable
)

from condensedinlinepanel.edit_handlers import CondensedInlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from core.abstracts import (
    BrochureItem,
    CarouselItem,
    RelatedLink
)


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey(
        'home.HomePage',
        related_name='carousel_items',
        on_delete=models.CASCADE,
    )


class HomePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey(
        'home.HomePage',
        related_name='related_links',
        on_delete=models.CASCADE,
    )


class HomePageBrochureItem(Orderable, BrochureItem):
    page = ParentalKey(
        'home.HomePage',
        related_name='brochure_items',
        on_delete=models.CASCADE,
    )


class HomePageClient(Orderable, RelatedLink):
    page = ParentalKey('home.HomePage', related_name='clients')
    image = models.ForeignKey(
        'core.CMSImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Client's logo"
    )

    panels = RelatedLink.panels + [
        ImageChooserPanel('image')
    ]


class HomePageProduct(Orderable, RelatedLink):
    page = ParentalKey('home.HomePage', related_name='products')
    title = models.CharField(_("Product section's title"))
    image = models.ForeignKey(
        'core.CMSImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_("Product section's image")
    )
    description = models.CharField(_("Product section's description"))
    product = models.ForeignKey(
        'product.ProductPage',
        on_delete=models.SET_NULL,
        related_name='+',
        blank=True,
        null=True,
    )

    panels = RelatedLink.panels + [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        FieldPanel('description'),
        PageChooserPanel('product'),
    ]


class HomePage(Page):
    brochures_title = models.TextField(blank=True, verbose_name="Brochures section's title")
    clients_title = models.TextField(blank=True, verbose_name="Clients section's title")
    products_title = models.TextField(blank=True, verbose_name="Products section's title")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Home Page')

    content_panels = [
        FieldPanel('title', classname="full title"),
        CondensedInlinePanel('carousel_items', label=_("Carousel's items")),
        FieldPanel('clients_title'),
        CondensedInlinePanel('clients', label=_("Clients"), card_header_from_field="title"),
        FieldPanel('products_title'),
        CondensedInlinePanel('products', label=_('Products'), card_header_from_field="title"),
        FieldPanel('brochures_title'),
        CondensedInlinePanel('brochure_items', label=_('Brochures'), card_header_from_field="title"),
        CondensedInlinePanel('related_links', label=_('Related links'), card_header_from_field="title"),
    ]
