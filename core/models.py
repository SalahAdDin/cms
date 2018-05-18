from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
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
