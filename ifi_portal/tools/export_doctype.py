import frappe
from frappe.modules.export_file import export_to_files
from pathlib import Path
import json


def export(doctype):
    """Exporta un DocType al filesystem"""

    export_to_files(
        record_list=[["DocType", doctype]],
        create_init=True,
    )

    print(f"✔ Exportado {doctype}")


def export_all():
    """Exporta todos los DocTypes personalizados del módulo IFI Portal"""

    doctypes = frappe.get_all(
        "DocType",
        filters={
            "module": "IFI Portal",
            "custom": 1
        },
        order_by="name",
        pluck="name"
    )

    print(f"\nSe encontraron {len(doctypes)} DocTypes\n")

    for dt in doctypes:
        print(f"Exportando {dt}...")
        export(dt)

    print("\nProceso terminado.")


def validate():
    """Verifica que todos los DocTypes exportados tengan su JSON"""

    app_path = Path(frappe.get_app_path("ifi_portal"))

    base = app_path / "ifi_portal" / "doctype"

    faltantes = []

    doctypes = frappe.get_all(
        "DocType",
        filters={
            "module": "IFI Portal",
            "custom": 1
        },
        pluck="name"
    )

    for dt in doctypes:

        folder = frappe.scrub(dt)

        archivo = base / folder / f"{folder}.json"

        if archivo.exists():
            print(f"✔ {dt}")
        else:
            print(f"✘ {dt}")
            faltantes.append(dt)

    print("\n------------------------")
    print(f"Total : {len(doctypes)}")
    print(f"Faltan: {len(faltantes)}")

    if faltantes:
        print("\nDocTypes faltantes:")
        for d in faltantes:
            print(" -", d)
