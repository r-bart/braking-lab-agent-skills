# Instalar Race Engineer en Claude

El piloto necesita una cuenta de Braking Lab y acceso al repositorio privado `r-bart/braking-lab-agent-skills`.

## Claude Code

1. Registra el marketplace: `claude plugin marketplace add r-bart/braking-lab-agent-skills`.
2. Instala el plugin: `claude plugin install braking-lab-race-engineer@braking-lab`. Si usas HTTPS para acceder al repositorio privado, ante un error SSH ejecuta `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1 claude plugin install braking-lab-race-engineer@braking-lab`.
3. Abre una sesión nueva. Ejecuta `/mcp` y conecta tu cuenta de Braking Lab cuando Claude lo pida.
4. Pregunta: «Compara mis dos últimas vueltas y dime dónde está la mayor diferencia».

Comprueba la instalación con `claude plugin details braking-lab-race-engineer`. Debe mostrar nueve skills y un servidor MCP. Para actualizar mediante HTTPS, ejecuta `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1 claude plugin update braking-lab-race-engineer@braking-lab` y abre una sesión nueva. Para retirarlo, ejecuta `claude plugin uninstall braking-lab-race-engineer@braking-lab`.

## Claude chat

Descarga [`braking-lab-claude-0.1.1.zip`](https://github.com/r-bart/braking-lab-agent-skills/releases/download/v0.1.1/braking-lab-claude-0.1.1.zip) de la versión privada. En Claude, abre **Personalizar → Plugins → Agregar plugin → Subir plugin** e importa el archivo. La importación se probó en la cuenta Personal: la ficha mostró nueve skills y un conector Braking Lab. Abre **Conectores → Conectar** para autorizar tu cuenta. OAuth se completó en el piloto; la primera tarea con datos quedó bloqueada por el límite de uso mensual de esa cuenta.

Si aparecen dos conexiones «Braking Lab», revisa la conexión MCP que ya tenías antes de instalar el plugin y conserva solo una activa. La skill no concede acceso adicional: los permisos y las confirmaciones dependen de tu cuenta y del servidor.
