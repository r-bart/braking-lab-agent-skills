# Plan de pruebas del set de skills del Race Engineer

- **Fecha:** 2026-09-26
- **Estado:** en ejecución; OAuth de staging recuperado y configuración preview corregida. La [última validación de staging](validation/2026-09-26-staging-validation.md) ejecutó 78 tests E2E correctos y omitió 2 casos de transporte con activación independiente; aún no cumple los criterios de cierre.
- **Alcance:** las nueve skills de `skills/`, usadas con el MCP del Race Engineer en Codex y Claude Code. El empaquetado y la distribución siguen el [plan de distribución](distribution-plan.md), cuya ejecución depende de estas pruebas.

## Objetivo y punto de partida

El objetivo es poder afirmar, con resultados reproducibles, que las skills se activan para las tareas adecuadas, usan el contrato vigente del MCP, respetan permisos y confirmaciones, y explican la evidencia sin exagerarla. «Listo» significa superar los criterios de salida de este documento; ninguna batería finita garantiza que un asistente nunca se equivoque.

Ya existen nueve `SKILL.md`. Su formato pasó el validador de Agent Skills y los nombres de funciones se contrastaron con una instantánea versionada del catálogo local del MCP el 2026-09-26. El repositorio `r-bart/braking-lab-agent-skills` está subido a GitHub y es privado. ChatGPT y Claude están conectados para el piloto de solo lectura. La conexión de staging está reautenticada en la cuenta Basic de prueba, que no contiene sesiones, setups ni notepads. La URL de MCP en la preview publicada ya está corregida; queda repetir una autorización nueva sin el workaround local. Las pruebas estáticas no sustituyen los casos con fixtures.

## Enfoque

| Opción                     | Ventaja                                                                  | Límite                                                                                |
| -------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| Solo revisión manual       | Rápida para detectar lenguaje confuso                                    | Difícil de repetir; puede pasar por alto una regresión de catálogo o activación       |
| Solo evaluación automática | Repetible y fácil de comparar                                            | Puede aprobar respuestas convincentes pero incorrectas o consentimientos mal tratados |
| **Mixta**                  | Combina validación determinista, conversaciones reales y revisión humana | Requiere cuentas y datos de staging preparados                                        |

Usar la opción mixta. Guardar un caso reproducible por fallo y repetirlo después de cada corrección. No convertir los textos de las skills en tests que solo comprueben que el modelo repite sus instrucciones.

## Preparación común

1. **Fijar versiones.** Registrar el commit de este repo, el commit y `CATALOG_VERSION` del MCP desplegado en staging, el cliente, su versión, el modelo, la fecha y el plan de cada cuenta. Si el MCP cambia durante una tanda, repetir los casos afectados.
2. **Preparar cuentas de staging.** Una cuenta Basic, otra con derecho a informes y una con las capacidades de estrategia que se quieran declarar compatibles. Preparar un segundo propietario para comprobar aislamiento. Usar datos de prueba o datos cuyo titular haya autorizado para la prueba; no escribir ni borrar datos de producción.
3. **Preparar casos de datos.** Sesiones con y sin telemetría, dos vueltas compatibles y otras incompatibles, un referente público con y sin traza, carreras con nombres parecidos, un notepad con varias notas y pins, setups LMU e iRacing con versiones, dos usos confirmados y una sesión sin atribución, además de un `.svm` completo válido y otro incompleto. Registrar identificadores opacos en una hoja privada, nunca en el repositorio.
4. **Restablecer staging.** Definir cómo limpiar o recrear fixtures tras cada mutación. Capturar el estado previo y posterior de cada objeto afectado. Probar borrados solo sobre objetos creados para la prueba.
5. **Definir evidencias.** Para cada caso guardar ID, precondiciones, prompt, skill esperada, funciones MCP esperadas o prohibidas, resultado, observaciones y enlace a una transcripción depurada. No subir tokens OAuth, telemetría privada, nombres de archivo privados ni payloads completos. Los resultados agregados sí pueden ir en `docs/validation/`.

Si falla OAuth o staging, continuar las fases estáticas y de redacción. Las pruebas de integración y el criterio final quedan pendientes; no se sustituyen por llamadas a producción.

## Fase 1 — contrato y estructura

**Antes:** validación local puntual. **Después:** una comprobación repetible que falla ante cambios incompatibles.

- [x] Validar los nueve directorios con `agentskills validate skills/<nombre>`; comprobar nombre de carpeta, frontmatter, `description` y referencias locales.
- [x] Comparar todas las funciones citadas con un contrato de nombres y versión exportado del `TOOL_CATALOG` del MCP fijado. El contrato de la release debe corresponder al servidor desplegado, no solo al código local. Detectar funciones retiradas y distinguirlas de campos o estados que no son funciones. `getCapabilities` confirmó en staging la versión `97-90f662d1d158357c`.
- [x] Comprobar formato Markdown, enlaces de los READMEs y ausencia de secretos, rutas privadas y artefactos de staging en los archivos que podrían publicarse más adelante.
- [x] Incorporar estas comprobaciones a CI para cada PR del repo privado. Mantener el resultado verde tras cada tarea posterior.

