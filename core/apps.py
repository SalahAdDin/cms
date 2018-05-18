from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreAppConfig(AppConfig):
    name = 'core'
    label = 'core'
    verbose_name = _('Core')
