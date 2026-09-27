# Race Engineer en tu asistente de IA

[English](README.md)

Pregunta por la vuelta que acabas de hacer, la carrera que estás preparando o el siguiente cambio de setup que quieres probar. Estas nueve skills ayudan a tu asistente de IA a usar el **Race Engineer de Braking Lab** con tus propios datos. Si falta una señal, la respuesta debe decirlo. Un cambio de setup sigue siendo una hipótesis hasta que lo pruebas en pista.

| Puedes preguntar                                   | Skill              |
| -------------------------------------------------- | ------------------ |
| «¿Qué puede hacer mi Race Engineer?»               | `race-engineer`    |
| «¿Dónde perdí tiempo en mi última sesión en Spa?»  | `debrief`          |
| «El coche subvira a la salida. ¿Qué cambiarías?»   | `setup-coaching`   |
| «Enséñame las versiones de mi setup de LMU.»       | `setup-library`    |
| «Añade la carrera del sábado al calendario.»       | `calendar-events`  |
| «¿Ayudó el cambio de setup después de probarlo?»   | `setup-evaluation` |
| «Guarda mi referencia de frenada para la curva 3.» | `track-notes`      |
| «¿Qué debería practicar antes de la carrera?»      | `race-week`        |
| «Compara mis dos últimas vueltas.»                 | `lap-comparison`   |

## Participa en el piloto privado

Necesitas acceso a este repositorio privado y una cuenta de Braking Lab con tus datos de conducción. Descarga el paquete de la [versión preliminar 0.1.1](https://github.com/r-bart/braking-lab-agent-skills/releases/tag/v0.1.1) y sigue la guía para [Claude](docs/install-claude.md), [ChatGPT](docs/install-chatgpt.md), [Codex](docs/install-codex.md) u [otro agente](docs/install-other-agents.md). Conecta tu cuenta de Braking Lab en el asistente y pregunta con tus propias palabras.

Las skills guían tareas habituales. No limitan lo que puede hacer el MCP, no cambian tu plan ni conceden más acceso. Tu cliente conectado puede seguir usando otras funciones del Race Engineer. Las acciones que guardan o cambian datos siguen sujetas a los permisos de tu cuenta y a las confirmaciones del servidor. [Consulta a qué datos puede acceder el Race Engineer](https://www.brakinglab.com/es/docs/race-engineer/security).

## Estado del piloto

ChatGPT completó el inicio de sesión y varias consultas de lectura en una cuenta. La versión 0.1.1 está instalada en ChatGPT, Claude, Claude Code y Codex. Codex cargó la skill esperada en los 54 casos de selección en español e inglés. El conector de staging de Codex también verificó el alta, la edición y el borrado de una carrera sintética con lectura posterior; una cuenta Basic rechazó correctamente la creación de Track Notes. Los 80 casos del arnés MCP pasaron en tres tandas: 78 contra la base de staging con código local, uno de protocolo interactivo contra el MCP desplegado y uno de orquestación hermética. Claude Code sigue bloqueado por el límite de uso de la cuenta. Los nueve recorridos con datos, los formularios de consentimiento en clientes reales y el soporte de escritura por cliente aún no están verificados. Ninguno de los plugins tiene todavía una ficha pública.

Consulta la [matriz de soporte por cliente](docs/validation/client-support-matrix.md), los [resultados de pruebas actuales](docs/validation/2026-09-26-test-run.md), la [validación de staging](docs/validation/2026-09-26-staging-validation.md) y el [registro de empaquetado](docs/validation/2026-09-26-packaging.md) para ver las evidencias y sus límites. El [plan de pruebas](docs/test-plan.md), el [plan de distribución](docs/distribution-plan.md) y las [notas de mantenimiento](docs/maintainers.md) recogen el trabajo previo a la publicación.