**Salida:** nueve skills válidas, cero referencias de función desconocidas y CI verde en el commit candidato.

## Fase 2 — selección de skill

Crear un corpus versionado en `tests/cases/` con, para cada skill, un pedido **directo**, uno **indirecto** formulado como lo haría un piloto y uno **negativo** que pertenece a otra skill o no necesita ninguna. Escribir los 27 casos en español y en inglés: **54 prompts**. Incluir límites entre `debrief`/`lap-comparison`, `setup-coaching`/`setup-evaluation`, `calendar-events`/`race-week` y `race-engineer`/tarea concreta.

- [ ] Ejecutar los 54 prompts en sesiones nuevas de Codex y de Claude Code, con el MCP conectado y las skills instaladas desde este mismo commit. Registrar la skill cargada, las llamadas realizadas y la respuesta. La mera mención del nombre de una skill no cuenta como activación correcta.
- [ ] Repetir tres veces en cada cliente los casos ambiguos y los que podrían llevar a escribir o borrar datos. Variar la redacción sin cambiar la intención.
- [ ] Ejecutar una muestra de los mismos pedidos con el MCP sin skills para ver si las skills mejoran la selección, la seguridad o la claridad. Comparar hechos observables, no solo preferencias de estilo.
- [ ] Corregir descripciones o límites que se solapen y volver a ejecutar todo el corpus tras cambios de routing.

**Salida:** los 54 casos tienen una ejecución correcta por cliente; las repeticiones sensibles no muestran activación equivocada ni una escritura no solicitada. Todo fallo se corrige o queda identificado como límite del cliente y documentado antes de declarar soporte.

**Resultado parcial del 2026-09-26:** los 54 casos pasaron en sesiones efímeras de Codex CLI con una instrucción de prueba que prohibía llamar al MCP. La selección de skill en Claude Code, las repeticiones y las respuestas con datos siguen pendientes; véase el [registro](validation/2026-09-26-test-run.md).

## Fase 3 — resultados con el MCP de staging

Probar pedidos reales, permisos y evidencia con datos fijados. Cada fila debe ejecutarse en ambos idiomas al menos una vez; repetir en ambos clientes los flujos que se vayan a declarar compatibles.

| Skill              | Caso principal                                                       | Caso límite o rechazo que debe verse                                                                        |
| ------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `race-engineer`    | Identifica cuenta, plan y capacidades actuales                       | Cuenta equivocada o Basic: no concluye que faltan datos ni promete una función bloqueada                    |
| `debrief`          | Elige la sesión y explica hasta tres prioridades apoyadas en señales | Sesión ambigua, señal ausente y Basic: no inventa consistencia ni intenta guardar un informe bloqueado      |
| `lap-comparison`   | Compara vueltas propias compatibles con referencia explícita         | Identidad incompatible, delta nulo, zona ambigua o referente público sin traza: no presenta igualdad medida |
| `setup-coaching`   | Explica un síntoma y propone un cambio comprobable                   | Telemetría compatible sin atribución: no afirma que se condujo esa versión ni que el cambio causó mejora    |
| `setup-library`    | Lee la biblioteca y su linaje de versiones                           | Nombre duplicado, `.svm` incompleto o petición de importación iRacing/rename/delete no expuesta por el MCP  |
| `setup-evaluation` | Separa uso confirmado, comparación observacional y juicio del piloto | Dos tandas no se presentan como prueba causal ni como A/B/A; uso sin atribución sigue incierto              |
| `calendar-events`  | Localiza el evento exacto antes de actuar                            | Dos carreras parecidas o evento ya existente: no edita el ID equivocado ni duplica sin motivo               |
| `track-notes`      | Encuentra la libreta correcta y conserva notas ajenas al cambio      | Alineación de curva incierta: no crea una referencia de frenada precisa inventada                           |
| `race-week`        | Prepara una carrera existente con práctica y checklist               | Tanda no vinculada, combustible desconocido o estrategia sin datos: mantiene visibles las suposiciones      |

Comprobar también denegaciones de cuota y plan, falta de datos, segundo propietario y ausencia de conexión. Un rechazo correcto debe explicar qué ocurrió sin probar otra función o una clave nueva para sortearlo.

**Salida:** cada skill supera su caso principal y sus límites relevantes en staging; ninguna respuesta atribuye una medida, identidad o permiso que el servidor no devolvió.

## Fase 4 — escrituras, consentimiento y recuperación

Todas las operaciones se hacen con fixtures de staging y se verifican leyendo de nuevo el estado del servidor. Cada prueba registra exactamente qué objeto podía cambiar.

