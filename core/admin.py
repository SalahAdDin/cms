from django.contrib import admin

from .models import (
    CMSImage,
    CMSRendition,
    GlobalSettings
)

from .snippets import (
    Advert,
    AdvertPlacement
)


admin.site.register(Advert)
admin.site.register(AdvertPlacement)
admin.site.register(CMSImage)
admin.site.register(CMSRendition)
admin.site.register(GlobalSettings)
