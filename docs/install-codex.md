# Instalar Race Engineer en Codex

Necesitas una cuenta de Braking Lab. La forma más corta en macOS o Linux es el [instalador interactivo](install-cli.md), que instala skills y configura el MCP de Codex.

1. Registra el catálogo: `codex plugin marketplace add https://github.com/r-bart/braking-lab-agent-skills.git`.
2. Instala el plugin: `codex plugin add braking-lab-race-engineer@braking-lab`.
3. Abre una sesión nueva y conecta la cuenta de Braking Lab cuando Codex lo solicite.
4. Pregunta: «Compara mis dos últimas vueltas y dime dónde está la mayor diferencia».

Comprueba que `codex plugin list` muestra `braking-lab-race-engineer@braking-lab` habilitado. La instalación del catálogo y el plugin se probaron localmente; OAuth, selección automática de skills y respuestas basadas en datos todavía necesitan una prueba completa con este paquete público. Usa el plugin o el instalador para las mismas skills, evitando dos copias activas.

Para actualizar la fuente Git, ejecuta `codex plugin marketplace upgrade braking-lab` y vuelve a instalar la versión nueva. Para retirarlo, ejecuta `codex plugin remove braking-lab-race-engineer@braking-lab`. Desinstalarlo no borra tus datos de Braking Lab.
