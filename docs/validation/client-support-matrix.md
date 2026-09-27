# Matriz de soporte observada — piloto privado

Fecha: 2026-09-26. Paquete: `v0.1.1`. «No verificado» significa que no se ha completado una prueba de extremo a extremo en ese cliente; no implica que la función sea incompatible.

| Cliente | Instalación y skills | OAuth y lectura | Escritura ordinaria | `elicitation.form` | Evidencia y límite |
| --- | --- | --- | --- | --- | --- |
| ChatGPT chat | Nueve skills importadas | Inicio de sesión y consultas de lectura en una cuenta | No verificado | No verificado | [Registro del piloto](2026-09-26-test-run.md); falta repetir con otra cuenta y fixtures. |
| Claude chat | Nueve skills importadas | OAuth completado; respuesta no verificada | No verificado | No verificado | El límite de uso de la cuenta impidió la primera respuesta. |
| Claude Code | Plugin 0.1.1 y nueve skills detectadas | No verificado | No verificado | No verificado | El CLI informó de límite de gasto mensual; restablecimiento semanal indicado para el 1 de octubre a las 19:00 (Madrid). |
| Codex Desktop | Nueve skills instaladas; selección de skill en una conversación observada | Conector de staging autenticado como cuenta Basic; identidad, catálogo y lecturas vacías verificados | Alta, edición y borrado de una carrera sintética con lectura posterior; Track Notes rechazado por plan Basic | No verificado | [Validación de staging](2026-09-26-staging-validation.md); faltan datos y plan Plus/Ultra en el cliente remoto. |
| Codex CLI | Plugin y nueve skills detectados; selección correcta en 54/54 prompts bilingües sin llamar al MCP | No verificado | No verificado | No verificado | La política del CLI denegó la aprobación de la conexión MCP en la prueba natural. |

Los tests locales con SDK y base de staging demuestran contratos del servidor, pero **no** sustituyen una ejecución en ChatGPT, Claude o Codex. No se anuncia una mutación con formulario como compatible hasta observar la elicitación directa y la lectura posterior en ese cliente. Los rechazos por plan son un resultado correcto y no autorizan reintentar con otra credencial.

## Actualización de distribución pública — 2026-09-27

La instalación de `v0.2.0` se probó desde el repositorio público con una configuración de Claude Code vacía, sin clave SSH: `claude plugin marketplace add r-bart/braking-lab-agent-skills`, `claude plugin install braking-lab-race-engineer@braking-lab --yes` y `claude plugin details braking-lab-race-engineer`. El inventario mostró las nueve skills y un servidor MCP. Esto verifica la instalación; la primera respuesta de Claude Code con datos de una cuenta sigue sin verificarse.

El instalador público se probó en un proyecto temporal con las nueve skills, actualización de una instalación gestionada, rechazo de colisiones y configuración MCP simulada para Codex. La ruta `/install.sh` se comprobó en las previews de `develop` y `main` de Vercel. En producción, `curl -fsSL https://www.brakinglab.com/install.sh | sh -s -- --list` enumeró las nueve skills y una instalación completa en un proyecto temporal colocó nueve archivos `SKILL.md`.
