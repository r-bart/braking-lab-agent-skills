# Validación contra staging — 2026-09-26

## Identidad y alcance

- Skills: versión 0.1.1 del repositorio privado `r-bart/braking-lab-agent-skills`; el candidato documental más reciente antes de esta tanda era `d0192aa`.
- Fuente local del MCP: commit `1d123a617` del monorepo; el directorio `apps/mcp-server` estaba limpio. El despliegue remoto devolvió `CATALOG_VERSION=97-90f662d1d158357c`, igual al contrato fijado por las skills. La igualdad del catálogo no certifica que el código desplegado sea ese commit.
- Cliente remoto: conector Braking Lab (STA) de Codex, autenticado como una cuenta sintética Basic. La ejecución opt-in de Vitest usó credenciales locales no registradas en Git y el guard del proyecto Supabase de staging. No se usaron datos de producción.

## Resultado observado

| Capa | Resultado | Alcance real |
| --- | --- | --- |
| MCP remoto | `whoami` confirmó cuenta y plan Basic; `getCapabilities` confirmó la versión de catálogo; `getLatestSession`, `getAllRaces`, `listCarSetups` y `getTrackNotepads` devolvieron el estado vacío esperado. | Es una cuenta sin telemetría ni setups; no valida los nueve recorridos con datos. |
| Permiso Basic | `createTrackNotepad` rechazó la escritura por plan. La llamada anterior había creado un evento sintético; se borró por ID y `getAllRaces` confirmó total cero. | Confirma la denegación y la limpieza, no el CRUD de notas en Plus/Ultra. |
| E2E con base real de staging | `MCP_ACCEPTANCE=1 pnpm test:e2e` ejecutó 37 tests correctos, 2 fallidos y 41 omitidos; terminó con código 1. Entre los correctos hay trazas, aislamiento entre propietarios, transporte MCP local con grants y carreras. | Los tests llaman a código local o a un servidor local sobre la base de staging, no al despliegue remoto. Varios grupos requieren fixtures LMU explícitos que no estaban configurados. |

Las dos aserciones fallidas de `tierA-analysis.e2e.test.ts` esperan deltas numéricos para zonas sin alineación comprobada y pendiente `0` cuando no hay datos. El contrato actual devuelve `null` en ambos casos; los tests unitarios del mismo módulo ya comprueban ese comportamiento. No se considera aprobado el E2E completo mientras esas expectativas y los fixtures opcionales sigan sin resolver.

## Reejecución con fixtures LMU existentes

