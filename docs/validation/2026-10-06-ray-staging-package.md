# Ray: paquete y calificación de staging

Fecha: 6 de octubre de 2026. El candidato público permanece en **1.0.0**, sin envío a revisión. El piloto privado existente se actualizó mediante la subida manual de ChatGPT a **1.1.5**, conservando su identidad, audiencia personal y conexión de staging. No hay promoción de producción.

## Ficha y activos

- Nombre visible del piloto y su conexión: **Braking Lab - Race Engineer · Staging**. El candidato público usa **Braking Lab - Race Engineer**.
- La descripción cubre preparación, telemetría, coaching, setups, estrategia, notas y entrenamiento. La UI muestra evidencia; la conversación permanece en ChatGPT.
- Logo e icono del compositor: `assets/braking-lab-isotype.png`, copia byte a byte del icono canónico de Capture (`apps/capture/src-tauri/icons/icon.png`), PNG RGBA de 512 × 512 px y 9.813 bytes; color de marca `#FA5F29`. Es la geometría v5 compartida con la SPA. Los manifests principal y de compatibilidad declaran expresamente los paths; 1.1.5 incluye también `logoDark` y `composerIconDark`.
- Web, soporte, privacidad y términos existentes fueron verificados por HTTP y contenido esperado. Se conservan los tres prompts iniciales, diez skills y binding canónico.
- No hay checkout integrado. Las funciones dependen de los permisos de la cuenta conectada y los enlaces de membresía abren Braking Lab.

El ZIP privado contiene la conexión existente y permanece fuera de GitHub y del directorio. Los paquetes públicos portable/Claude no contienen bindings privados, credenciales ni datos del reviewer.

La cabecera de la UI real muestra el isotipo nuevo y **BRAKING LAB - RAY**. La ficha del plugin sigue mostrando el SVG amarillo genérico de ChatGPT. La subida manual de 1.1.4 registró URLs oficiales de los activos; 1.1.5 guardó las variantes oscuras en la release `pluginrel_6ac4ec23cff4819186849fe7f3d99bff`, pero ninguna cambió ese renderizado. No se declara arreglado el icono visible ni se generan versiones especulativas.

El portal de OpenAI tenía la sesión invalidada. Tras la recuperación normal y la verificación de identidad, se inspeccionaron los catálogos de las organizaciones existentes: el piloto privado no aparece allí. Su enlace de gestión devuelve «Plugin not found in this organization». Se restauró el ámbito original; la organización rbart ventures figura como **Verified** para poder presentar apps de ChatGPT. No se creó otro plugin ni se sustituyó su propiedad, audiencia o conexión para intentar cambiar el icono.

## Contrato y empaquetado

Los snapshots públicos se exportaron desde el commit limpio `3c06e08622f48a9b2e71847d901d426c79d8b5a3`. El catálogo de dominio permanece en `101-ed5a84b844b4a006`, con 101 operaciones, 110 herramientas typed y `execute_code`: 111 herramientas en total. `ray_evidence` descubre `selection` opcional.

El constructor privado admite una versión estable explícita y rechaza versiones no canónicas, iguales e inferiores. Conserva conexión y prompts; no inventa un binding de producción. Pasaron 32 tests de contratos/metadatos/archivos, schema de paquete/MCP, diez skills mediante Agent Skills, referencias de dominio/Ray, Strict Claude, generación reproducible y URLs públicas. Estos checks no certifican el host real.

## Despliegues y prueba del host

PR 128 corrigió título, discovery y recuperación de hashes antiguos. PR 130 corrigió el refresco simultáneo de cinco lecturas y la declaración SDK de modos de visualización. Su despliegue `8d9b28bacad42d7590375258bea68cf0efe8bb3b` pasó calificación autenticada, pero la página global seguía en presentación compacta: el host informaba inline sin fullscreen disponible.

PR 131 pasó CI `37465889638` y se integró en `develop` como `77c56017901dabcfbf379db709a6c5bbcc01944c`. Railway deployment `1e532fe6-3488-4137-aa12-897b321bcc88` alcanzó `SUCCESS`; health identifica ese commit y readiness pasa. La calificación autenticada confirmó:

- Source hash `1c5a2e90edf98f69c930dbb61d5ddffa6c5eff26b62200e366d825af4f28f9d8` y contrato de dominio inalterado `ff45dba8bb5ff278a9e2dac22722802a5aa6f49fa2b3ebd342aa726669b06ea2`.
- 111 herramientas, identidad propia y hints separados: presentación global `workspace`, evidencia de hilo `inline`.
- HTML actual con digest `8411f4d7be509c484870f5caa9b3a4b5871a434478aacb1abd1716c0a0cd77b6` y alias legacy con HTTP 200. Un hash obsoleto devuelve 400/-32002; nunca sustituye otro artefacto bajo ese hash.
- Revocación exacta del grant temporal del reviewer al terminar.