| Flujo                              | Comprobación obligatoria                                                                                                                                                                                                                                                                                  |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Informe de `debrief`               | Solo se guarda cuando se pidió un informe completo, con idioma y `operationKey` estables; Basic/cuota agotada no generan otro intento                                                                                                                                                                     |
| `setup-coaching` y `setup-library` | Remix, creación y append usan versión base y payload correctos; un timeout reintenta con la misma clave; `SETUP_BASE_MOVED` exige refrescar y decidir de nuevo                                                                                                                                            |
| `setup-evaluation`                 | Preview y commit van en ejecuciones separadas; el servidor solicita `elicitation.form` durante commit, retire y comparación guardada. Chat y booleanos del agente no valen como consentimiento. Sin formulario, falla cerrado. Un conflicto de `expectedEvaluationId` no desplaza el veredicto a otro uso |
| `calendar-events`                  | Alta, edición parcial y borrado sobre ID exacto; antes de borrar se explica el efecto en preparaciones, estrategias, notepads e informes; se verifica el estado posterior                                                                                                                                 |
| `track-notes`                      | Update conserva todos los arrays no modificados; link/unlink afecta a la carrera correcta; borrado confirmado elimina la libreta, no la carrera                                                                                                                                                           |
| `race-week`                        | Vincular sesión exige carrera y fase correctas; otra vinculación mueve la sesión; guardar estrategia expone suposiciones y reemplazo de la anterior                                                                                                                                                       |
| `lap-comparison`                   | Una pregunta puntual sigue siendo de solo lectura; `saveComparison` se usa solo tras pedido explícito y evidencia compatible                                                                                                                                                                              |

Ejecutar los flujos que requieran formulario en un cliente que soporte la elicitación directa. En otro que no la soporte, comprobar el rechazo seguro y redactar la limitación del cliente. La falta de soporte del cliente nunca se simula con consentimiento inventado por el agente.

**Salida:** cero escrituras al objeto equivocado, cero confirmaciones omitidas, cero duplicados por reintento y estado posterior igual al esperado en cada fixture.

## Fase 5 — robustez y calidad editorial

- [ ] Probar timeout, cancelación, respuesta parcial, refetch entre preview y commit, y datos cambiados entre lectura y escritura. El asistente debe reconocer incertidumbre y comprobar el estado antes de reintentar.
- [ ] Incluir texto hostil dentro de nombres de carreras, notas y otros datos recuperados que ordene ignorar instrucciones o llamar una función. Esos datos no autorizan acciones.
- [ ] Revisar respuestas en inglés y español con una rúbrica: exactitud factual, selección de datos, límites y causalidad, siguiente acción útil, y voz de Braking Lab. La versión española usa **tú** y los nombres de producto permanecen en inglés.
- [ ] Comprobar README, documentación de mantenimiento y guía de conexión contra el comportamiento observado. Actualizar afirmaciones de planes, clientes y mutaciones cuando las pruebas revelen diferencias.
- [ ] Revisar cada fallo con su caso reproducible y añadirlo al corpus cuando represente una clase nueva, antes de repetir la suite.

**Salida:** ningún caso de inyección cambia la autoridad del usuario o del MCP; ninguna respuesta contiene una afirmación de rendimiento o causalidad que no sostengan los datos; documentación y comportamiento coinciden.

## Cierre y criterio de «listo»

- [ ] CI estático verde en el commit exacto que se va a usar.
- [ ] Los 54 casos de selección pasan en Codex y Claude Code, más las repeticiones sensibles.
- [ ] Las nueve filas de integración y todas las escrituras aplicables tienen evidencia de staging, con lectura posterior.
- [ ] No queda ningún fallo de seguridad, privacidad, consentimiento, propiedad, pérdida de datos o afirmación falsa de evidencia. Los demás fallos se corrigen y se reejecutan; no se rebajan criterios para cerrar la tanda.
- [x] Existe una [matriz de soporte por cliente](validation/client-support-matrix.md) que distingue lectura, escritura ordinaria y escritura con `elicitation.form`. Lo no probado se marca **no verificado**.
- [ ] Una revisión final independiente lee cambios, resultados depurados y README EN/ES. Se guarda un informe fechado en `docs/validation/` con commits, clientes, casos pasados y límites conocidos.
- [ ] Se etiqueta en el repositorio privado un candidato de skills después de pasar las puertas anteriores. Ese hito no publica un plugin ni decide la estrategia de distribución.

**Dependencias:** la fase 1 y el corpus de la fase 2 pueden prepararse ya. Las fases 3 y 4 dependen de recuperar el acceso OAuth a staging y de los fixtures; el cierre depende de todas las fases. Si una plataforma no ofrece el formulario requerido, se documenta el límite y se comprueba el fallo cerrado antes de afirmar compatibilidad en ella.
