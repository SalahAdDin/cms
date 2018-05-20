from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class HomeAppConfig(AppConfig):
    name = 'home'
    label = 'home'
    verbose_name = _('Home Page')
