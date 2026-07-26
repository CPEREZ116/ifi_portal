import frappe
from .link_registry import LINK_PROVIDERS


def get_allowed_link_values(doctype, user=None):

    if not user:
        user = frappe.session.user

    provider = LINK_PROVIDERS.get(doctype)

    if not provider:
        return None

    return provider(user)


def build_link_filters(doctype, user=None):

    values = get_allowed_link_values(doctype, user)

    if values is None:
        return {}

    return {
        "name": ["in", values]
    }