El propietario completó OAuth en su navegador. Desde ajustes de ChatGPT se renovaron las herramientas y se abrió la conexión canónica. La prueba real confirmó el workspace completo y recorrió resumen, preparación, notas, telemetría, coaching, setups, estrategia y entrenamiento. La cuenta conectada devolvió sesiones, carreras, blocs, setups y ejercicios. Se revisaron una sesión con vueltas, trazas y comparación; un checklist de carrera; notas de curva; parámetros de una versión propia; y los estados sin coaching, asociaciones, prácticas vinculadas o estrategia guardada. El refresco de permisos terminó y conservó el workspace. No se guardaron mutaciones de dominio durante ese recorrido.

PR 131 incluye 237 tests de Ray y siete tests focalizados de bootstrap. CI también pasó MCP, tipos/lint, Docker y el harness PostgreSQL de Capture. Una página global es independiente del modo fullscreen del host; el hint solo controla el contenido del iframe, sin conceder capacidades, permisos o consentimiento.

## Fallos encontrados y siguiente corrección

La prueba de **Preguntar a Ray** desde la página global devolvió `MCP app messages require an available composer`. PR 133 corrige el destino con la extensión OpenAI de mensaje: página global/archivo → conversación nueva; evidencia de hilo, incluso fullscreen → conversación activa. Las preguntas nuevas incluyen solo identificadores de evidencia seleccionada, conservan autorización por propietario y no suponen consentimiento de escritura. Los envíos fallidos no se reintentan en otro destino.

PR 133 también localiza `ready`, corrige «1 versiones» y sustituye términos internos de almacenamiento en la explicación de notas. Pasaron tipos/lint/formato/build y 243 tests de Ray, incluidos destinos, contexto privado, cambio de propietario, extensión ausente y fallo de envío sin duplicación. Tipos/lint/formato del MCP pasan. CI `37468746109` pasó y se integró en `develop` como `a4a512f6fea5501c83929cc577325a21cd098b74`. La calificación autenticada del deployment `1a36ade4-1a10-4e60-8e30-98008d91e2a2` pasó con source hash `29a2c954e6ddc8087e3f81875b4545d76dbffb47098c544613e434964bd62449`, contrato de dominio inalterado y UI digest `227b8048ad0787a3450b0f3660ac57a8128ecca0b7ee8f82b732d662e4374ac4`. Recursos actual/legacy devuelven 200 y hashes obsoletos 400/-32002. Se revocó el grant temporal exacto. La acción global «Preguntar a Ray por dónde empezar» creó una conversación nueva visible en Inicio, «Elegir próxima tarea». Se abrió y se comprobó la respuesta con lecturas reales de la cuenta, sesiones, setups y ejercicios; no hubo escrituras. La pestaña global no navega al chat nuevo. El host retiró su model context después del envío, aunque el chat sí se creó: el aviso actual de contexto retirado necesita interpretarse con ese comportamiento. El agente informó de un rechazo inicial de concurrencia y se recuperó agrupando lecturas; no se afirma ausencia total de contención para consultas generadas por el agente.

Una segunda pregunta desde una sesión seleccionada creó otro chat y conservó la referencia. ChatGPT pausó después una lectura `execute_code` con aprobación nativa y un aviso de «instrucción sospechosa» sobre reglas de flujo de análisis, saludo, persistencia y cuenta/cuota. La aprobación quedó pendiente en esa primera observación; su desenlace está registrado en el seguimiento final. No era un rechazo automático ni una prueba final de debrief. El diálogo no mostró el código completo. Debe revisarse este comportamiento para publicación sin retirar restricciones de consentimiento o permisos.

La comparación de dos vueltas históricas mostró un delta intermedio grande y zonas con posiciones repetidas. Esto queda como observación para revisar la calidad de la captura/alineación; no prueba por sí solo su causa ni valida la comparación como evidencia medida fiable. Los identificadores antiguos de coche/circuito en setups tampoco se convierten en identidades exactas por mostrarlos con otro nombre.

La capacidad de viewport del navegador de pruebas no cambió la anchura DOM observada al pedir 390 px; se retiró el override. Ese intento no certifica responsive móvil ni la app nativa de ChatGPT. La aceptación móvil sigue pendiente.

## Limpieza y documentación para clientes

Plugin Management retiró la conexión anterior **Braking Lab Race Engineer**; la lectura fresca de instaladas confirmó que ya no figura. La conexión canónica de staging permanece habilitada y se renombró por la UI sin cambiar su ID, endpoint o cuenta. El plugin privado y su dependencia MCP son dos entradas necesarias, no duplicados que deban eliminarse.

