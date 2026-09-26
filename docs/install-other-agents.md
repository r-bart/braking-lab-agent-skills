# Race Engineer en otros agentes

El paquete portable tiene `plugin.json`, `mcp.json` y las nueve skills en `skills/`. Si tu cliente admite **Agent Plugins**, instala el repositorio o descarga [`braking-lab-portable-0.1.0.zip`](https://github.com/r-bart/braking-lab-agent-skills/releases/download/v0.1.0/braking-lab-portable-0.1.0.zip) y comprueba que carga también el servidor MCP `https://mcp.brakinglab.com/mcp`. Autoriza tu cuenta de Braking Lab desde el propio cliente.

Si tu cliente solo instala Agent Skills, puedes usar `npx skills add r-bart/braking-lab-agent-skills -g` cuando tengas acceso al repositorio. Ese comando instala **solo las skills**: configura por separado un servidor MCP Streamable HTTP con la URL anterior y completa OAuth. El CLI de terceros envía telemetría anónima de instalación por defecto; puedes desactivarla con `DISABLE_TELEMETRY=1`.

No se anuncia compatibilidad de un cliente por leer el manifiesto. Debe superar una instalación real, OAuth y una pregunta de lectura. Las operaciones que requieren confirmación directa mediante `elicitation.form` pueden no estar disponibles; el servidor debe rechazarlas de forma segura si el cliente no ofrece esa capacidad.