El [PR #75 del monorepo](https://github.com/r-bart/braking-lab-monorepo/pull/75) corrige esas aserciones sin cambiar código de producto. El archivo afectado pasó **22/22** pruebas sobre staging, además de typecheck, lint y formato.

El generador revisado de fixtures LMU se ejecutó contra la cuenta sintética Ultra. Tras varios rechazos por tasa de subida terminó con `UNKNOWN_SEED_FAILURE`; no se interpretó como éxito. Se inventariaron y borraron **solo** los 10 setups nuevos incompletos y sus 16 blobs canónicos, con verificación de que no quedaban esas filas. Los diez fixtures anteriores permanecieron. Para la siguiente ejecución se fijaron los seis pares de IDs existentes después de comprobar propietario, nombre, estado `ready`, versión 1 y ruta canónica; los IDs se guardaron únicamente en un archivo local privado.

La suite completa con esos fixtures anteriores terminó con **46 tests correctos, 9 fallidos y 25 omitidos**. Los fallos se agrupan en Setup Interview, evaluación y procedencia/remix: el constructor rechaza un valor final discontinuo fuera del dominio exacto revisado o un punto medio no observado. El rechazo evita escribir un setup sin evidencia, pero los casos principales de esas pruebas no pasan. Las omisiones incluyen pruebas que dependen de otras puertas de staging. Este resultado sustituye el anterior como estado E2E más reciente; tampoco habilita una release pública.

Una comprobación de solo lectura de la variante exacta afectada encontró **cero** diales movidos con una base alternativa cuyo resultado también fuera una posición observada y **cuatro** diales no movidos con una base alternativa observada. El generador elegía por intervalo numérico, que no certifica los huecos. El mismo PR ahora selecciona posiciones observadas y puede usar un dial no movido para diferenciar el fixture sintético. En esa tanda pasó typecheck, lint y el contrato estático del generador, pero la generación completa aún no estaba verificada.

## Tanda del 27 de septiembre: fixtures nuevos y E2E

Una primera generación espaciada creó los diez setups base y sus hijos sin rechazos de tasa, pero terminó al intentar retroceder el puntero de la versión activa para borrar una versión de prueba. Staging respondió `AI_SETUP_LATEST_REGRESSION`, como exige el guard. Se verificaron y borraron solo las diez filas sintéticas de esa ejecución y sus 16 versiones. Una inspección posterior halló 15 blobs huérfanos de esos IDs; se eliminaron por ruta canónica individual y la lectura posterior confirmó cero. El generador quedó corregido para comparar dos hijos duraderos en su prueba de no clonación, sin retroceder versiones, y para confirmar el borrado de cada blob antiguo.

La siguiente generación terminó **correctamente**: diez setups nuevos, 15 versiones y doce variables de ID para los seis pares base/version exigidos por E2E, sin rechazos de subida. El barrido eliminó las diez filas anteriores y una comprobación de sus rutas confirmó cero blobs restantes. Los IDs se guardaron solo en un archivo local privado con permisos `0600`. Tras las pruebas y la reparación de los tres punteros, una nueva lectura confirmó diez setups, 15 versiones, cero usos, los seis pares base en v1 y todas las rutas de versión canónicas.

La suite completa contra la base real de staging, usando esos fixtures nuevos, terminó con **49 tests correctos, 6 fallidos y 25 omitidos** (80 en total, código 1). Los fallos de Setup Interview, evaluación, procedencia y remix siguen relacionados con puntos medios o valores finales que el dominio exacto no observa; el servidor los rechaza sin guardar hijos inseguros. Una aserción adicional exige que el fixture IV difiera en un dial *movido* aunque la variante revisada no ofrece tal base alternativa. El test de limpieza también intentaba retroceder el puntero antes de borrar la versión hija. Se corrigió el orden de limpieza en los cinco archivos E2E afectados y se validaron en staging, por separado, el borrado de un hijo/blob y la restauración del fixture RA a v1. Tres punteros sintéticos que la ejecución roja había dejado vacíos se restauraron a v1 y se verificaron. **La suite completa no se ha repetido después de esta corrección del arnés**; las seis fallas funcionales no se dan por resueltas.

Esta ejecución ejercita código local del MCP sobre la base de staging. No prueba por sí sola la versión desplegada del servidor ni la selección y respuesta de las skills en Claude o ChatGPT.

## Reejecución completa con el fixture Alpine — 27 de septiembre

Una lectura de las 524 referencias activas y sus 88 variantes exactas encontró una base alternativa observada para el fixture de construcción IV en `Alpine_A424`. Se regeneraron los diez setups sintéticos con esa variante y el generador terminó correctamente, sin reintentos por tasa. La base IV difiere de su referente en un dial que la derivación mueve, de modo que la aserción de delta relativo conserva su capacidad de detectar una copia de valores absolutos.

Se ajustaron los pedidos E2E para usar valores finales observados. Los casos de punto medio dry/balanced y pasos wet no observados ahora exigen el rechazo concreto y comprueban que no apareció ninguna versión hija ni cambió el puntero. El arnés usa reintentos acotados solo para `UPLOAD_RATE_LIMITED`, respetando el tiempo indicado por staging; no se modificó el constructor del producto ni el guard de dominio exacto.

La suite completa `MCP_ACCEPTANCE=1 pnpm test:e2e` terminó con **78 tests correctos, 0 fallidos y 2 omitidos** en 819,60 segundos (código 0). Los omitidos son `interactive-session.e2e.test.ts` y `staging-transport-smoke.e2e.test.ts`, que requieren sus activaciones y credenciales específicas. Pasaron, entre otros, construcción de Setup Interview (6/6), riesgo e identidad (10/10), procedencia (7/7), remix (4/4), evaluación (12/12), aislamiento entre propietarios (5/5), análisis (22/22), trazas (6/6) y transporte local (3/3). La lectura posterior confirmó **10 setups, 15 versiones, cero usos**, seis bases activas en v1 y rutas de blob canónicas. Typecheck, lint y formato pasaron; la verificación del paquete de skills confirmó las nueve skills, los dos manifests y las 66 funciones del catálogo fijado.

Este resultado valida el código MCP local contra la base real de staging. No ejecuta los dos casos de transporte opt-in, no certifica el despliegue remoto y no constituye una prueba de uso de las skills por Claude o ChatGPT.

## Puertas de salida pendientes

La validación solicitada se ha ejecutado, pero el criterio de «listo» de [`../test-plan.md`](../test-plan.md) **no se cumple**. Falta conectar una cuenta de staging con derechos Plus/Ultra al MCP desplegado y recorrer debrief, comparación, setups, Track Notes y race week con datos; verificar sus escrituras por lectura posterior; probar formularios `elicitation.form` en un cliente compatible; y ejecutar el corpus de 54 prompts en Claude Code. El CLI de Claude informó de límite de gasto mensual y restablecimiento semanal el 1 de octubre a las 19:00 (Madrid). La suite E2E local está verde; las pruebas opt-in de sesión interactiva y transporte remoto siguen pendientes.

Hasta resolver estas puertas, la release sigue siendo privada y preliminar. No hay evidencia suficiente para afirmar soporte funcional completo de las nueve skills ni para enlazar una instalación pública desde la landing.
