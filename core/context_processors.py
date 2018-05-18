from django.conf import settings
from django.contrib.sites.models import Site
from django.db.models.functions import datetime
from django.utils.safestring import mark_safe
from string import Template

# TODO: Update to the current tracking code
# TODO: Implements in templates
TRACKING_CODE = """
    <script>
    window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};
    ga.l=+new Date;
    ga('create', '$ga_code', 'auto');
    ga('send', 'pageview');
    </script>
    <script async src='https://www.google-analytics.com/analytics.js'></script>
"""


def analytics(request):
    """
    Enable analytics script if debug is False
    """
    script = ''
    if not settings.DEBUG:
        template = Template(TRACKING_CODE)
        script = mark_safe(
            template.substitute(
                ga_code=settings.GOOGLE_ANALYTICS_CODE,
            )
        )

    return {'ANALYTICS': script}


def utils(request):
    return {
        # 'company_logo': settings.LOGO_COMPANY,
        'local': datetime.datetime.now(),
        'site': Site.objects.get_current(),
        'site_header': settings.SITE_HEADER
    }
