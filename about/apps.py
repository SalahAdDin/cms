from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AboutConfig(AppConfig):
    name = 'about'
    label = 'about'
    verbose_name = _('About Page')
