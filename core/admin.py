from django.contrib import admin

from .models import GlobalSettings
from .models import CMSImage
from .models import CMSRendition

admin.site.register(GlobalSettings)
admin.site.register(CMSImage)
admin.site.register(CMSRendition)
