# Ray: ficha privada y paquete de staging

Fecha: 6 de octubre de 2026. El candidato público permanece en **1.0.0**, sin envío a revisión. El piloto privado existente se actualizó mediante Plugin Creator a **1.1.0**, conservando su identidad, audiencia personal privada y conexión de staging.

## Ficha y activos

- Nombre visible: **Braking Lab - Ray · Staging**. El candidato público usa **Braking Lab - Ray**.
- Descripción: ingeniero de pista para preparación, telemetría, coaching, setups, estrategia, notas y entrenamiento. La UI muestra evidencia y la conversación permanece en el host.
- Logo e icono del compositor: isotipo existente `assets/braking-lab-v5.png`, PNG RGBA de 512 × 512 px; color de marca `#FA5F29`. No se añade la firma manuscrita descartada.
- Web, soporte, privacidad y términos: enlaces existentes verificados con HTTP y contenido esperado.
- Se mantienen el tipo, texto y orden de los tres prompts iniciales, las diez skills y la conexión existente. La lectura de la fuente guardada confirma estos valores y el overlay legacy sincronizado.
- No se incorpora checkout ni promoción de upgrade. Las funciones siguen los permisos existentes de la cuenta.

La actualización privada no cambia permisos ni comparte el plugin con terceros. Su ZIP contiene el binding original y **no** se publica en GitHub ni se envía al directorio. Los paquetes públicos portable/Claude siguen libres de bindings privados, credenciales y datos del reviewer.

## Contrato y controles

Los snapshots se exportaron desde el commit limpio del monorepo `3c06e08622f48a9b2e71847d901d426c79d8b5a3`. El catálogo de dominio sigue en `101-ed5a84b844b4a006`; el opener `ray_evidence` ahora descubre el campo opcional `selection`. Hay 101 operaciones de dominio y 110 herramientas typed, además de `execute_code`.

El constructor privado acepta una versión estable explícita y rechaza valores no canónicos, versiones iguales e inferiores. Conserva la conexión exacta y los prompts; no infiere un binding de producción. La documentación de mantenimiento describe la lectura previa y la protección mediante release esperado.

Validaciones completadas: **32 tests** de contratos, metadatos y archivos; schema de paquete/MCP; diez skills mediante Agent Skills; referencias de dominio/Ray; Strict Claude; generación de archivos reproducibles y URLs públicas. La revisión posterior comprobó identidad, prompts, audiencia, mapping y límites de distribución. No se detectaron bloqueos en el cambio de empaquetado.

## Lo que esta evidencia no certifica

La lectura posterior de Plugin Creator confirma una release guardada, no el renderizado de la UI. El navegador de ChatGPT disponible no pudo cargar el enlace del piloto y su pestaña Personal no lo mostró; no se inventa una causa ni se declara denegado el acceso de edición, que sí funcionó mediante el backend.

La UI integrada y el nuevo opener necesitan la calificación propia del despliegue de octubre 6 y aceptación en ChatGPT escritorio/móvil. El registro de octubre 5 es histórico. La guía de integración del monorepo está en `apps/mcp-server/docs/ray-client-integration.md`: SPA y Capture no requieren migrar payloads por este cambio; restaurar una comparación completa en la SPA necesitaría un contrato adicional explícito.

El reviewer de staging es Franz Hermann, sin administrador y con contenido de prueba persistente. Sus trazas LMU y sus imports iRacing son fuentes separadas; no se afirma que esos setups se condujeron en esas vueltas. No se ha copiado telemetría del propietario porque su perfil de staging no tenía sesiones disponibles. Las credenciales permanecen en archivos privados con permisos 0600.

`verify_submission.py --ready` sigue bloqueando por la ausencia de una URL real de vídeo. También permanecen abiertos el buzón controlado del reviewer, la aceptación del propietario, la promoción y calificación de producción y los campos/atestaciones del portal. Ningún registro local equivale a aprobación de OpenAI.

## Lecciones del pase

Separar las versiones del piloto privado y el candidato público evita distribuir una conexión personal como una ficha pública. Una actualización del MCP no actualiza automáticamente los metadatos del plugin: hay que guardar una nueva release y leerla de nuevo. Los checks de empaquetado y la calificación del host son gates distintos; conservar esa distinción permite avanzar sin afirmar una integración todavía no observada.
