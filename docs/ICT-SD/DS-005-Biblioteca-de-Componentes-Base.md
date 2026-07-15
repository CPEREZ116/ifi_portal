---
Manual: Sistema de Diseño Mi ICT (DS)
Documento: DS-005
Título: Biblioteca de Componentes Base
Proyecto: Proyecto Nehemías
Versión: 1.0
Estado: Borrador
Propietario: International Confederation of Theotherapy (ICT)
Autor: Proyecto Nehemías
Última actualización: Julio 2026
---

# Biblioteca de Componentes Base

## Portal Institucional Mi ICT

---

# Propósito

Definir los componentes visuales reutilizables que conformarán el Portal Institucional Mi ICT y los futuros servicios de la Plataforma Digital de la International Confederation of Theotherapy.

El objetivo es construir una interfaz consistente mediante componentes reutilizables, evitando desarrollos independientes para cada módulo.

---

# Filosofía

Mi ICT no se construye página por página.

Mi ICT se construye componente por componente.

Cada nuevo desarrollo deberá reutilizar los componentes existentes antes de crear nuevos elementos visuales.

---

# Principios

Los componentes deberán cumplir los siguientes principios:

- Reutilizables.
- Simples.
- Consistentes.
- Responsivos.
- Accesibles.
- Independientes.
- Evolutivos.

---

# Clasificación

Los componentes se organizan en cinco categorías.

## Componentes de Navegación

- Header
- Menú Principal
- Breadcrumb
- Footer

---

## Componentes de Contenido

- Hero
- Tarjetas
- Paneles
- Contenedores
- Separadores

---

## Componentes de Acción

- Botón Primario
- Botón Secundario
- Botón de Acción
- Botón de Icono

---

## Componentes de Entrada

- Campo de Texto
- Área de Texto
- Lista Desplegable
- Selector de Fecha
- Checkbox
- Radio Button
- Selector de Archivos

---

## Componentes de Retroalimentación

- Alertas
- Toast
- Loader
- Modal
- Confirmación
- Estado Vacío

---

# Componentes Base

---

# C-001 Header Institucional

## Propósito

Representar el encabezado oficial del Portal Mi ICT.

Siempre deberá incluir:

- Logotipo oficial.
- Menú principal.
- Acceso al Portal.

Nunca deberá contener elementos administrativos.

---

# C-002 Hero Institucional

Utilizado únicamente al inicio de cada servicio principal.

Incluye:

- Imagen institucional.
- Título.
- Subtítulo.
- Acción principal.

Debe transmitir cercanía y confianza.

---

# C-003 Tarjeta de Servicio

Representa una funcionalidad disponible.

Ejemplos:

- Donaciones.
- Certificados.
- Eventos.
- Cursos.

Cada tarjeta deberá incluir:

- Icono.
- Título.
- Descripción.
- Acción.

---

# C-004 Botón Primario

Representa la acción principal.

Ejemplos:

- Realizar Donación.
- Continuar.
- Guardar.

Color:

Azul Institucional.

---

# C-005 Botón Secundario

Representa acciones complementarias.

Ejemplos:

- Cancelar.
- Regresar.
- Más información.

---

# C-006 Campo de Texto

Todos los formularios utilizarán el mismo componente.

Características:

- Etiqueta superior.
- Validación.
- Mensaje de ayuda.
- Estado de error.

---

# C-007 Tarjeta Informativa

Utilizada para:

- Noticias.
- Devocionales.
- Eventos.

---

# C-008 Alerta

Tipos:

- Información.
- Éxito.
- Advertencia.
- Error.

Todas las alertas utilizarán el mismo diseño.

---

# C-009 Modal

Se utilizará únicamente cuando sea necesario interrumpir el flujo del usuario.

Evitar su uso excesivo.

---

# C-010 Estado Vacío

Cuando un usuario aún no tenga información.

Ejemplo:

"No tienes donaciones registradas."

Mostrar siempre:

- Ilustración.
- Mensaje.
- Acción recomendada.

---

# C-011 Loader

Mientras una operación está en proceso.

Nunca dejar pantallas congeladas.

Mostrar:

- Indicador de progreso.
- Mensaje sencillo.

Ejemplo:

"Estamos procesando tu información..."

---

# C-012 Avatar

Representa la identidad del usuario.

Utilizado en:

- Perfil.
- Menú superior.
- Dashboard.

---

# C-013 Badge

Permite representar estados.

Ejemplos:

- Pendiente.
- Pagado.
- En proceso.
- Aprobado.

---

# C-014 Breadcrumb

Facilita la navegación.

Ejemplo:

Inicio

>

Donaciones

>

Nueva Donación

---

# C-015 Footer Institucional

Compartido por toda la Plataforma.

Incluye:

- Información institucional.
- Derechos de autor.
- Proyecto Nehemías.
- Política de privacidad.
- Contacto.

---

# Reutilización

Todo nuevo componente deberá responder las siguientes preguntas:

¿Existe un componente similar?

¿Puede adaptarse?

¿Es realmente necesario crear uno nuevo?

La reutilización tendrá prioridad sobre la creación de nuevos componentes.

---

# Versionamiento

Cada componente será versionado.

Ejemplo:

C-001 Header v1.0

C-003 Tarjeta v1.2

La evolución deberá mantenerse documentada.

---

# Relación con el Desarrollo

Cada componente tendrá:

- Documentación funcional.
- Implementación HTML.
- Estilos CSS.
- Comportamiento JavaScript.
- Ejemplos de uso.

---

# Evolución

La Biblioteca de Componentes crecerá junto con Mi ICT.

Los nuevos dominios reutilizarán estos componentes, fortaleciendo una experiencia consistente para toda la Plataforma Digital.

---

# Declaración Final

La Biblioteca de Componentes constituye el lenguaje visual compartido de la Plataforma Digital ICT.

Cada componente representa una capacidad reutilizable que permitirá construir soluciones coherentes, sostenibles y fáciles de mantener durante los próximos años.

---

## Proyecto Nehemías

### Sistema de Diseño Mi ICT

**Principio Rector**

> No construimos páginas independientes.

> Construimos componentes reutilizables que fortalecen una única experiencia digital.