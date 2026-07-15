---
Manual: Experiencia de Usuario (ICT-UX)
Documento: UX-001
Título: Mapa del Portal Mi ICT
Proyecto: Proyecto Nehemías
Versión: 1.0
Estado: Borrador
Propietario: International Confederation of Theotherapy (ICT)
Autor: Proyecto Nehemías
Última actualización: Julio 2026
---

# Mapa del Portal Mi ICT

## Propósito

Definir la arquitectura funcional del Portal Mi ICT, identificando los módulos, páginas, formularios, componentes y procesos que conformarán la experiencia digital del feligrés, donante y visitantes de la ICT.

El objetivo es construir el portal utilizando prioritariamente las capacidades nativas de Frappe Framework, desarrollando únicamente aquellas funcionalidades que representan procesos propios de la International Confederation of Theotherapy.

---

# Principios de Arquitectura

Antes de desarrollar cualquier funcionalidad se aplicará la siguiente regla:

1. ¿Existe en Frappe?
   - Sí → Configurar o personalizar.
   - No → Desarrollar en IFI Portal.

---

# Actores

El Portal contempla inicialmente los siguientes tipos de usuarios:

- Visitante
- Donante
- Feligrés
- Coordinador
- Administrador del Portal
- Tesorería
- Contabilidad

Cada actor tendrá una experiencia y permisos específicos.

---

# Arquitectura General

Portal Mi ICT

├── Sitio Institucional
├── Registro
├── Inicio de Sesión
├── Portal del Usuario
├── Donaciones
├── Certificados
├── Eventos
├── Cursos
├── Ayuda
└── Contacto

---

# Clasificación de Módulos

Cada módulo se implementará utilizando el componente nativo más adecuado de Frappe.

| Módulo | Tipo |
|---------|------|
| Inicio | Web Page |
| Acerca de | Web Page |
| Noticias | Web Page / Blog |
| Eventos | Web Page |
| Contacto | Web Form |
| Registro Portal | Web Form |
| Solicitud de Donación | Web Form |
| Portal del Usuario | Portal |
| Perfil | Portal |
| Mis Donaciones | Portal |
| Mis Certificados | Portal |
| Dashboard | Portal |
| Administración | Desk ERPNext |

---

# Navegación Principal

Visitante

Inicio

Donaciones

Eventos

Cursos

Ayuda

Ingresar

---

Usuario autenticado

Inicio

Mi Portal

Mis Donaciones

Mis Certificados

Mi Perfil

Cerrar Sesión

---

# Flujo General

Visitante

↓

Registro

↓

Validación

↓

Consulta Davidka

↓

Creación Usuario

↓

Portal habilitado

↓

Donaciones

↓

Planilla IFI

↓

Motor Contable

↓

ERPNext

---

# Componentes Visuales

Todos los módulos reutilizarán la Biblioteca Oficial de Componentes Mi ICT.

- C-001 Header
- C-002 Hero
- C-003 Tarjetas
- C-004 Botones
- C-005 Footer
- ...

---

# Integraciones

El Portal interactuará con los siguientes sistemas:

- ERPNext
- Davidka Misional
- Wompi
- AuraQuantic
- SIIMED

---

# Dominios Funcionales

El Portal se divide en cinco dominios:

- Institucional
- Pastoral
- Financiero
- Formación
- Administración

Cada dominio evolucionará de manera independiente.

---

# Roadmap de Implementación

## Fase 1

Portal Institucional

- Home
- Registro
- Login
- Dashboard

## Fase 2

Donaciones

- Sobre Digital
- Donación en Línea
- Certificados

## Fase 3

Gestión Pastoral

- Perfil
- Clasificación
- Eventos
- Cursos

## Fase 4

Gobierno Financiero

- Planillas
- Distribuciones
- Integración Contable

---

# Declaración Final

El Portal Mi ICT constituye la puerta de entrada digital a los servicios institucionales de la International Confederation of Theotherapy.

Su implementación priorizará el uso de las capacidades nativas de Frappe Framework, garantizando sostenibilidad, facilidad de mantenimiento y una evolución alineada con el Proyecto Nehemías.

---

## Proyecto Nehemías

### UX-001

**Principio Rector**

> No desarrollamos funcionalidades que Frappe ya ofrece.
> Desarrollamos únicamente aquello que representa el conocimiento y los procesos propios de la ICT.