import frappe
from frappe.utils import flt


def calcular(doc):

    resultado = []

    for detalle in doc.conceptos_de_donacion:

        regla = obtener_regla(
            detalle.concepto,
            detalle.subconcepto
        )

        if not regla:
            frappe.throw(
                f"No existe una Regla de Distribución para el concepto {detalle.concepto}"
            )

        for destino in regla.destinos:

            valor = round(
                flt(detalle.valor) *
                flt(destino.porcentaje) / 100,
                2
            )

            resultado.append({

                "concepto": detalle.concepto,

                "subconcepto": detalle.subconcepto,

                "tipo_destino": destino.tipo_destino,

                "porcentaje": destino.porcentaje,

                "valor": valor

            })

    return resultado


def obtener_regla(concepto, subconcepto=None):

    filtros = {
        "activo": 1,
        "concepto": concepto
    }

    #---------------------------------------
    # Buscar regla específica
    #---------------------------------------

    if subconcepto:

        nombre = frappe.db.get_value(
            "Regla de Distribucion",
            {
                **filtros,
                "subconcepto": subconcepto
            },
            "name"
        )

        if nombre:
            return frappe.get_doc(
                "Regla de Distribucion",
                nombre
            )

    #---------------------------------------
    # Buscar regla general
    #---------------------------------------

    nombre = frappe.get_all(
        "Regla de Distribucion",
        filters={
            "activo": 1,
            "concepto": concepto,
            "subconcepto": ""
        },
        pluck="name",
        limit=1
    )

    if nombre:
        return frappe.get_doc(
            "Regla de Distribucion",
            nombre[0]
        )

    return None