# Plan de distribución del Race Engineer

- **Fecha:** 2026-09-26
- **Estado:** paquetes privados importados e instalados; pruebas autenticadas y publicaciones pendientes
- **Fuente:** este repositorio privado, con una sola copia de las nueve skills en `skills/`

## Decisión de lanzamiento — 27 de septiembre

La publicación dirigida a usuarios se hará con **las tres vías disponibles a la vez**: Claude, ChatGPT y una instalación por CLI para otras personas. No se anunciará un lanzamiento parcial de solo Claude o solo repositorio público. La URL de la landing se activará cuando las tres rutas tengan instrucciones reales y una primera consulta autenticada comprobada.

- **Claude:** plugin de Claude Code desde el marketplace Git del repositorio y ZIP para Claude chat. La ficha del directorio de Anthropic puede tramitarse en paralelo; no es requisito para compartir el plugin desde GitHub.
- **ChatGPT:** ficha pública del Plugins Directory compartido con Codex. El ZIP del piloto usa una app personal y no sirve como prueba de instalación para cuentas ajenas. El portal exige identidad publicadora verificada antes incluso de crear un borrador. El 27 de septiembre, la organización `rbart ventures` ofrecía iniciar verificación individual o de empresa; el propietario eligió identidad individual. El trámite de Persona queda en manos del propietario.
- **CLI:** usar primero `npx skills add r-bart/braking-lab-agent-skills -g` desde el repositorio público, más los pasos MCP/OAuth del cliente. Ese comando instala skills, no la conexión. Probar una instalación limpia y una consulta autenticada por cada cliente que se anuncie. Crear un CLI propio solo si esas pruebas demuestran que hace falta para completar el recorrido.

El calendario de ChatGPT depende de la revisión de OpenAI después del envío. Preparar paquetes y repositorio no acorta ni sustituye esa revisión. Mantener la release privada hasta que el directorio apruebe el plugin y las tres rutas puedan lanzarse juntas.

## Objetivo

Que un piloto de Braking Lab pueda elegir Claude o ChatGPT, instalar el Race Engineer desde el directorio de su asistente, autorizar su cuenta de Braking Lab y empezar con una pregunta útil. Para otros agentes, aprovechar el paquete portable cuando instale skills y MCP; donde no lo haga, ofrecer instalación de skills por CLI y una guía corta para conectar el MCP. La instalación no debe prometer operaciones que un cliente no pueda completar, en particular las que requieren `elicitation.form`.

La [validación de las skills](test-plan.md) es una puerta de entrada para publicar. Este plan fija la secuencia de distribución, pero no convierte una prueba estructural en una aprobación de producto. El repositorio sigue privado durante el piloto.

**Avance del 26 de septiembre:** los tres archivos se construyen desde `skills/`. ChatGPT y Claude chat importaron sus archivos; Claude Code y Codex instalaron desde el repositorio privado. ChatGPT completó OAuth y consultas de lectura; Claude completó OAuth, pero el límite de uso de la cuenta impidió la primera respuesta. La [evidencia de validación](validation/2026-09-26-packaging.md) registra los detalles. Siguen abiertos los flujos de escritura, la prueba con otra cuenta y la revisión de directorios.

## Decisión de arquitectura

| Opción                                                 | Ventaja                                                             | Coste o límite                                                                                       |
| ------------------------------------------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Solo MCP y documentación                               | Se puede ofrecer ya con la URL del servidor                         | El usuario conecta manualmente el MCP; no recibe los flujos guiados de las skills                    |
| Solo `npx skills add`                                  | Un comando instala skills en muchos agentes                         | No instala ni autentica de forma universal el MCP; ChatGPT web y Claude chat necesitan su vía nativa |
| **Un repo, dos paquetes nativos y CLI complementario** | Instalación sencilla en Claude y ChatGPT; una sola fuente de skills | Dos manifiestos, dos revisiones de directorio y pruebas por cliente                                  |

Elegir la tercera opción. Mantener `skills/` como fuente única y el MCP remoto como autoridad para datos, permisos, cuotas y confirmaciones. Los manifiestos son adaptadores de instalación; no contienen otra versión de los flujos. No crear un CLI de Braking Lab hasta comprobar que el CLI existente deja una necesidad real sin cubrir.

Estructura en este mismo repositorio:

