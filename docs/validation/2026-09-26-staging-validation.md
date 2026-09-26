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

## Puertas de salida pendientes

La validación solicitada se ha ejecutado, pero el criterio de «listo» de [`../test-plan.md`](../test-plan.md) **no se cumple**. Faltan fixtures y cuenta de staging con derechos Plus/Ultra para los flujos principales de debrief, comparación, setups, Track Notes y race week en el MCP desplegado; lectura posterior de sus escrituras; formularios `elicitation.form` en un cliente compatible; y el corpus de 54 prompts en Claude Code, bloqueado por el límite de uso observado. La suite E2E general está roja y algunos grupos no corren sin IDs de fixtures propiedad del piloto.

Hasta resolver estas puertas, la release sigue siendo privada y preliminar. No hay evidencia suficiente para afirmar soporte funcional completo de las nueve skills ni para enlazar una instalación pública desde la landing.
