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
- GitHub Actions completó correctamente la validación de esquemas, las nueve skills y la generación de los tres archivos en el commit `e4052e0`. La primera ejecución había fallado en la configuración del caché de pip; se corrigió `cache-dependency-path`.

## Pendiente antes de declarar soporte completo

- OAuth y `whoami` en la cuenta piloto; no se autorizó ninguna cuenta de Braking Lab durante esta validación.
- Primer debrief y una escritura ordinaria en ChatGPT, con lectura posterior; pruebas de límites y rechazo seguro según `docs/test-plan.md`.
- Prueba funcional en Claude Code. La instalación y la validación local pasaron, pero la ejecución del modelo quedó detenida por el límite mensual de Claude Code de esta cuenta.
- OAuth y primer uso en Claude chat y en una segunda cuenta de ChatGPT; comprobar actualización y desinstalación.
- Confirmar la elegibilidad del mapeo de la app registrada al preparar el envío público de OpenAI. El registro personal sirve para el piloto, no equivale a una ficha publicada.

El repositorio y los archivos siguen privados. Esta validación prueba el empaquetado y la importación; no prueba la calidad de las respuestas ni los flujos autenticados.
