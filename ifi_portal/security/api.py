import frappe

from .links import get_allowed_link_values

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def link_query(
    doctype,
    txt,
    searchfield,
    start,
    page_len,
    filters,
):

    allowed = get_allowed_link_values(
        doctype,
        frappe.session.user
    )

    frappe.logger().info(f"ALLOWED: {allowed}")

    txt = f"%{txt}%"

    allowed = get_allowed_link_values(doctype, frappe.session.user)

    if not allowed:
        return []


    return frappe.db.sql(
    f"""
    SELECT
        name,
        nombre
    FROM `tab{doctype}`
    WHERE
        name IN %(allowed)s
        AND is_group = 0
        AND (
            name LIKE %(txt)s
            OR codigo LIKE %(txt)s
            OR nombre LIKE %(txt)s
        )
    ORDER BY codigo
    LIMIT %(start)s, %(page_len)s
    """,
    {
        "allowed": tuple(allowed),
        "txt": txt,
        "start": start,
        "page_len": page_len,
    },
    as_list=True,
)

import json

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def donacion_query(
    doctype,
    txt,
    searchfield,
    start,
    page_len,
    filters=None,
):

    if filters is None:
        filters = {}

    txt = f"%{txt}%"

    usadas = filters.get("usadas") or []

    # Cuando llega desde JavaScript normalmente viene como JSON
    if isinstance(usadas, str):
        try:
            usadas = json.loads(usadas)
        except Exception:
            usadas = []

    where = """
        estado = 'Borrador'
        AND unidad_organizacional = %(unidad)s
        AND calendario = %(calendario)s
        AND entrega = %(entrega)s
        AND (
            IFNULL(planilla, '') = ''
            OR planilla = %(planilla)s
        )
    """

    params = {
        "unidad": filters.get("unidad_organizacional"),
        "calendario": filters.get("calendario"),
        "entrega": filters.get("entrega"),
        "planilla": filters.get("planilla"),
        "txt": txt,
        "start": start,
        "page_len": page_len,
    }

    if usadas:
        where += "\nAND name NOT IN %(usadas)s"
        params["usadas"] = tuple(usadas)

    return frappe.db.sql(
        f"""
        SELECT
            name,
            nombre
        FROM `tabDonacion`
        WHERE
            {where}
            AND (
                name LIKE %(txt)s
                OR nombre LIKE %(txt)s
                OR identificacion LIKE %(txt)s
            )
        ORDER BY name
        LIMIT %(start)s, %(page_len)s
        """,
        params,
        as_list=True,
    )