```text
skills/                         Nueve Agent Skills compartidas
plugin.json                     Paquete Agent Plugins portable
mcp.json                        Referencia portable al MCP remoto
.claude-plugin/plugin.json      Metadatos del plugin de Claude
.claude-plugin/marketplace.json Catálogo privado de Claude Code
.agents/plugins/marketplace.json Catálogo de Codex
.mcp.json                       Referencia al MCP para Claude
openai/app.json                 Conector personal registrado para ChatGPT
scripts/build_archive.py        Tres archivos de distribución desde skills/
docs/                           Pruebas, instalación y soporte
```

Los formatos de `mcp.json` y `.mcp.json` son distintos y apuntan al mismo servicio de producción. El archivo ChatGPT contiene un manifiesto generado con `.app.json` y omite `mcp.json` para mostrar una sola conexión. El archivo portable mantiene `mcp.json` y omite `.app.json`; el de Claude utiliza `.mcp.json`. Las pruebas contra staging usarán una copia local o configuración de prueba claramente marcada, nunca un manifiesto publicable que pueda dirigir usuarios a staging. No introducir hooks ni scripts de instalación si las skills y el MCP remoto bastan.

## Alcance de cada vía

| Vía                                 | Qué instala                                                | Qué hace todavía el piloto                                                                                          |
| ----------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Plugin de Claude                    | Skills y referencia al MCP                                 | Instalar el plugin y autorizar Braking Lab; confirmar operaciones sensibles cuando el cliente soporte el formulario |
| Plugin de ChatGPT                   | Skills y conexión registrada al MCP                        | Instalar desde el directorio y completar OAuth de Braking Lab                                                       |
| Codex                               | El paquete de OpenAI, si las pruebas confirman ese cliente | Instalar y autorizar; no afirmar equivalencia con ChatGPT solo por compartir directorio                             |
| Otros clientes Agent Plugins        | Skills y MCP, si ambos se cargan en ese cliente            | Instalar el paquete y completar OAuth; verificar las capacidades antes de anunciar soporte                          |
| `npx skills add` para otros agentes | Solo las skills compatibles                                | Conectar el MCP Streamable HTTP y completar OAuth según el cliente; consultar las limitaciones verificadas          |

Una skill instalada no da más acceso que el MCP. Los clientes sin conexión MCP obtienen instrucciones, pero no pueden leer la telemetría ni modificar datos de Braking Lab. Los que no soportan la confirmación directa deben mostrar un rechazo seguro en esos flujos.

## Fases de implementación

Cada tarea termina con los archivos válidos y el repo en un estado instalable para la vía que ya funcionaba. Las publicaciones públicas son tareas separadas de la creación del paquete.

### Fase 0 — cerrar la calidad de las skills

**Antes:** nueve skills escritas y validadas estructuralmente. **Después:** resultado reproducible del [plan de pruebas](test-plan.md), con matriz de soporte por cliente.

#### Tarea 0.1 — ejecutar el plan de pruebas

- [ ] Completar validación de catálogo, corpus de activación, pruebas de staging y revisión editorial.
- [ ] Recuperar el acceso OAuth a staging sin usar producción como sustituto.
- [ ] Registrar qué operaciones funcionan en Claude Code y Codex, y cuáles fallan de forma segura por falta de `elicitation.form`.
- [ ] Etiquetar un candidato privado de skills con su versión de catálogo MCP.

**Verificación:** se cumplen los criterios de «listo» en `docs/test-plan.md`; los límites de cliente quedan escritos.

### Fase 1 — paquete de Claude en el repo privado

**Antes:** skills instaladas localmente. **Después:** plugin de Claude que se carga desde el mismo repo sin copiar `skills/`.

#### Tarea 1.1 — manifiesto y MCP

- [ ] Crear `.claude-plugin/plugin.json` y `.mcp.json` con nombre, versión, descripción, autor y servidor correctos. No guardar tokens ni credenciales.
- [ ] Validar con `claude plugin validate . --strict` y cargar la copia local con `claude --plugin-dir .`.
- [ ] Confirmar inventario de nueve skills, una sola conexión MCP, OAuth y cuenta esperada; probar un debrief de lectura y un flujo de escritura permitido.

**Verificación:** validación estricta sin avisos, skill elegida por una petición natural y `whoami` de la cuenta de prueba correcta.

#### Tarea 1.2 — instalación privada de Claude

