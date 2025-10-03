## Presentación del hito 5

**Introducción**  
Este proyecto es un sistema de gestión de inmuebles desarrollado en Django. El objetivo es ofrecer una plataforma donde arrendadores puedan publicar y administrar propiedades, y donde arrendatarios puedan consultar la oferta disponible.

**Características principales (H4 / H4B - hitos anteriores)**  
1. **Autenticación completa**:  
   - Registro de usuarios.  
   - Inicio y cierre de sesión (con protección CSRF, cierre solo por POST).  
   - Perfil de usuario con datos básicos y opción de edición.  

2. **Gestión de inmuebles (CRUD con ORM)**:  
   - Crear, editar y eliminar inmuebles (arrendadores).  
   - Listar inmuebles disponibles (arrendatarios).  
   - Uso explícito del ORM de Django en todas las operaciones (insert, update, delete, select).

3. **Administración de permisos y grupos**:  
   - Arrendadores con permisos de gestión.  
   - Arrendatarios con permisos de visualización.  
   - Uso del panel de administración para validar roles y permisos.

**Hito 5 – Extensión de funcionalidades**  
- Se implementó un filtrado de la oferta por **comuna** y por **región**, accesible vía parámetros en la URL o mediante formulario simple.  
- El servidor se ejecuta en entorno Codespaces, permitiendo navegar de forma pública por las funcionalidades.  
- Durante la demo se muestran:  
  - El flujo de registro/login.  
  - Acceso al perfil y edición de datos.  
  - Visualización de oferta pública filtrada.  
  - Gestión completa (crear/editar/eliminar) desde la vista de arrendadores.  

**Cierre**  
El sistema cumple con los requerimientos de autenticación, gestión de datos con ORM y presentación en vivo.  
Como trabajo futuro se podría:  
- Añadir el campo `owner` en `Inmueble` para asociar inmuebles a cada usuario.  
- Implementar paginación y filtros avanzados con formularios select.  




----

##Rutas principales##

- **Inicio**: `/`  
- **Login**: `/accounts/login/`  
- **Registro**: `/accounts/register/`  
- **Perfil**: `/accounts/profile/`  
- **Editar perfil**: `/accounts/profile/editar/`  
- **Oferta pública**: `/inmuebles/oferta/`  
- **Filtrar por comuna/región**: `/inmuebles/oferta/?comuna=1&region=1`  
- **Gestión arrendadores**: `/inmuebles/gestionar/`  
- **Crear inmueble**: `/inmuebles/nuevo/`  
- **Editar inmueble**: `/inmuebles/<id>/editar/`  
- **Eliminar inmueble**: `/inmuebles/<id>/eliminar/` 