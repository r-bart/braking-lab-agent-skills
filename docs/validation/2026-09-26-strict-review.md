# Revisión estricta — distribución privada

**Fecha:** 2026-09-26  
**Base revisada:** `468a0b1` y los cambios editoriales de esta revisión  
**Alcance:** README EN/ES, guías de instalación, paquetes, documentación de distribución y enlaces de la landing v4 prototípica.

## Requisitos y evidencia

| Criterio                                      | Resultado                           | Evidencia                                                                                                                                                                                                                          |
| --------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Una fuente de nueve skills y tres paquetes    | Cumple                              | `scripts/verify_package.py`, `scripts/build_archive.py` y checksums pasaron tras la revisión.                                                                                                                                      |
| README comprensible para un piloto            | Corregido                           | Los dos README indican acceso privado, ruta de instalación y límites comprobados.                                                                                                                                                  |
| Guías que conducen al archivo instalable      | Corregido                           | Claude chat, ChatGPT y paquete portable enlazan a los ZIP de la release; `dist/` no se publica en Git.                                                                                                                             |
| README dentro del ZIP                         | Corregido para el siguiente paquete | El ZIP incluía un README con enlaces relativos a documentos ausentes. El generador deja el README completo en el repositorio y empaqueta solo los archivos que carga el cliente. La release `v0.1.0` conserva el paquete anterior. |
| Enlace desde la landing v4 a este repositorio | No existe                           | La página prototípica de Race Engineer dirige sus CTA a la app y a `/docs/race-engineer/mcp-setup`; no enlaza a GitHub ni a una ficha pública de plugin.                                                                           |
| Pruebas completas para publicación            | Pendiente                           | Faltan el corpus de selección, integración de staging, escrituras, confirmaciones, otra cuenta de ChatGPT y primera respuesta en Claude.                                                                                           |
| Preparación del envío público de OpenAI       | Pendiente                           | El portal requiere envío **With MCP** directo, verificación de dominio y soporte OAuth adicional. El ID de app personal solo sirve para el piloto.                                                                                 |
| Licencia y política de fuente pública         | Pendiente                           | El repositorio no tiene licencia. Hace falta una decisión explícita antes de ofrecer el código como proyecto público reutilizable.                                                                                                 |

## Comprobaciones

- Validación de los nueve directorios Agent Skills y esquemas de los manifiestos: correcta.
- Construcción de los tres ZIP y `SHA256SUMS`: correcta. Cada ZIP contiene una sola vía de conexión MCP.
- Prettier y `git diff --check` en los archivos modificados: correctos.
- Enlaces locales de los once archivos Markdown del repositorio: ninguno apunta a un archivo ausente.
- Las rutas web de seguridad EN/ES y la página de producto respondieron `200`. Un acceso HTTP sin credenciales al ZIP privado de GitHub respondió `404`, coherente con la visibilidad privada; el asset existe en la release consultada con GitHub CLI autenticado.
- Análisis de 154 objetos Git alcanzables: no encontró patrones de credenciales, rutas locales del propietario ni direcciones de correo. No sustituye una revisión de contenido y licencia antes de abrir el repositorio.
- No se modificó la landing v4: su árbol de trabajo contiene cambios de otra tarea que deben conservarse.

## Juicio estricto

**Piloto privado: aprobado con límites visibles. Publicación abierta: cambios requeridos.** El caso más probable de fallo es intentar instalar el ZIP de ChatGPT desde otra cuenta: solo se comprobó con la cuenta que registró la app personal. Si falla, revisar primero el estado de la conexión en la ficha del cliente y los registros OAuth del servidor sin guardar tokens ni datos de conducción en este repo. Con más tiempo, probaría una cuenta ajena y automatizaría un caso de instalación limpia por plataforma antes de escribir enlaces públicos en la landing.

El repositorio sigue **privado**. La landing no necesita acceso público a él para sus enlaces actuales. Cuando existan fichas públicas verificadas, la landing debe enlazar a esas fichas o a una página de instalación pública revisada, según el [plan de distribución](../distribution-plan.md).
