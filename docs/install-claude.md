# Instalar Race Engineer en Claude

El piloto necesita una cuenta de Braking Lab y acceso al repositorio privado `r-bart/braking-lab-agent-skills`.

## Claude Code

1. Registra el marketplace: `claude plugin marketplace add r-bart/braking-lab-agent-skills`.
2. Instala el plugin: `claude plugin install braking-lab-race-engineer@braking-lab`. Si usas HTTPS para acceder al repositorio privado, ante un error SSH ejecuta `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1 claude plugin install braking-lab-race-engineer@braking-lab`.
3. Abre una sesión nueva. Ejecuta `/mcp` y conecta tu cuenta de Braking Lab cuando Claude lo pida.
4. Pregunta: «Compara mis dos últimas vueltas y dime dónde está la mayor diferencia».

Comprueba la instalación con `claude plugin details braking-lab-race-engineer`. Debe mostrar nueve skills y un servidor MCP. Para actualizar, ejecuta `claude plugin update braking-lab-race-engineer@braking-lab` y abre una sesión nueva. Para retirarlo, ejecuta `claude plugin uninstall braking-lab-race-engineer@braking-lab`.

## Claude chat

El archivo privado `dist/braking-lab-claude-<versión>.zip` contiene las mismas nueve skills. Impórtalo en la sección de plugins de Claude y conecta Braking Lab desde la pestaña de conectores si Claude no lo ofrece durante la instalación. La importación y el inicio de sesión en Claude chat todavía requieren una prueba con una cuenta piloto; no se anuncia como vía lista hasta completarla.

Si aparecen dos conexiones «Braking Lab», revisa la conexión MCP que ya tenías antes de instalar el plugin y conserva solo una activa. La skill no concede acceso adicional: los permisos y las confirmaciones dependen de tu cuenta y del servidor.
