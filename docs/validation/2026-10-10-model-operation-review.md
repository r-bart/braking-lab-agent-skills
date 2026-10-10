# Modelo de operaciones — candidato MCP 0.5.2

El escaneo inicial del borrador público 1.0.0, conectado por OAuth a Franz Hermann, descubrió el MCP de producción 0.5.1 y señaló cinco herramientas: `execute_code`, `ray_updatePreparationPhase`, `ray_updateChecklistItem`, `ray_confirmSetupUsage` y `ray_getFunctionSchema`. El dominio figura verificado. Las credenciales de reviewer se guardaron en los campos privados de OpenAI con autorización explícita del propietario; no se incluyen aquí ni en el ZIP. El portal conserva cinco casos positivos, tres negativos y la URL del vídeo. No hay envío ni publicación.

Los snapshots se reexportaron del commit limpio de staging `c58cd673c521a247f38f78b530ba7b2b86c76b8c`. Catálogo canónico sin cambios: `101-ed5a84b844b4a006`, 101 funciones. Superficie nueva: 117 herramientas typed, 118 contando el executor compatible. Los cuatro mirrors de compatibilidad y el executor declaran visibilidad app-only. Siete aliases de preparación ofrecen una acción fija con esquema estricto y reutilizan autorización, ownership, dispatcher y requisitos de consentimiento existentes. La metadata de audiencia no constituye autorización.

Las diez skills usan los esquemas de las herramientas ofrecidas al modelo y reservan la introspección para Code Mode compatible. La skill `race-week` nombra esas siete acciones y exige lectura después de un toggle incierto. El verificador admite únicamente las cuatro excepciones app-only y exige las aliases, sus campos requeridos exactos, la política de reintento y la ausencia del selector `action`. Conserva el rechazo de ocultar herramientas de lectura o confirmación. Siete nuevos tests cubren deriva de esa superficie.

Validación local del paquete: diez skills válidas; 73 referencias canónicas y 15 referencias `ray_*` verificadas; 39 pruebas pasan; metadata y cuatro URLs públicas verificadas; archivos deterministas y SHA-256 correctos; Claude strict validation pasa. El ZIP nuevo conserva `Braking Lab` y `braking-lab-race-engineer`, y su SHA-256 es `76ae645282ef0e0e5c5169fc5d7e5a87944931f77988e445d97b741e0cc12a1e`. Este fue el candidato preparado antes del despliegue; la comprobación final del paquete guardado se registra abajo.

La fuente MCP del parche pasa typecheck, lint, formato, build y 4.134 pruebas herméticas (una skipped, tres todo). Su integración de staging pasa además 66 pruebas focalizadas y build. Estos fueron los resultados previos a despliegue; la integración, cualificación y el nuevo escaneo se registran abajo. Estos resultados no acreditan los ocho recorridos nativos sobre el paquete público exacto ni el consentimiento final de publicación.

## Despliegue y comprobación de staging

La CI 38085607155 pasó completa y PR 150 se integró en develop `bd4bc9da7c2dbe82f9c813d2436d4a4bdad5bf2b`, con ventana libre autorizada. Railway `e02b5e01-d369-430f-b48f-b2c0a774b229` sirve MCP 0.5.2; el hash de fuente es `ea34fe3b03d8b8123869c14c1396b6e75c25b537885f6ab0c535a80dac6e9bc0`. La prueba autenticada pasó 12 bloques: identidad exacta, las 117 descripciones typed, audience app-only del executor, rechazo de las siete aliases con scope read, bootstrap/membresía, trazas y comparaciones propias, setups y padre incorrecto, contratos estrictos de opener, rechazo de otro propietario, aperturas de tareas y preferencias, conservación tras escritura rechazada y recurso UI ligado a su hash. No hubo cambios de contenido. Se revocó únicamente el grant temporal creado para la prueba. El recorrido no acredita renderizado nativo.

La CI 38085957959 también pasó completa y PR 151 se integró selectivamente en main `0e058c9a51d8551d0d811bca372a82620ecc4c3b`. La promoción inició Railway `3bcfa986-720d-40cf-8d23-cb578208a67c`; su resultado y la cualificación se registran en la sección siguiente. No se ha desplegado SPA, Capture o Landing ni aplicado migraciones.

El borrador público no está instalado y ChatGPT devuelve «Plugin not found» al abrir su ficha. El portal solo ofrece acciones de conexión/escaneo y descarga, sin control de prueba nativa. Esto es una limitación observada de acceso, no un fallo demostrado de Ray; los ocho casos del paquete público exacto siguen sin aceptación nativa. No crear una conexión duplicada ni presentar el ensayo de desarrollo como esa aceptación.

## Comprobación de producción

Railway `3bcfa986-720d-40cf-8d23-cb578208a67c` terminó en SUCCESS y sirve MCP 0.5.2 desde main `0e058c9a51d8551d0d811bca372a82620ecc4c3b`. La comprobación autenticada con Franz pasó identidad, readiness, discovery OAuth, grant de solo lectura, UserInfo verificado, sesión Streamable HTTP, las 117 descripciones typed exactas, las siete escrituras rechazadas por scope, bootstrap, recurso UI ligado a su hash, rotación de refresh y rechazo después de revocar únicamente el grant temporal. No se hicieron cambios de contenido ni se simularon aprobaciones de usuario. El reescaneo del borrador público se registra como comprobación independiente en la sección siguiente.

## Paquete guardado y resultado del portal

Se subió el ZIP `76ae645282ef0e0e5c5169fc5d7e5a87944931f77988e445d97b741e0cc12a1e` al borrador existente `appsub_6aca9fc11f60819191bfca3756c086e2`, manteniendo una sola conexión de producción. El dominio figura verificado y OAuth autorizado. El nuevo escaneo del MCP 0.5.2 terminó con «No findings in the latest MCP scan». Las diez skills muestran «Checks passed». Permanece únicamente el aviso no bloqueante sobre la categoría Productivity.

El ZIP descargado del portal tiene SHA-256 `5ce55b38da54cf34c2b7de370d6475cff29767597c111c560cda3ac5b0d273c3`; el contenedor ZIP se regeneró, pero los diez archivos SKILL.md y el isotipo son idénticos byte a byte al upload, y plugin.json/mcp.json son estructuralmente idénticos. El isotipo nuevo de 512 px aparece en la ficha y el publicador visible sigue siendo Braking Lab, sin nombre personal completo.

Se comprobaron de nuevo los campos privados de reviewer tras el reupload: login, cuenta dedicada, contraseña presente sin exposición y pasos de acceso. Cinco casos positivos y tres negativos figuran completos. Países: todos los admitidos; traducción: español; vídeo y notas de versión conservados. Estas verificaciones de presencia no acreditan ejecución nativa de los ocho casos.

## Puerta del publicador

El diálogo final permite abrir Submit for review y muestra seis declaraciones sin marcar: términos y guías de OpenAI, leyes aplicables, ausencia de transferencias/inversiones, derechos sobre contenido y endpoints, aptitud para menores de 18 y no dirigirse a menores de 13 ni compartir sus datos. El botón Submit permanece deshabilitado. La skill de preparación exige que las complete el publicador autorizado; se dejó el diálogo preparado para el titular, sin marcar casillas ni presentar el borrador. La prueba nativa exacta sigue pendiente independientemente de esas declaraciones.
