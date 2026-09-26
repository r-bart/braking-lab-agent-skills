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

ChatGPT completó el inicio de sesión y varias consultas de lectura en una cuenta. Claude completó el inicio de sesión, pero el límite de uso de la cuenta impidió la primera respuesta. Claude Code y Codex instalaron el plugin; aún faltan pruebas de sus flujos autenticados. No se ha verificado ningún flujo de escritura o confirmación, y ninguno de los plugins tiene todavía una ficha pública.

Consulta el [registro de validación](docs/validation/2026-09-26-packaging.md) para ver las pruebas y sus límites. El [plan de pruebas](docs/test-plan.md), el [plan de distribución](docs/distribution-plan.md) y las [notas de mantenimiento](docs/maintainers.md) recogen el trabajo previo a la publicación.
