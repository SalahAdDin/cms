from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from wagtail.admin.menu import MenuItem
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.editor_html import WhitelistRule
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler,
    BlockElementHandler
)
from wagtail.core import hooks
from wagtail.core.whitelist import allow_without_attributes


class StaffMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_staff


@hooks.register('register_settings_menu_item')
def register_staff_django_admin_menu_item():
    return StaffMenuItem(_('Site Admin'), '/django-admin', classnames='icon icon-wagtail-inverse', order=20000)


@hooks.register('register_rich_text_features')
def register_strikethrough_feature(features):
    """
    Registering the `strikethrough` feature, which uses the `STRIKETHROUGH` Draft.js inline style type,
    and is stored as HTML with an `<s>` tag.
    """
    feature_name = 'strikethrough'
    type_ = 'STRIKETHROUGH'
    tag = 's'

    control = {
        'type': type_,
        'label': 'S',
        # TODO
        # 'icon': 'icon icon-fa-strikethrough',
        # 'icon': ['M100 100 H 900 V 900 H 100 Z'],
        'description': ugettext('Strikethrough'),
        # This isn’t even required – Draftail has predefined styles for STRIKETHROUGH.
        # 'style': {'textDecoration': 'line-through'},
    }

    # features.default_features.append(feature_name)

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.register_converter_rule('editorhtml', feature_name, [
        WhitelistRule(feature_name, allow_without_attributes),
    ])


@hooks.register('register_rich_text_features')
def register_quotation_feature(features):
    """
    Registering the `quotation` feature, which uses the `QUOTATION` Draft.js inline style type,
    and is stored as HTML with an `<q>` tag.
    """
    feature_name = 'quotation'
    type_ = 'QUOTATION'
    tag = 'q'

    control = {
        'type': type_,
        'label': '❞',
        'description': ugettext('Quotation'),
        # This isn’t even required – Draftail has predefined styles for QUOTATION.
        # 'style': {'textDecoration': 'line-through'},
    }

    # features.default_features.append(feature_name)

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.register_converter_rule('editorhtml', feature_name, [
        WhitelistRule(feature_name, allow_without_attributes),
    ])


@hooks.register('register_rich_text_features')
def register_blockquote_feature(features):
    """
    Registering the `blockquote` feature, which uses the `blockquote` Draft.js block type,
    and is stored as HTML with a `<blockquote>` tag.
    """
    feature_name = 'blockquote'
    type_ = 'BLOCKQUOTE',
    tag = 'blockquote'

    control = {
        'type': 'BLOCKQUOTE',
        'label': '❝',
        'description': ugettext('Blockquote'),
        # Optionally, we can tell Draftail what element to use when displaying those blocks in the editor.
        'element': 'blockquote',
    }

    # features.default_features.append(feature_name)

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {tag: BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: tag}},
    })

    features.register_converter_rule('editorhtml', feature_name, [
        WhitelistRule(feature_name, allow_without_attributes),
    ])


@hooks.register('register_rich_text_features')
def register_underline_feature(features):
    """
    Registering the `underline` feature, which uses the `UNDERLINE` Draft.js inline style type,
    and is stored as HTML with an `<u>` tag.
    """
    feature_name = 'underline'
    type_ = 'UNDERLINE'
    tag = 'u'

    control = {
        'type': type_,
        'label': 'U',
        # TODO
        # 'icon': 'icon icon-fa-underline',
        # 'icon': ['M100 100 H 900 V 900 H 100 Z'],
        'description': ugettext('Underline'),
        # This isn’t even required – Draftail has predefined styles for UNDERLINE.
        # 'style': {'textDecoration': 'line-through'},
    }

    # features.default_features.append(feature_name)

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.register_converter_rule('editorhtml', feature_name, [
        WhitelistRule(feature_name, allow_without_attributes),
    ])


@hooks.register('register_rich_text_features')
def register_mark_feature(features):
    """
    Registering the `mark` feature, which uses the `MARK` Draft.js inline style type,
    and is stored as HTML with an `<mark>` tag.
    """
    feature_name = 'mark'
    type_ = 'MARK'
    tag = 'mark'

    control = {
        'type': type_,
        # 'label': 'H',
        'icon': 'icon icon-pick',
        # 'icon': ['M100 100 H 900 V 900 H 100 Z'],
        'description': ugettext('Highlight'),
        # This isn’t even required – Draftail has predefined styles for MARK.
        # 'style': {'textDecoration': 'line-through'},
    }

    # features.default_features.append(feature_name)

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.register_converter_rule('editorhtml', feature_name, [
        WhitelistRule(feature_name, allow_without_attributes),
    ])


@hooks.register('register_rich_text_features')
def register_keyboard_feature(features):
    """
    Registering the `mark` feature, which uses the `KEYBOARD` Draft.js inline style type,
    and is stored as HTML with an `<mark>` tag.
    """
    feature_name = 'keyboard'
    type_ = 'KEYBOARD'
    tag = 'kbd'

    control = {
        'type': type_,
        'label': '⌘',
        'description': ugettext('Keyboard'),
        # This isn’t even required – Draftail has predefined styles for KEYBOARD.
        # 'style': {'textDecoration': 'line-through'},
    }

    # features.default_features.append(feature_name)

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {tag: InlineStyleElementHandler(type_)},
        'to_database_format': {'style_map': {type_: tag}},
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    features.register_converter_rule('editorhtml', feature_name, [
        WhitelistRule(feature_name, allow_without_attributes),
    ])
