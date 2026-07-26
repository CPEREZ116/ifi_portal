import frappe

# ============================================================================
# IFI Portal Security Engine
# Organization Services
# ============================================================================

# DocTypes
UNIT_DOCTYPE = "Unidad Organizacional"
ASSIGNMENT_DOCTYPE = "Asignacion Unidad Operativa"


def get_assigned_units(user: str) -> list[str]:
    """
    Return the operational units directly assigned to a user.

    Example:
        ["701", "801"]
    """

    return (
        frappe.get_all(
            ASSIGNMENT_DOCTYPE,
            filters={
                "usuario": user,
                "activo": 1,
            },
            pluck="unidad_operativa",
        )
        or []
    )


def get_descendant_units(unit: str) -> list[str]:
    """
    Return a unit and all its descendants using the Nested Set tree.

    Example:

        701
            702
                703
                704
            705

    Returns:

        ["701", "702", "703", "704", "705"]
    """

    node = frappe.db.get_value(
        UNIT_DOCTYPE,
        unit,
        ["lft", "rgt"],
        as_dict=True,
    )

    if not node:
        return []

    return (
        frappe.get_all(
            UNIT_DOCTYPE,
            filters={
                "lft": [">=", node.lft],
                "rgt": ["<=", node.rgt],
            },
            order_by="lft asc",
            pluck="name",
        )
        or []
    )


def get_allowed_units(user: str) -> list[str]:
    """
    Return every unit the user can access.

    This includes:

    - Direct assignments
    - All descendant units

    Duplicates are removed automatically.

    Example:

        User assigned to 701

        Returns:

        [
            "701",
            "702",
            "703",
            "704",
            "705"
        ]
    """

    allowed = set()

    assigned_units = get_assigned_units(user)

    for unit in assigned_units:
        descendants = get_descendant_units(unit)
        allowed.update(descendants)

    return sorted(allowed)



