import frappe

from .organization import get_allowed_units


# ============================================================================
# IFI Portal Security Engine
# Permission Services
# ============================================================================

DEFAULT_FIELD = "unidad_organizacional"


def get_allowed_filter(user=None):
    """
    Devuelve el filtro para usar en frappe.get_all()

    Example:

        filters.update(
            get_allowed_filter()
        )
    """

    if not user:
        user = frappe.session.user

    units = get_allowed_units(user)

    if not units:
        return {
            DEFAULT_FIELD: ["=", ""]
        }

    return {
        DEFAULT_FIELD: ["in", units]
    }


def has_unit_access(unit, user=None):
    """
    Valida si un usuario tiene acceso a una Unidad Organizacional.
    """

    if not user:
        user = frappe.session.user

    return unit in get_allowed_units(user)


def validate_document_permission(doc, field=DEFAULT_FIELD, user=None):
    """
    Valida que el documento pertenezca
    a una unidad permitida.
    """

    if not user:
        user = frappe.session.user

    unit = doc.get(field)

    if not unit:
        return

    if not has_unit_access(unit, user):

        frappe.throw(
            f"No tiene permisos sobre la Unidad Organizacional {unit}."
        )


def build_permission_query_conditions(
    user,
    table,
    field=DEFAULT_FIELD,
):
    """
    Construye la condición SQL utilizada por Frappe
    para limitar los registros visibles.
    """

    units = get_allowed_units(user)

    if not units:
        return "1=0"

    values = "', '".join(units)

    return (
        f"`{table}`.`{field}` "
        f"IN ('{values}')"
    )


def get_allowed_units_query(user=None):

    if not user:
        user = frappe.session.user

    units = get_allowed_units(user)

    return units