# Validación del empaquetado — 2026-09-26

## Resultado comprobado

- `scripts/verify_package.py`: pasaron los esquemas Agent Plugins 1.0.0, las nueve skills con `agentskills validate`, la identidad de los manifiestos y la URL única de producción.
- `claude plugin validate` con `--strict`: pasaron el marketplace y el plugin en una carpeta temporal sin marketplace.
- El endpoint público `https://mcp.brakinglab.com/mcp` devolvió `401` sin autenticación. Las páginas públicas de producto, privacidad y términos devolvieron `200`.
- ChatGPT importó el primer archivo de prueba y mostró nueve skills. Este archivo incluía tanto la app registrada como el MCP portable y la ficha mostró dos entradas de conexión; por eso se separaron los archivos.
- ChatGPT importó una variante de prueba con **solo la app registrada** y mostró **Apps 1, Skills 9**, sin una entrada MCP duplicada. El manifiesto de prueba tenía un nombre interno distinto para evitar la colisión con el primer archivo ya importado. El archivo distribuible de ChatGPT usa la misma estructura y el nombre interno definitivo `braking-lab-race-engineer`.
- ChatGPT importó también el archivo definitivo `braking-lab-chatgpt-0.1.0.zip` en la cuenta Personal. La [ficha privada](https://chatgpt.com/plugins/Plugin_3ea10eecd6008191a6885f644dbdc9a2) mostró **Apps 1, Skills 9**, sin una segunda entrada MCP. Al pulsar «Install plugin», ChatGPT abrió el diálogo para conectar la app; se cerró antes de conceder acceso a datos de la cuenta.
- Claude Code registró el marketplace privado y, con `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1`, instaló `braking-lab-race-engineer@braking-lab` versión `0.1.0`. `claude plugin details` mostró nueve skills y un servidor MCP; `claude plugin list` lo mostró habilitado. Sin esa variable, la instalación intentó SSH y falló por falta de clave GitHub en esta máquina.
- Claude chat importó `braking-lab-claude-0.1.0.zip` como plugin personal. La ficha mostró versión `0.1.0`, nueve skills y un conector Braking Lab. El plugin quedó activado y el conector mostró «Sin conexión»; no se inició OAuth.
- Codex registró primero el marketplace local y después repitió la instalación desde el repositorio privado por HTTPS. `codex plugin list --json` mostró `braking-lab-race-engineer@braking-lab` versión `0.1.0` habilitado, con origen Git y política de autenticación `ON_USE`. El caché contenía `plugin.json`, `mcp.json` y las nueve skills. Todavía falta una sesión nueva con OAuth y tareas reales.
- En una sesión nueva de Codex, las nueve skills aparecieron en el contexto. El inicio del MCP de Braking Lab devolvió `Auth required`, que es coherente con un conector todavía sin autorizar. La cuenta ya tenía copias locales de esas skills, por lo que esta prueba no demuestra aún selección automática exclusiva del plugin.
- `DISABLE_TELEMETRY=1 npx skills add r-bart/braking-lab-agent-skills --list` clonó el repositorio privado con las credenciales Git locales y enumeró las nueve skills. Es una comprobación de descubrimiento; el comando no instaló skills ni configuró el MCP.
- Los documentos OAuth públicos del MCP anunciaron `race-engineer:read`, `race-engineer:write`, autorización `code` con PKCE S256 y registro dinámico. El descubrimiento no sustituye al inicio de sesión en un cliente.
- GitHub Actions completó correctamente la validación de esquemas, las nueve skills y la generación de los tres archivos en el commit `e4052e0`. La primera ejecución había fallado en la configuración del caché de pip; se corrigió `cache-dependency-path`.
- La ejecución de GitHub Actions del commit `a4d9e22` pasó también la comprobación SHA-256 de los archivos. La versión preliminar privada [`v0.1.0`](https://github.com/r-bart/braking-lab-agent-skills/releases/tag/v0.1.0) adjunta los tres ZIP y `SHA256SUMS`.

## OAuth y lectura del piloto

Con autorización expresa del propietario de la cuenta, ChatGPT y Claude completaron OAuth contra el MCP de producción. Las fichas de ambos clientes mostraron la conexión activa. ChatGPT respondió correctamente a una consulta de cuenta y plan, enumeró las tres sesiones más recientes y comparó dos vueltas limpias de una misma sesión. La comparación identificó la vuelta de referencia, presentó deltas medidos y señaló una zona de frenada sin correspondencia. El historial de las respuestas indicó interacción con Braking Lab Race Engineer. No se solicitó ninguna escritura ni se guardaron datos en estas pruebas; los identificadores de cuenta y las sesiones privadas se omiten de este registro. Estas tres consultas seleccionaron el plugin explícitamente en el compositor.

En un chat nuevo, sin seleccionar el plugin ni mencionarlo por su nombre, «¿Qué plan tengo ahora mismo en Braking Lab? Compruébalo en mi cuenta y no cambies nada» produjo una respuesta correcta y el historial indicó «Interacted with Braking Lab Race Engineer». Esto prueba la activación natural de la integración para esa petición, pero la interfaz no muestra qué `SKILL.md` eligió internamente.

Claude chat no pudo ejecutar la primera consulta tras conectar: la cuenta alcanzó su límite mensual de uso y la interfaz devolvió el borrador sin respuesta. La conexión quedó visible como «Conectado». Claude Code había mostrado el mismo límite antes de conectar.

## Comprobación adicional del paquete privado

En el commit `48465b5` se reconstruyeron los tres ZIP `0.1.1` y se verificaron todos con `SHA256SUMS`. La inspección de su contenido no encontró referencias a staging, fixtures `e2e-`, Supabase ni marcadores de clave privada. Un barrido de los 258 objetos del historial Git buscó patrones de claves OpenAI, GitHub y Supabase, claves privadas y asignaciones de secreto; no encontró coincidencias. Estas comprobaciones acotan errores de empaquetado evidentes, pero no sustituyen la revisión completa de privacidad, licencia, soporte y funcionamiento de clientes exigida antes de hacer público el repositorio.

## Pendiente antes de declarar soporte completo

- Primer debrief y una escritura ordinaria en ChatGPT, con lectura posterior; pruebas de límites y rechazo seguro según `../test-plan.md`.
- Primera respuesta basada en datos en Claude chat y Claude Code cuando se restablezca el límite mensual.
- Prueba con una segunda cuenta de ChatGPT; comprobar actualización y desinstalación.
- Para el envío público de OpenAI, crear un borrador **With MCP** con la URL de producción y las skills. El registro personal sirve para el piloto; el portal no admite referenciarlo como integración existente. Antes del envío, implementar y verificar en el servidor la prueba de dominio y el soporte OAuth de `openid`, `email` y UserInfo exigidos para las restricciones de dominio de workspace.

El repositorio y los archivos siguen privados. Esta validación prueba empaquetado, importación, OAuth y las consultas de lectura descritas; quedan pendientes la evaluación completa de respuestas, otros clientes y los flujos de escritura y confirmación.
