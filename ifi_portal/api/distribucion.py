import frappe

from ifi_portal.services.distribucion import calcular


@frappe.whitelist()
def calcular_distribucion(docname):

    doc = frappe.get_doc(
        "Donacion",
        docname
    )

    return calcular(doc)