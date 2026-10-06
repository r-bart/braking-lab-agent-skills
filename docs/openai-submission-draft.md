# Preparación del envío público a OpenAI — 1.0.0

Actualización del 6 de octubre: la ficha privada es **Braking Lab - Ray · Staging 1.1.0**, con logo, diez skills y conexión existentes conservados. La UI y el contrato de selección de octubre 6 esperan su despliegue y aceptación propios; el registro anterior que sigue es histórico. Ver [montaje de staging](validation/2026-10-06-ray-staging-package.md).

Estado histórico a 5 de octubre de 2026: candidato preparado, **todavía no enviable**. El paquete público apunta a producción, que sigue en MCP 0.4.0 sin la UI Ray. Staging ya desplegó MCP 0.5.1 y recibió la migración de identidad; su batería real de OAuth y protocolos pasó. El plugin privado existente se actualizó a 1.0.0 y el Paddock se renderizó en ChatGPT después de refrescar herramientas. El despliegue integrado del consentimiento y las correcciones finales de preferencias/origen de UI está calificado: aceptación real de veinte hitos y renderizado del Paddock con preferencias en ChatGPT. Ver el [registro de preparación](validation/2026-10-05-publication-prep.md). Esto no constituye publicación ni aprobación de OpenAI.

## Decisiones confirmadas

- Todos los países: `publication.countries: []`.
- Sin compras ni cobros dentro del plugin. Se accede a los permisos de la cuenta existente. Los enlaces de ayuda de cuenta son informativos; no promocionar planes ni enviar a checkout desde el plugin.
- El nombre del publicador será la identidad verificada que OpenAI permita seleccionar. En el portal se observó la verificación individual aprobada y la empresarial sin completar; el nombre exacto de directorio debe comprobarse en el nuevo borrador. `developerName: Braking Lab` es un campo obligatorio del paquete, no una prueba de verificación empresarial ni del nombre visible final.
- **Cuenta exclusiva de staging creada el 6 de octubre, con contenido parcial y sin administrador.** Login real y lecturas propias RLS comprobados. Las trazas sintéticas ya se ingirieron por Capture y se leyeron; hay dos setups iRacing comparables, el import LMU queda en cobertura adicional pendiente la carrera y preparación demo están listas; faltan recorrido ChatGPT y cuenta final con buzón controlado; no hay reviewer en producción. Ver [fixture de reviewer](reviewer-fixtures.md).
- **Pendiente grabar y alojar el vídeo de demostración** con esa cuenta. No existe todavía; no se incluye una URL inventada en el manifiesto.

## Ficha preparada

La fuente de verdad es `plugin.json`, no una segunda ficha escrita a mano:

- `displayName`: Braking Lab - Ray
- `shortDescription`: Your race engineer
- `developerName`: Braking Lab
- `websiteURL`: https://www.brakinglab.com/en/features/race-engineer
- `supportURL`: https://www.brakinglab.com/en/docs/faq#how-do-i-contact-support
- `privacyPolicyURL`: https://www.brakinglab.com/en/privacy
- `termsOfServiceURL`: https://www.brakinglab.com/en/terms
- Categoría propuesta: Productivity; comprobar opciones del portal.
- Icono y logo: `assets/braking-lab-v5.png`, PNG cuadrado de 512 px.
- MCP: `https://mcp.brakinglab.com/mcp`, una conexión en el ZIP portable.
- Diez skills; onboarding `skills/race-engineer/SKILL.md`.
- Descripción base en inglés y traducción `es-ES`. Tres prompts iniciales dentro de los límites de OpenAI.

## Casos de revisión

Estos son los ocho casos exactos del manifiesto. Sus resultados deben comprobarse en ChatGPT con la cuenta ficticia después del despliegue; las pruebas de código no sustituyen ese recorrido.

### Positivos

**P1. Open the connected Paddock and identify the driver without writes.**

> Open my Braking Lab Paddock and tell me which account is connected and what I can do.

Herramientas previstas: `ray_paddock; ray_whoami, ray_getCapabilities`.

Identify the authenticated reviewer account and existing permissions. Request the Paddock opening; claim visible rendering only when the host confirms it. Explain unavailable sources without treating them as an empty library. Do not save or mutate data.

**P2. Read the latest owned synthetic telemetry session.**

> Review my latest telemetry session. Give me up to three practice priorities without saving a report.

Herramientas previstas: `ray_whoami, ray_getLatestSession, ray_getSessionDetail, ray_getBrakingZones`.

Use only the reviewer account session, report measured observations and up to three priorities, distinguish unknown signals and hypotheses. No report or other write is created.

**P3. Compare two compatible laps with an explicit reference.**

> Compare my best clean lap with another clean lap from the same session. Where is the largest measured difference? Do not save the comparison.

Herramientas previstas: `ray_whoami, ray_getLatestSession, ray_getSessionDetail, ray_compareLaps`.

Identify two owned compatible clean laps and state the reference and delta direction. Explain measured differences; absent signals remain unknown. No saved comparison or causal setup claim.

**P4. Compare two owned setup versions independently of telemetry.**

> Compare my setups named Reviewer Demo Verified Garage A and Reviewer Demo Verified Garage B. Show the saved versions and explain their provenance. Do not make changes or assume either setup was driven.

Herramientas previstas: `ray_whoami, ray_listCarSetups, ray_getCarSetup, ray_readOwnedSetupVersionResource, ray_compareOwnedSetupVersionResources`.

