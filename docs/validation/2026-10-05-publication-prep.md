# Plugin v1 — preparación y calificación de staging

Fecha: 2026-10-05. Evolución del MCP, OAuth, Ray Paddock y diez skills existentes. Candidato público 1.0.0; MCP 0.5.1. Publicación y producción esperan aceptación del propietario.

## Fuente y distribución

Los snapshots de contrato se exportaron del commit limpio `ecbd42366fe2a59386946ae8171d156b36a61b1f` del monorepo, integrado en `develop` por PR 124 (evolución de PR 123). Catálogo `101-ed5a84b844b4a006`: 101 operaciones y 110 herramientas typed. Cada operación de dominio es visible para app/model y declara readOnlyHint/destructiveHint/openWorldHint; se conservan permisos, scopes y elicitación directa.

El ZIP portable público contiene `mcp.json` de producción; Claude contiene `.mcp.json`. Ambos contienen los diez skills y ningún binding privado de app, hooks, credenciales, fixtures o documento interno. La reproducción determinista y los límites de empaquetado tienen pruebas. `verify_submission.py --ready` exige una URL real de vídeo y sigue fallando hasta que exista; el verificador no pretende certificar comportamiento ni aprobación.

El piloto privado existente se actualizó mediante Plugin Creator a 1.0.0. La lectura posterior confirmó el release nuevo, la conexión de staging, los diez skills, los prompts, el overlay legacy y la audiencia USER/PRIVATE. El paquete privado no se distribuye como submission público ni su identificador de app se guarda en Git.

## Evidencia del servidor real

Primera calificación: Railway deployment `ed77a0a4-1945-4e87-862a-6ce207527da1`, commit `22e1867ae95bb91b23c2c5e5c6d159460624d3e7`, MCP 0.5.1. `/health` confirmó esa identidad. La migración de scopes se aplicó únicamente en staging, conservando los 46 grants anteriores.

Una ejecución de aceptación de 151 segundos contra el MCP y Supabase de staging pasó veinte hitos: discovery; identidad verificada y UserInfo con permisos exclusivamente de identidad; DCR/S256 PKCE/resource/issuer/code replay; Bearer obligatorio; capacidades de sesión; bootstrap del calendario; aislamiento de dueño y sesión; límites de read/write; rotación y revocación; reconexión; recuperación del mismo successor dentro de la gracia existente de 15 segundos; revocación tras reutilización fuera de gracia; rechazo/cancelación/ausencia de capacidades; aborto del cliente; deadline del servidor; limpieza verificada.

Se usaron dos cuentas sintéticas efímeras por ejecución. Nunca se aceptó una asociación de setup, subió un objeto ni invocó un modelo de pago. Las dos ejecuciones preliminares con expectativa de refresh desactualizada se reconciliaron por IDs exactos, verificando antes identidad sintética y ausencia de objetos; sus usuarios se eliminaron y no se reintentó ningún write sensible. El gate de AI Setup se pausó durante cada ejecución y se restauró a su valor original. Los errores exponen códigos estables, no mensajes privados de proveedores.

## Evidencia del cliente

ChatGPT mostró versión 1.0.0, diez skills y la conexión existente. El primer intento de apertura dijo App unavailable. Tras actualizar el catálogo de la app, se observó el Paddock realmente renderizado en fullscreen con la cuenta Basic sintética ya conectada, identidad, navegación ES y ausencia honesta de telemetría. Una respuesta del opener por sí sola no se contó como renderizado.

La apertura del diálogo de preferencias detectó una incompatibilidad: nativeSettingsRead usa la respuesta Extensions sin el envelope ordinario de Ray. Se corrigió solo ese contrato validado; errores, datos inválidos y herramientas de dominio no pueden omitir success. Se añadió una prueba con los formatos nativo y legacy. La guía de UI exige origen dedicado; el recurso ahora declara el origen propio del MCP y solo el destino externo de la app configurada, manteniendo cerrado CSP de red y frames.

