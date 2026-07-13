# GF-001 — Modelo de Gestión de Ingresos

# Proyecto Nehemías

## Manual del Dominio de Gobierno Financiero

**Dominio:** Gobierno Financiero  
**Código:** GF-001  
**Versión:** 1.0  
**Estado:** Borrador  
**Última actualización:** Julio 2026

> **"Preservamos el conocimiento institucional para servir a las generaciones futuras."**

---

# Propósito

Definir el modelo funcional de la Gestión de Ingresos de la ICT, estableciendo el ciclo completo mediante el cual los recursos recibidos por la organización son registrados, validados, distribuidos y preparados para su incorporación al Gobierno Administrativo y Contable.

La Gestión de Ingresos constituye la primera capacidad implementada dentro del Dominio de Gobierno Financiero y será la base de la Implementación Piloto del Proyecto Nehemías.

---

# Objetivo

Garantizar que todo ingreso recibido por la ICT sea administrado con:

- Transparencia.
- Trazabilidad.
- Integridad.
- Oportunidad.
- Control.
- Auditoría.

Todo ingreso deberá poder reconstruirse completamente desde su origen hasta su contabilización.

---

# Alcance

La Gestión de Ingresos comprende:

- Registro de la intención de donación.
- Recaudo.
- Confirmación del pago.
- Generación del Recibo IFI.
- Aplicación de reglas de distribución.
- Consolidación en la Planilla de Ingresos.
- Workflow financiero.
- Preparación para la contabilización.
- Publicación de indicadores operativos.

La contabilización pertenece al Dominio de Gobierno Administrativo y Contable.

---

# Actores

## Feligrés

Origen del ingreso.

## Portal Institucional

Canal de interacción con el feligrés.

## Pasarela de Pago

Procesa el recaudo electrónico.

## Gobierno Financiero

Administra el ciclo de ingresos.

## Tesorería

Valida y aprueba la información financiera.

## Gobierno Administrativo y Contable

Recibe la información aprobada para su contabilización.

---

# Capacidades del Modelo

- Portal del Feligrés.
- Sobre de Diezmo.
- Motor de Recaudo.
- Integración con Wompi.
- Recibo IFI.
- Motor de Distribución.
- Planilla de Ingresos.
- Workflow Financiero.
- Contabilización ERPNext.
- Dashboard Ejecutivo.

---

# Flujo Funcional

```text
Feligrés
      │
Portal Institucional
      │
Sobre de Diezmo
      │
Pasarela de Pago (Wompi)
      │
Confirmación del Pago
      │
Recibo IFI
      │
Motor de Distribución
      │
Planilla de Ingresos
      │
Workflow Financiero
      │
Contabilización ERPNext
      │
Indicadores y Reportes
```

---

# Principios del Dominio

- Todo ingreso tendrá un origen identificado.
- Ningún ingreso será distribuido sin respaldo documental.
- Toda distribución será reproducible y auditable.
- Toda modificación deberá quedar registrada.
- Ninguna contabilización se realizará sin la aprobación del Workflow Financiero.
- El conocimiento funcional del proceso deberá permanecer documentado en el Centro de Conocimiento Institucional.

---

# Documentos del Dominio

El modelo de Gestión de Ingresos se desarrolla mediante los siguientes documentos:

- GF-002 — Portal Institucional.
- GF-003 — Portal del Feligrés.
- GF-004 — Sobre de Diezmo.
- GF-005 — Motor de Recaudo.
- GF-006 — Integración con Wompi.
- GF-007 — Recibo IFI.
- GF-008 — Motor de Distribución.
- GF-009 — Planilla de Ingresos.
- GF-010 — Workflow Financiero.
- GF-011 — Contabilización ERPNext.
- GF-012 — Dashboard Ejecutivo.

Cada documento describe una capacidad específica del dominio.

---

# Relación con la Arquitectura Empresarial

Este documento implementa los principios definidos en el Manual Oficial de Arquitectura Empresarial ICT y constituye la primera aplicación práctica del Dominio de Gobierno Financiero dentro del Proyecto Nehemías.

---

# Visión

La Gestión de Ingresos permitirá que la ICT administre los recursos confiados por sus feligreses mediante procesos estandarizados, transparentes y trazables, fortaleciendo la confianza institucional y preservando el conocimiento asociado a cada operación.

---

# Reflexión Final

La Gestión de Ingresos no comienza con un pago.

Comienza con la confianza de una persona que decide apoyar la misión de la ICT.

El propósito del Dominio de Gobierno Financiero es administrar esa confianza con fidelidad, transparencia y excelencia, dejando un registro íntegro que pueda ser comprendido, auditado y preservado para las generaciones futuras.

---

## Proyecto Nehemías

**Manual del Dominio de Gobierno Financiero**

**Filosofía**

> No construimos formularios.

> Construimos capacidades empresariales.

**Lema**

> **"Preservamos el conocimiento institucional para servir a las generaciones futuras."**