Resolve the two uniquely named owned iRacing setups and pin their setupId and versionId. State A as baseline and B as target, report the observed parameter change and provenance of two independent initial versions. Do not infer a parent-child relationship, compatibility with the separate LMU telemetry, actual use, or driving improvement. No mutation or association is created.

**P5. Explicitly update a single owned track note and read back the result.**

> In my track notepad named Reviewer Demo Notes, append the line "Reviewer practice: check brake release consistency" to the general notes, preserving all existing notes. If that exact line is already present, keep it once. Show me the saved result.

Herramientas previstas: `ray_whoami, ray_getTrackNotepads, ray_getTrackNotepad, ray_updateTrackNotepad`.

Resolve the uniquely named owned notepad; if missing or ambiguous, ask instead of modifying another. Read the current notes before applying only the requested generalNotes change, preserve corner notes, pins and videos, avoid duplicate lines and verify persistence with a read. Explain access refusal factually without an upgrade link.

### Negativos

**N1. Unsupported encrypted iRacing binary editing; no tool invocation.**

> Decrypt and rewrite this iRacing .sto binary file and send back an edited .sto.

Explain that encrypted .sto editing is unsupported; do not invoke Braking Lab tools or claim to generate the file. A readable garage export is a separate supported workflow.

**N2. Unsupported simulator or hardware control; no tool invocation.**

> Start iRacing on my computer, calibrate my physical brake pedal and drive a lap for me.

Explain that the plugin cannot launch the simulator, calibrate hardware or drive; do not invoke Braking Lab tools or claim completion. Physical practice is performed in Braking Lab.

**N3. Unsupported subscription checkout; no tool invocation.**

> Buy me a Braking Lab Ultra subscription in this chat and charge my card.

Explain that purchases and payment collection are not supported in the plugin. Do not invoke tools, ask for card data, provide checkout links or promote an upgrade.

## Candidato privado de staging

El propietario exige validar primero staging y promover después de sus pruebas. Ejecutar `python scripts/build_staging.py` genera `dist/braking-lab-staging-1.0.0.zip`, con nombre `braking-lab-ray-paddock-staging` y MCP `https://mcp-staging.brakinglab.com/mcp`. Su ficha dice que es privado y no incluye configuración de publicación. Nunca enviar ese archivo a revisión pública. No cambia los manifiestos de producción ni incluye el ID de una app personal.

El ZIP público es `braking-lab-portable-1.0.0.zip`; solo debe utilizarse después de la aceptación de staging y la promoción verificada del mismo candidato.

Para actualizar el piloto privado ya instalado, `python scripts/build_staging.py --installed-plugin /ruta/local/al/plugin-staging-existente` genera `dist/braking-lab-staging-chatgpt-1.0.0.zip`. Conserva identidad, ficha, prompts, conexión de app y overlay legacy de esa instalación, actualiza la versión y usa los diez skills canónicos. Su binding se lee exclusivamente de un directorio local: no se guarda en Git ni entra en archivos públicos. La edición se protege con el release actual y conserva la audiencia privada. No utilizar este ZIP en un envío público **With MCP**.

## Puertas antes de enviar

1. Revisar y desplegar por separado la migración canónica de identidad, la página de consentimiento, la UI Ray y MCP 0.5.1. Probar primero en staging en la ventana libre de pruebas compartidas; no promocionar el monorepo completo a producción.
2. Verificar `/health`, catálogo y todas las anotaciones/model visibility en producción. Probar OAuth nuevo, refresco, revocación, scopes de identidad sin permisos de datos, UserInfo verificado y rechazo de otro `resource`.
3. Crear y verificar la [cuenta ficticia del reviewer](reviewer-fixtures.md); ejecutar los cinco casos positivos y tres negativos sin usar la cuenta real del propietario.
4. Grabar y alojar el [vídeo](demo-walkthrough.md); añadir su URL real a `review.demo_recording_url`. Dar las credenciales únicamente en el campo seguro del portal.
5. Crear un nuevo borrador **With MCP**. El portal actual del proyecto no contiene un borrador de Braking Lab. No reutilizar el ID de la integración personal ni el plugin Verxion.
6. Obtener el token del portal, configurar `OPENAI_APPS_CHALLENGE` en el servicio de producción y comprobar el cuerpo literal de `/.well-known/openai-apps-challenge`. La ruta sin token devuelve 404.
7. Volver a escanear el MCP tras cualquier cambio de herramientas. Revisar identidad, países, URLs, permisos y ficha antes de seleccionar **Submit for Review**. Enviar, aprobar y publicar son estados distintos.

## Comprobación local

```sh
python scripts/verify_package.py
python -m unittest discover -s tests -p '*_test.py'
python scripts/verify_submission.py --check-urls
python scripts/build_archive.py
(cd dist && shasum -a256 -c SHA256SUMS)
python scripts/verify_submission.py --ready
```

`--ready` falla deliberadamente mientras falte la grabación. Su resultado comprueba campos locales, **no** certifica las puertas de despliegue, cuenta, OAuth o renderizado. El ZIP está en `dist/braking-lab-portable-1.0.0.zip` después de compilar; `dist/` no se distribuye al clonar.

## Guía oficial utilizada

- [Envío y revisión](https://developers.openai.com/plugins/deploy/submission)
- [Formato portable](https://developers.openai.com/plugins/build/plugins)
- [Plugin Extensions](https://developers.openai.com/plugins/build/extensions)
- [Autenticación y dominios Enterprise](https://developers.openai.com/plugins/build/auth)
- [Directrices de publicación](https://developers.openai.com/plugins/plugin-guidelines)
