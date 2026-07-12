# ICT-EA-011 — Modelo de Integración Institucional

## Proyecto Nehemías

**Iniciativa de Arquitectura Empresarial para la preservación del Patrimonio Digital Institucional de la ICT.**

> **"Preservamos el conocimiento institucional para servir a las generaciones futuras."**

---

# Propósito

Definir el modelo de integración que permitirá la interoperabilidad entre los dominios empresariales de la ICT, garantizando el intercambio seguro, controlado y trazable de la información institucional.

El Modelo de Integración constituye uno de los pilares de la Arquitectura Empresarial ICT.

---

# Introducción

La Arquitectura Empresarial reconoce que ninguna plataforma debe funcionar de forma aislada.

Cada dominio administra su propia información, pero todos deben colaborar mediante mecanismos de integración estandarizados.

La integración no busca duplicar datos; busca compartir capacidades e información de manera controlada.

---

# Principios de Integración

- Una única fuente oficial de información.
- Integración antes que duplicación.
- APIs antes que acceso directo a bases de datos.
- Eventos cuando el negocio lo requiera.
- Seguridad y trazabilidad en todas las integraciones.
- Documentación obligatoria de cada servicio.

---

# Dominios Integrados

## Gobierno Pastoral

Publica información relacionada con:

- Personas.
- Organización ministerial.
- Iglesias.
- Distritos.
- Territoriales.

---

## Gobierno Financiero

Publica:

- Recibos IFI.
- Planillas.
- Distribuciones.
- Estados financieros operativos.

Consume:

- Personas.
- Organización ministerial.
- Catálogos contables.

---

## Gobierno Administrativo y Contable

Publica:

- Catálogo de cuentas.
- Centros de costo.
- Estado de contabilización.
- Información tributaria.

Consume:

- Operaciones financieras preparadas para contabilización.

---

## Centro de Conocimiento Institucional

Publica:

- Procedimientos.
- Reglamentos.
- Arquitectura.
- Reglas de negocio.
- Documentación oficial.

---

## Inteligencia Artificial Institucional

Consume exclusivamente conocimiento oficial publicado por el Centro de Conocimiento Institucional.

No accede directamente a las bases de datos operacionales.

---

# Mecanismos de Integración

- APIs REST.
- Webhooks.
- Eventos.
- Servicios programados.
- Mensajería (cuando sea necesario).

---

# Gobierno de las APIs

Toda API institucional deberá contar con:

- Propietario.
- Documentación.
- Versionamiento.
- Autenticación.
- Autorización.
- Registro de auditoría.
- Política de cambios.

---

# Flujo de Integración

1. Un dominio genera un evento de negocio.
2. La información es validada.
3. Se publica mediante un servicio documentado.
4. Los dominios consumidores procesan el evento.
5. Se registra la trazabilidad.
6. El conocimiento relacionado se documenta en el CCI.

---

# Beneficios

- Integraciones desacopladas.
- Menor dependencia entre plataformas.
- Escalabilidad.
- Reutilización de servicios.
- Trazabilidad.
- Continuidad institucional.

---

# Visión

La integración institucional permitirá incorporar nuevas plataformas sin modificar la lógica de negocio de los dominios existentes, preservando la estabilidad y la evolución de la Plataforma Digital ICT.

---

# Reflexión Final

La integración no consiste únicamente en conectar aplicaciones.

Consiste en permitir que los dominios empresariales colaboren preservando la autonomía, el conocimiento institucional y la misión de la ICT.

---

## Proyecto Nehemías

**Iniciativa de Arquitectura Empresarial para la preservación del Patrimonio Digital Institucional de la ICT.**

### Filosofía

> No construimos software.

> Construimos capacidades institucionales.

### Lema

> **"Preservamos el conocimiento institucional para servir a las generaciones futuras."**