El despliegue integrado final `58eb2c5e-d2c9-41c1-97ca-13724f1fc9a4`, commit `b2591a500b85d5a0de82f06bf87c42f49bfbcf9e`, se completó correctamente. La aceptación real se repitió sobre esa identidad: los veinte hitos pasaron en 151 segundos, incluida la limpieza de las cuentas efímeras. Se restauró el gate original después de finalizar. El MCP autenticado confirma entorno staging, versión 0.5.1, catálogo `101-ed5a84b844b4a006`, sourceHash `6fea25f9013ebce694b1b9ce4842a2bffb8eca3eb09477e72097b99b5ce31458` y contractHash `ff45dba8bb5ff278a9e2dac22722802a5aa6f49fa2b3ebd342aa726669b06ea2`.

En ChatGPT, tras refrescar el catálogo, el recurso final se renderizó bajo el origen dedicado de staging. El Paddock mostró la identidad y última sesión de una cuenta de staging ya conectada; abrir Preferencias mostró correctamente idioma, unidades y densidad, sin modificar sus valores. No se guarda ninguna identidad de cuenta en este informe. No se han ejecutado todavía los cinco casos positivos y tres negativos públicos con la cuenta exclusiva del reviewer.

## Revisión profunda de UI

La revisión solicitada aplicó las skills de Emil pertinentes a UI, accesibilidad, formularios, móvil, tipografía, color, superficies, estados, rendimiento y movimiento. Se mantuvo la marca y se priorizaron última sesión/próxima carrera; cuenta y cuotas quedan plegables. Se corrigieron edición rápida de arrays, paginación, validación previa, recuperación de contratos y cursor de telemetría. El informe completo con post-review vive en el monorepo: `thoughts/reviews/2026-10-05_ray-ui-deep-review.md`.

Se probaron las seis áreas a 320 px, nombres extremos sin overflow horizontal, vacío/lectura fallida, preferencias y sus focos (incluido Retry), y las tres páginas de 41 notas y 41 ejercicios con Next desactivado al final. La captura de escritorio usa datos sintéticos de un fixture local; no se presenta como telemetría real. La revisión visual del nuevo build dentro de ChatGPT, Safari/iPhone físico, lector de pantalla y rendimiento móvil físico siguen pendientes de aceptación.

Railway construye el rediseño desde PR 124; la calificación del build anterior descrita arriba no demuestra por sí sola aceptación del nuevo recurso UI.

## Controles locales

- MCP: tipos, lint y build pasan. Suite final: 4.088 pruebas pasan en 331 archivos; una skipped y tres todo existentes. Las 26 pruebas focalizadas de recurso, registro y transporte también pasan.
- UI Ray final: tipos, lint, format, build y 94 pruebas en 14 archivos pasan. HTML 984,68 kB; nueve pruebas focalizadas de recurso/registro MCP pasan después del rediseño.
- SPA: tipos, lint, build, cuatro pruebas de consentimiento y consistencia EN/ES pasan.
- SQL: ocho fixtures sobre migraciones canónicas con PGlite y fixture real en PostgreSQL 16.9 pasan.
- Paquete: 31 pruebas de contratos, metadatos y archivos reproducibles pasan; diez skills válidos, 74 referencias de dominio y siete referencias Ray explícitas verificadas. Strict Claude valida el marketplace y el manifiesto directo; el smoke del instalador 1.0.0 pasa. URLs públicas de web, soporte, privacidad y términos responden correctamente.
- Los workflows del monorepo siguen pending/queued en GitHub; no se presentan como aprobados. Las previews del candidato y el build integrado de la SPA en Vercel están aprobados; Railway integrado está aprobado. El build integrado de landing seguía pendiente al registrar esta comprobación.

## Trabajo abierto

Aceptación del propietario en staging; cuenta exclusiva con contenido ficticio; grabación real y URL del vídeo; promoción selectiva y migración aprobada de producción; identidad pública verificada que permita OpenAI; token real de verificación de dominio; nuevo borrador With MCP, rescan y review. Todos los países; sin checkout ni promoción de compras. Ver [fixtures](../reviewer-fixtures.md), [guion](../demo-walkthrough.md) y [submission](../openai-submission-draft.md).
