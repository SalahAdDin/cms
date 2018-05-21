from django.utils.translation import ugettext_lazy as _

from wagtail.admin.menu import MenuItem
from wagtail.core import hooks


class StaffMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_staff


@hooks.register('register_settings_menu_item')
def register_staff_django_admin_menu_item():
    return StaffMenuItem(_('Site Admin'), '/django-admin', classnames='icon icon-wagtail-inverse', order=20000)
