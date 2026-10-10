# Preparación del envío público a OpenAI — 1.0.0

Estado vigente del 10 de octubre de 2026: staging privado **1.1.9**, paquete
público **1.0.0**, MCP **0.5.2**. PR 150 integrada en develop
`bd4bc9da7c2dbe82f9c813d2436d4a4bdad5bf2b` y PR 151 en main
`0e058c9a51d8551d0d811bca372a82620ecc4c3b`; ambos despliegues están
comprobados. El ZIP nuevo `6d9405411dfc99b348b4f3e5dcc0af817cd0fea4638a19329fe10f0e67d899ef`
ya se ha subido al mismo borrador y su conexión OAuth permanece autorizada. El
escaneo de MCP 0.5.2 terminó sin findings y las diez skills pasan sus checks. La comprobación autenticada de staging pasó
12 bloques y la de producción 20 checks, sin cambios de contenido; las grants
temporales exactas quedaron revocadas. Los casos nativos del borrador público
no están acreditados: la última prueba de acceso devolvió «Plugin not found»
y no había control de ensayo nativo en el portal. Tras actualizar categoría y
descripción, una recarga mostró el estado **In review** de 1.0.0 y publicación
**Not published**. El envío está realizado; no se afirma aceptación nativa ni
aprobación o publicación. El agente no marcó declaraciones ni pulsó Submit.

La primera promoción base fue MCP 0.5.1. PR 149 promovida a main
`74acf0498a4683f532dad2c33b33ec10c6d0a99b`, desplegada en producción mediante
Railway `6e20bf20-3d1b-4712-addc-5949a5aca87f`. La cualificación autenticada
pasó OAuth stateful, identidad, recursos UI, refresh y revocación. La conexión
nativa de desarrollo mostró Ray y sus bibliotecas con Franz Hermann.

Franz tiene perfil privado, membresía Ultra sintética y acceso por contraseña
con recuperación a cargo de Braking Lab. Contiene tres libretas, tres sesiones,
seis vueltas y dos setups independientes. Dos libretas y una sesión/dos vueltas
son copias privadas de material real expresamente autorizado por el propietario;
el resto son fixtures sintéticas. No atribuir estos registros reales a Franz ni
asociarlos a sus setups. El recorrido principal muestra Silverstone, Stowe y
sus pins, trazas reales y conversación sobre la evidencia.

