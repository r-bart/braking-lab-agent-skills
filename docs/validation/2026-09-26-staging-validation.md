# Validación contra staging — 2026-09-26

## Identidad y alcance

- Skills: commit `211ed06` del repositorio privado `r-bart/braking-lab-agent-skills`.
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

Una comprobación de solo lectura de la variante exacta afectada encontró **cero** diales movidos con una base alternativa cuyo resultado también fuera una posición observada y **cuatro** diales no movidos con una base alternativa observada. El generador elegía por intervalo numérico, que no certifica los huecos. El mismo PR ahora selecciona posiciones observadas y puede usar un dial no movido para diferenciar el fixture sintético. Pasó typecheck, lint y el contrato estático del generador; **la nueva generación completa sigue sin verificar** por el límite de subidas.

## Puertas de salida pendientes

La validación solicitada se ha ejecutado, pero el criterio de «listo» de [`../test-plan.md`](../test-plan.md) **no se cumple**. Falta conectar una cuenta de staging con derechos Plus/Ultra al MCP desplegado y recorrer debrief, comparación, setups, Track Notes y race week con datos; verificar sus escrituras por lectura posterior; probar formularios `elicitation.form` en un cliente compatible; y ejecutar el corpus de 54 prompts en Claude Code. El CLI de Claude informó de límite de gasto mensual y restablecimiento semanal el 1 de octubre a las 19:00 (Madrid). La suite E2E general sigue roja por los rechazos de dominio exacto en los casos LMU.

Hasta resolver estas puertas, la release sigue siendo privada y preliminar. No hay evidencia suficiente para afirmar soporte funcional completo de las nueve skills ni para enlazar una instalación pública desde la landing.