- [ ] Probar el archivo ZIP para un tester individual. Si el piloto necesita actualizaciones para varios testers, preparar un marketplace privado de GitHub y comprobar instalación y actualización con una cuenta distinta de la autora.
- [ ] Comprobar por separado Claude chat y Claude Code antes de afirmar soporte en ambas superficies. Registrar si el conector aparece, pide OAuth y conserva la sesión.
- [ ] Ensayar desinstalación, reinstalación y una versión nueva sin duplicar las skills o el MCP.

**Verificación:** un tester autorizado instala, inicia sesión, obtiene una respuesta útil y puede actualizar o retirar el plugin siguiendo la guía.

### Fase 2 — paquete de ChatGPT y comprobación de Codex

**Antes:** fuente de skills y paquete Claude listos. **Después:** paquete Agent Plugins probado en ChatGPT; Codex queda identificado como compatible o limitado por evidencia.

#### Tarea 2.1 — manifiesto portable y conexión

- [ ] Crear `plugin.json` y `mcp.json` en la raíz, con `skills/` descubierto desde su ubicación canónica. Registrar el MCP en ChatGPT Developer mode y añadir el mapeo específico que exija el cliente, si lo exige.
- [ ] Validar los esquemas JSON, rutas y metadatos; instalar el paquete como plugin personal en una cuenta de prueba.
- [ ] Probar selección de skill, OAuth, `whoami`, un análisis de lectura y una escritura ordinaria con lectura posterior. Probar una operación con formulario en un cliente que lo soporte y el rechazo seguro en otro que no.

**Verificación:** instalación y primer uso completos en ChatGPT, sin copiar las skills ni crear una segunda fuente de verdad.

#### Tarea 2.2 — prueba específica en Codex

- [ ] Instalar el mismo paquete desde un marketplace local o de repositorio de Codex.
- [ ] Comprobar descubrimiento de las nueve skills, conexión OAuth y al menos un flujo de lectura y uno de escritura en una sesión nueva.
- [ ] Documentar diferencias reales frente a ChatGPT; si una capacidad no funciona, no anunciarla para Codex.

**Verificación:** matriz de soporte separada para ChatGPT y Codex, vinculada a transcripciones depuradas.

### Fase 3 — piloto privado y experiencia de instalación

**Antes:** ambos paquetes funcionan en la máquina de desarrollo. **Después:** una persona ajena a la implementación puede instalar y usar el Race Engineer sin ayuda en vivo.

#### Tarea 3.1 — instrucciones y ensayo con testers

- [ ] Redactar dos guías de máximo una pantalla: «Instalar en Claude» y «Instalar en ChatGPT», con pasos de OAuth, primer prompt, actualización, desconexión y ayuda si la cuenta conectada no es la correcta.
- [ ] Pedir a testers de ambos clientes que sigan la guía desde cero. Observar pasos, errores y tiempo hasta la primera respuesta basada en sus datos; no usar datos privados en el registro de resultados.
- [ ] Corregir los puntos donde el usuario tenga que copiar JSON, buscar una URL interna o entender `SKILL.md`.

**Verificación:** cada tester completa instalación, OAuth y primera pregunta sin intervención; los fallos tienen caso reproducible y solución documentada.

#### Tarea 3.2 — seguridad de publicación

- [ ] Revisar todos los archivos e historial que se expondrían si el repositorio se hiciera público. Decidir licencia, identidad publicadora, soporte, privacidad y términos; no cambiar la visibilidad del repo como efecto lateral de preparar el paquete.
- [ ] Separar el mapeo `openai/app.json` de la distribución pública: contiene el ID de la app personal del piloto. La release pública no debe ofrecer el ZIP de ChatGPT del piloto como instalación general; la ficha aprobada por OpenAI será la ruta para otras cuentas.
- [ ] Fijar versión de skills y contrato MCP; comprobar que la URL publicable es la de producción, que staging no aparece en el paquete y que el servidor de producción ofrece las funciones probadas.
- [ ] Preparar rollback: versión anterior del paquete, desactivar o retirar una ficha, y mensaje para usuarios afectados sin prometer que desinstalar borra datos de su cuenta.

**Verificación:** checklist de publicación firmado en el repo privado; cero secretos o fixtures en el paquete; versión reproducible.

### Fase 4 — publicación nativa para Claude y ChatGPT

**Antes:** piloto privado aprobado. **Después:** usuarios pueden instalar desde los directorios, siguiendo enlaces de Braking Lab.

#### Tarea 4.1 — envío a directorios