La aprobación humana y readback de P5 ya están verificados. El vídeo de demostración
`ray-production-reviewer-demo-v2.mp4` dura 3:44, con escenas reales de interfaz,
conversación y guardado aprobado. Está alojado y se reproduce sin login en [R2](https://media.rbart-dev.com/review/ray/v1/ffdf219c55cf703344e9a74a2bb0c5079a83e794d32690e5b3d5766ba6badfa8/ray-production-reviewer-demo-v2.mp4); no sustituye la
suite de ocho casos del paquete público exacto. N1 y N3 conservaron fallos en el
ensayo anterior; las correcciones de las skills están validadas en origen pero
requieren probar la versión guardada. El borrador público 1.0.0 ya está creado;
el dominio MCP está verificado y las diez skills muestran «Checks passed».
La conexión OAuth permanece autorizada a Franz y los campos privados de reviewer
se han vuelto a comprobar después del reupload, incluida la presencia de la
contraseña sin exponerla. El portal conserva los cinco casos positivos, tres
negativos, países, traducción y vídeo. El escaneo MCP actualizado no señala
incidencias; los cinco findings históricos de 0.5.1 ya no aparecen. Se ajustó la categoría a Data & Analytics y se aclaró la finalidad de
análisis de datos en inglés y español; el paso final ya no muestra el aviso
de categoría. La versión 1.0.0 figura ahora **In review**, con categoría
Data & Analytics. Los ocho casos nativos del paquete exacto continúan sin
aceptación acreditada. No se ha aprobado ni publicado. Ver el [ensayo nativo](validation/2026-10-10-native-production-rehearsal.md)
y la [comprobación de 0.5.2](validation/2026-10-10-model-operation-review.md).

## Decisiones confirmadas

- Todos los países: `publication.countries: []`.
- Sin compras ni cobros dentro del plugin. Se accede a los permisos de la cuenta existente. Los enlaces de ayuda de cuenta son informativos; no promocionar planes ni enviar a checkout desde el plugin.
- El nombre del publicador será la identidad verificada que OpenAI permita seleccionar. En el portal se observó la verificación individual aprobada y la empresarial sin completar; el nombre exacto de directorio debe comprobarse en el nuevo borrador. El portal ofrece una identidad individual verificada. El propietario exige mantener `Braking Lab` como publicador visible y no incluir su nombre completo en identificadores ni en la ficha. La ficha guardada actualmente muestra Braking Lab; verificar el nombre público final antes de enviar.
- **Cuenta exclusiva Franz Hermann en staging, sin administrador.** Login por contraseña y correo ficticio sin buzón; Braking Lab atiende la recuperación. El despliegue final pasó lecturas propias, trazas/comparación, scopes y OAuth. Los dos imports iRacing sirven para P4; el import LMU es cobertura adicional. Quedan los ocho recorridos nativos de publicación en producción. La cuenta equivalente ya está aprovisionada y sus lecturas
  pasan; no se afirma aceptación de los casos nativos. Ver el [fixture vigente](reviewer-fixtures.md) y la [cualificación final](validation/2026-10-10-final-design-handoff.md).
- **Vídeo grabado y alojado.** URL real incorporada a `review.demo_recording_url`; lectura anónima y reproducción verificadas. Copia privada retenida en R2.

## Ficha preparada

La fuente de verdad es `plugin.json`, no una segunda ficha escrita a mano:

- `displayName`: Braking Lab - Race Engineer
- `shortDescription`: Your race engineer
- `developerName`: Braking Lab
- `websiteURL`: https://www.brakinglab.com/en/features/race-engineer
- `supportURL`: https://www.brakinglab.com/en/docs/faq#how-do-i-contact-support
- `privacyPolicyURL`: https://www.brakinglab.com/en/privacy
- `termsOfServiceURL`: https://www.brakinglab.com/en/terms
- Categoría: Data & Analytics. La descripción prioriza análisis de telemetría y conversación sobre la evidencia; la categoría figura entre las admitidas por OpenAI.
- Icono y logo: `assets/braking-lab-isotype.png`, PNG cuadrado de 512 px.
- MCP: `https://mcp.brakinglab.com/mcp`, una conexión en el ZIP portable.
- Diez skills; onboarding `skills/race-engineer/SKILL.md`.
- Descripción base en inglés y traducción `es-ES`. Tres prompts iniciales dentro de los límites de OpenAI.

## Casos de revisión

Estos son los ocho casos exactos del manifiesto. Sus resultados deben comprobarse en ChatGPT con la cuenta ficticia después del despliegue; las pruebas de código no sustituyen ese recorrido.

### Positivos

**P1. Open Race Engineer and identify the connected driver without writes.**

> Open Braking Lab - Race Engineer and tell me which account is connected and what I can do.

Herramientas previstas: `ray_paddock; ray_whoami, ray_getCapabilities`.

Identify the authenticated reviewer account and existing permissions. Open the Race Engineer workspace through ray_paddock; claim visible rendering only when the host confirms it. Explain unavailable sources without treating them as an empty library. Do not save or mutate data.

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

Resolve the uniquely named owned notepad; if missing or ambiguous, ask instead of modifying another. Read the current notes and show an exact draft of the generalNotes change. Ask for the pilot's explicit approval before saving, even when the initial prompt requests a saved result. Then apply only the approved generalNotes change, preserve corner notes, pins and videos, avoid duplicate lines and verify persistence with a read. Explain access refusal factually without an upgrade link.

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

1. Promoción y despliegue completados: PR 149, main y Railway indicados arriba. MCP y UI Ray viajan juntos; no hubo despliegue de SPA, Capture o Landing ni migración adicional de OAuth.
2. Verificar `/health`, catálogo y todas las anotaciones/model visibility en producción. Probar OAuth nuevo, refresco, revocación, scopes de identidad sin permisos de datos, UserInfo verificado y rechazo de otro `resource`.
3. La [cuenta del reviewer](reviewer-fixtures.md) ya está creada y su login/datos cualificados. Ejecutar los cinco casos positivos y tres negativos sobre el paquete público exacto; los ensayos de la conexión de desarrollo no sustituyen esa puerta.
4. Grabar y alojar el [vídeo](demo-walkthrough.md); añadir su URL real a `review.demo_recording_url`. Dar las credenciales únicamente en el campo seguro del portal.
5. Borrador público creado en el proyecto Braking Lab: `plugin_asdk_app_6aca9fc11f2c8191a867e4475e078342`, versión `appsub_6aca9fc11f60819191bfca3756c086e2`. La ficha muestra `Braking Lab` y el identificador `braking-lab-race-engineer`; las diez skills pasan. No reutiliza la integración personal ni Verxion. OAuth a Franz y los campos privados de reviewer ya están completos. Faltan los casos nativos de esta versión y el nuevo escaneo de MCP 0.5.2 tras su despliegue.
6. Dominio verificado. `OPENAI_APPS_CHALLENGE` está configurado; el cuerpo literal HTTPS coincide con el token del portal. Railway `bc538ec9-2b7a-40a3-a0e1-8f75d93c277a` reutiliza main `74acf0498a4683f532dad2c33b33ec10c6d0a99b`; `/ready` responde `ready`. La ruta sin token devuelve 404.
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

`--ready` comprueba los campos locales y la URL declarada, **no** certifica las puertas de cuenta, OAuth, versión guardada o renderizado. El ZIP está en `dist/braking-lab-portable-1.0.0.zip` después de compilar; `dist/` no se distribuye al clonar.

## Guía oficial utilizada

- [Envío y revisión](https://developers.openai.com/plugins/deploy/submission)
- [Formato portable](https://developers.openai.com/plugins/build/plugins)
- [Plugin Extensions](https://developers.openai.com/plugins/build/extensions)
- [Autenticación y dominios Enterprise](https://developers.openai.com/plugins/build/auth)
- [Directrices de publicación](https://developers.openai.com/plugins/plugin-guidelines)
