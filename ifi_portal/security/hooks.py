from .permissions import build_permission_query_conditions
from .secured_doctypes import SECURED_DOCTYPES


def permission_query(user, doctype):

    config = SECURED_DOCTYPES.get(doctype)

    if not config:
        return None

    return build_permission_query_conditions(
        user=user,
        table=f"tab{doctype}",
        field=config["field"],
    )


def donacion_query(user):
    return permission_query(user, "Donacion")


def recibo_donacion_query(user):
    return permission_query(user, "Recibo Donacion")


def planilla_query(user):
    return permission_query(user, "Planilla")