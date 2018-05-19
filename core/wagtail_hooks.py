from django.utils.translation import ugettext_lazy as _

from wagtail.admin.menu import MenuItem
from wagtail.core import hooks


@hooks.register('register_settings_menu_item')
def register_django_admin_menu_item():
    return MenuItem(_('Site Admin'), '/django-admin', classnames='icon icon-wagtail-inverse', order=20000)