- [ ] Enviar el plugin de Claude con su paquete, información de acceso al MCP y materiales que exija Anthropic. Resolver su validación y revisión antes de publicar.
- [ ] Crear en el portal de OpenAI un envío **With MCP** con la URL HTTPS de producción e incluir las nueve skills en ese mismo borrador. No presentar `openai/app.json`, el ID de la app personal ni el ZIP privado como referencia de una integración ya publicada: el portal debe escanear el MCP directamente. Completar identidad verificada, dominio, política de privacidad, cuenta demo de producción sin MFA ni confirmación por correo, grabación de los casos principales, cinco casos positivos, tres negativos y anotaciones reales de todas las herramientas. El portal no permite crear el borrador antes de verificar la identidad publicadora.
- [ ] Preparar en el servidor MCP la prueba de dominio `/.well-known/openai-apps-challenge` y el soporte OAuth exigido para restricciones de dominio de workspace: scopes `openid` y `email`, UserInfo Endpoint con `email` y `email_verified: true`. El catálogo actual anuncia solo `race-engineer:read` y `race-engineer:write`; este cambio pertenece al monorepo y requiere implementación y pruebas separadas antes de solicitar revisión pública.
- [ ] Mantener estados separados: «enviado», «aprobado» y «publicado» no son equivalentes. No enlazar una ficha antes de confirmar que está visible para una cuenta ajena.

**Verificación:** instalación desde cada directorio en una cuenta nueva, OAuth y primera consulta correctos; guardar URL real de cada ficha.

#### Tarea 4.2 — entrada única en Braking Lab

- [ ] Crear en la landing una página «Usa Race Engineer con tu asistente» con botones para Claude y ChatGPT, y una opción «Otro cliente MCP». La página explica el requisito de cuenta, autorización y límites del plan sin lenguaje técnico innecesario.
- [ ] Enlazar cada botón a la ficha comprobada, no a una búsqueda o a un enlace supuesto. Después de instalar, mostrar un prompt inicial concreto y la solución si se conectó la cuenta equivocada.
- [ ] Medir de forma agregada el recorrido botón → conexión autorizada → primer uso satisfactorio, sin registrar telemetría de conducción ni tokens.

**Verificación:** los dos recorridos desde la landing funcionan en móvil y escritorio; cada enlace llega a la ficha correcta y la guía coincide con el producto publicado.

### Fase 5 — CLI para otros agentes (ejecutar antes del lanzamiento conjunto)

**Antes:** el repositorio sigue privado y se pueden probar instalaciones locales. **Después:** cada cliente adicional anunciado tiene una ruta de instalación probada y lista para activarse al abrir el repositorio. Se usa el paquete Agent Plugins cuando el cliente carga skills y MCP; el CLI cubre los clientes que necesitan instalar las skills por separado.

#### Tarea 5.1 — probar el paquete portable y el CLI existente

- [ ] Consultar la lista vigente de clientes Agent Plugins y probar el paquete completo en dos o tres con demanda real, empezando por Cursor y VS Code/GitHub Copilot. Confirmar descubrimiento de skills, conexión MCP, OAuth, actualización y desinstalación; la lectura del manifiesto por sí sola no prueba compatibilidad.
- [ ] Donde el paquete no ofrezca una instalación completa, probar `npx skills add r-bart/braking-lab-agent-skills -g` en un entorno limpio y validar selección, actualización y desinstalación. Durante el piloto privado requiere acceso a GitHub; para uso abierto exige una fuente pública o un paquete público revisado.
- [ ] Revisar la telemetría de instalación del CLI de terceros y su opción de exclusión antes de recomendar el comando en una página pública.
- [ ] Publicar una tabla por cliente: ruta de instalación probada, pasos para conectar el MCP cuando hagan falta, OAuth, funciones probadas y límites. No presentar la instalación de skills como instalación completa del Race Engineer.

**Verificación:** un tester reproduce la instalación elegida, conecta el MCP, inicia sesión y completa una consulta de lectura en cada cliente anunciado.

#### Tarea 5.2 — decidir si hace falta CLI propio

- [ ] Revisar los resultados de la tarea 5.1. Crear un instalador de Braking Lab solo si el paquete portable y la configuración MCP documentada siguen impidiendo la mayoría de instalaciones y existe una API o archivo estable para cada cliente objetivo.
- [ ] Si se construye, definir `install`, `check`, `update` y `uninstall`, cambios reversibles y detección de configuraciones existentes. El CLI no recibirá ni almacenará contraseñas de Braking Lab: OAuth permanece en el cliente.
- [ ] Si el CLI existente basta, mantener solo las guías y evitar otro programa que actualizar.