La lectura del plugin privado legacy 0.3.2 confirma que apunta a esa conexión retirada y usa activos anteriores. Su desinstalación exacta se completó con Plugin Management y la barra lateral de instalados confirmó su ausencia. Permanecen el plugin final y su dependencia MCP. No se alteraron plugins ajenos al proyecto ni se creó una conexión de producción.

El descriptor «Mi Paddock» visto anteriormente era obsoleto; la renovación en el navegador correcto ya permitió cargar el recurso actual. La guía para SPA/Capture es `apps/mcp-server/docs/ray-client-integration.md`. No cambia el contrato de dominio, OAuth, scopes, cuotas ni payloads de SPA/Capture; estos clientes no necesitan migración. La restauración de una comparación completa en la SPA necesitaría un contrato adicional explícito.

## Gates de publicación pendientes

El reviewer de staging es Franz Hermann, sin administrador, con contenido persistente de prueba. Sus trazas LMU y sus imports iRacing tienen procedencias separadas: no se afirma que esos setups se condujeron en esas vueltas. La prueba de nueve hitos del reviewer verifica lecturas, aislamiento y contratos; los ocho casos dentro del host correcto y consentimiento nativo siguen pendientes. Credenciales y grants permanecen privados.

`verify_submission.py --ready` bloquea mientras no exista una URL real del vídeo. También quedan el buzón controlado del reviewer, aceptación del propietario y móvil, calificación de producción tras promoción autorizada y campos/atestaciones del portal. Ningún registro local equivale a aprobación de OpenAI.

## Seguimiento de la prueba real

El debrief seleccionado terminó después de aprobar una lectura puntual del host,
sin habilitar permisos persistentes. La respuesta reconoció la población pequeña,
la ausencia de una referencia comparable y magnitudes físicamente anómalas de
la captura. No se guardó un informe ni se modificaron registros. Esto acredita
el traspaso de selección y la lectura del agente, no la fiabilidad metrológica de
esas vueltas históricas ni la aprobación de una escritura.

PR 140 convierte el bloque de órdenes conversacionales de `execute_code` en un
contrato factual de permisos, efectos y límites. La lectura no obliga a guardar
un informe; los límites compartidos de concurrencia se distinguen del presupuesto
por ejecución y un rechazo no cancela llamadas hermanas. La persona de Ray y las
comprobaciones servidoras de autorización y consentimiento permanecen. La UI
indica cuándo una pregunta se ha enviado a un chat nuevo y cómo continuar desde
Inicio. Pasan 77 tests focalizados de MCP y 243 de Ray, tipos/lint/formato y build.
CI `37490245422` completó todos los checks y Railway deployment
`5cef4202-a4f2-4edd-8423-1bad0231a3d9` alcanzó SUCCESS con commit
`b4ffbfaeef5b2de5354224105fec788615a8bd4c`. Source hash
`bce9c5d7b7ce93a687f477765af599f04b2d3c3a845abe78e744e006ea02b189`,
contrato de dominio inalterado y UI digest
`607f15f745d1611b4699f65602c68df920b3869f0b3922a8270e6e0bced5c1ab`.
La prueba autenticada de nueve hitos pasa: identidad, permisos, trazas,
comparación propia, parentage de versiones, rechazo de parámetros y propietario
ajeno, openers y HTML. Recursos actual/legacy devuelven 200; hashes obsoletos
400/-32002. Un primer initialize agotó su espera; las siguientes pruebas de
lecturas y recursos pasaron. Todos los grants exactos se revocaron, incluido
el del intento fallido. No se atribuye una causa sin evidencia.

Tras renovar las herramientas, la UI real cargó y «Preguntar a Ray» desde una
sesión creó la conversación «Debrief de sesión». El aviso español explica
correctamente que se debe abrir Inicio para continuar. El host restableció la
UI al resumen tras el envío; no hubo navegación ni reintento automático.
El agente volvió a encontrar contención al agrupar lecturas y reintentó
secuencialmente. El host sigue mostrando un aviso de instrucción sospechosa
sobre la descripción de execute_code. La ausencia de ese aviso no se declara
validada y las comprobaciones de permisos no se retiran para silenciarlo.

La respuesta anterior también consumió la consistencia legacy agrupada por
ordinales de zona. Esa métrica necesita revisión de su política de calidad
antes de aceptar resultados como evidencia medida para producción; reconocer
anomalías en el texto no valida el algoritmo.

La nueva conversación completó el debrief tras aprobación nativa de una lectura
puntual. Verificó propietario y selección, rechazó interpretar la población
pequeña/anómala como consistencia establecida y declaró no haber guardado ni
modificado nada. No se aceptó su propuesta de guardar. El descriptor factual
actual también se comprobó mediante tools/list autenticado: el aviso del host
sigue siendo una incidencia reproducible, no un caso resuelto. No se concedieron
permisos persistentes ni se eludió el clasificador.
