# Instalar Race Engineer en Claude

Necesitas una cuenta de Braking Lab para usar tus datos. El repositorio es público. También puedes usar el [instalador interactivo](install-cli.md) para Claude Code.

## Claude Code

1. Registra el marketplace: `claude plugin marketplace add r-bart/braking-lab-agent-skills`.
2. Instala el plugin: `claude plugin install braking-lab-race-engineer@braking-lab`.
3. Abre una sesión nueva. Ejecuta `/mcp` y conecta tu cuenta de Braking Lab cuando Claude lo pida.
4. Pregunta: «Compara mis dos últimas vueltas y dime dónde está la mayor diferencia».

Comprueba la instalación con `claude plugin details braking-lab-race-engineer`. Debe mostrar nueve skills y un servidor MCP. Para actualizar, ejecuta `claude plugin update braking-lab-race-engineer@braking-lab` y abre una sesión nueva. Para retirarlo, ejecuta `claude plugin uninstall braking-lab-race-engineer@braking-lab`.

## Claude chat

Descarga [`braking-lab-claude-0.2.0.zip`](https://github.com/r-bart/braking-lab-agent-skills/releases/download/v0.2.0/braking-lab-claude-0.2.0.zip). En Claude, abre **Personalizar → Plugins → Agregar plugin → Subir plugin** e importa el archivo. La importación se probó en la cuenta Personal: la ficha mostró nueve skills y un conector Braking Lab. Abre **Conectores → Conectar** para autorizar tu cuenta. OAuth se completó en el piloto; la primera tarea con datos quedó bloqueada por el límite de uso mensual de esa cuenta.

Si aparecen dos conexiones «Braking Lab», revisa la conexión MCP que ya tenías antes de instalar el plugin y conserva solo una activa. La skill no concede acceso adicional: los permisos y las confirmaciones dependen de tu cuenta y del servidor.