**Verificación:** decisión registrada con fallos observados y coste de mantenimiento; ningún CLI propio se publica por inercia.

## Dependencias y archivos previstos

```yaml
dependencies:
  "1.1": ["0.1"]
  "1.2": ["1.1"]
  "2.1": ["0.1"]
  "2.2": ["2.1"]
  "3.1": ["1.2", "2.1"]
  "3.2": ["3.1", "2.2"]
  "4.1": ["3.2"]
  "4.2": ["4.1", "5.1"]
  "5.1": ["2.1", "3.1"]
  "5.2": ["5.1"]
```

| Archivo                                                                             | Acción prevista                                     | Finalidad                                 |
| ----------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------- |
| `skills/*/SKILL.md`                                                                 | Mantener una sola copia; corregir solo tras pruebas | Flujos portables                          |
| `plugin.json`, `mcp.json`                                                           | Crear en fase 2                                     | Paquete portable y MCP para OpenAI        |
| `.claude-plugin/plugin.json`, `.mcp.json`                                           | Crear en fase 1                                     | Paquete y MCP para Claude                 |
| `.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`               | Crear solo si lo exige la vía privada elegida       | Catálogos pequeños; no duplican skills    |
| `docs/test-plan.md`, `docs/validation/`                                             | Ejecutar y registrar                                | Puerta de calidad y evidencia depurada    |
| `docs/install-claude.md`, `docs/install-chatgpt.md`, `docs/install-other-agents.md` | Crear según cada fase                               | Ayuda breve y específica por cliente      |
| `apps/landing/...` en el monorepo privado                                           | Crear en fase 4, mediante cambio separado           | Entrada de usuarios y enlaces verificados |

## Riesgos y decisiones antes de publicar

| Riesgo                                                                | Respuesta                                                                                                     |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Un cliente instala la skill pero no conecta el MCP                    | Separar claramente «instalar» y «conectar tu cuenta»; prueba de primer uso en cada vía                        |
| ChatGPT y Claude difieren en OAuth o `elicitation.form`               | Matriz por cliente y rechazo seguro; no afirmar paridad por compartir skills                                  |
| El catálogo MCP cambia respecto al plugin aprobado                    | Fijar versión, contrato y prueba de staging/producción antes de cada release; coordinar rollback              |
| Un manifiesto de prueba apunta a staging                              | Generar copias de prueba fuera del paquete publicable y comprobar URL de producción en CI                     |
| Repo privado y CLI público son incompatibles para usuarios sin acceso | Elegir fuente pública revisada antes del lanzamiento abierto; no pedir credenciales GitHub al piloto habitual |
| Duplicar skills por plataforma crea drift                             | Una sola carpeta `skills/`; empaquetados y catálogos solo la referencian                                      |
| Instalador propio amplía soporte sin pruebas                          | Probar el paquete portable y el CLI existente; ampliar únicamente con demanda y clientes concretos            |
| El CLI de terceros recoge telemetría de instalación                   | Revisar qué envía y cómo desactivarla; informar al usuario si se recomienda                                   |

## Criterio final

El lanzamiento conjunto ocurre cuando Claude se instala desde el marketplace Git o el ZIP probado, ChatGPT se instala desde una ficha pública aprobada, y la vía CLI se reproduce desde un repositorio público en cada cliente anunciado. Las tres rutas deben completar OAuth y una primera consulta con la cuenta correcta; la landing enlaza a destinos comprobados. Las operaciones aún no verificadas se describen como límites de la versión, sin atribuirles compatibilidad. La fuente de skills sigue siendo única y los resultados se documentan por versión.

## Referencias del formato

- [Agent Skills](https://agentskills.io/specification), [Agent Plugins](https://agent-plugins.org/) y su [lista de clientes compatibles](https://agent-plugins.org/compatible-clients) para el núcleo portable.
- [Plugins de Claude](https://code.claude.com/docs/en/plugins-reference) y [marketplaces privados de Claude](https://code.claude.com/docs/en/plugin-marketplaces).
- [Paquetes de OpenAI](https://developers.openai.com/plugins/build/plugins), [envío al directorio](https://developers.openai.com/plugins/deploy/submission) y [envío de plugins con MCP remoto](https://developers.openai.com/plugins/guides/submit-claude-plugin).
- [CLI de Skills](https://github.com/vercel-labs/skills) para instalación en otros agentes.
