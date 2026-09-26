# Skills del Race Engineer de Braking Lab

[English](README.md)

Pregunta por la vuelta que acabas de hacer, la carrera que estás preparando o el siguiente cambio de setup que quieres probar. Estas skills ayudan a tu asistente de IA a usar el **Race Engineer de Braking Lab** con tus propios datos. Mantienen las respuestas cerca de la evidencia: si falta una señal, no se presenta como una medición; un cambio de setup sigue siendo una hipótesis hasta que lo pruebas en pista.

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

## Prueba las skills

1. [Conecta el MCP del Race Engineer](https://www.brakinglab.com/es/docs/race-engineer/mcp-setup) e inicia sesión con la cuenta de Braking Lab donde están tus datos. Las skills no conectan ni autentican el MCP por sí solas.
2. Clona el [repositorio privado](https://github.com/r-bart/braking-lab-agent-skills) con una cuenta que tenga acceso. Para una prueba local, enlaza o copia sus nueve carpetas `skills/<name>/` en `~/.codex/skills/` para Codex o `~/.claude/skills/` para Claude Code. Inicia una sesión nueva si tu cliente todavía no las detecta.
3. Pregunta con tus propias palabras. El asistente elige la skill relevante; también puedes invocarla por nombre en los clientes que lo permitan.

Las skills guían tareas habituales. No limitan lo que puede hacer el MCP, no cambian tu plan ni conceden más acceso. Tu cliente conectado puede seguir usando otras funciones del Race Engineer. Las acciones que guardan o cambian datos siguen sujetas a los permisos de tu cuenta y a las confirmaciones del servidor. [Consulta a qué datos puede acceder el Race Engineer](https://www.brakinglab.com/es/docs/race-engineer/security).

## Estado actual

Las nueve skills están escritas. Se ha validado su formato y se han contrastado los nombres de las funciones con el catálogo del MCP. Faltan las pruebas reales con una cuenta de test autenticada, incluida la selección de skills, los límites del plan y las confirmaciones. Este repositorio todavía no contiene un plugin para Claude o Codex ni una publicación en sus directorios.

Sigue el [plan de pruebas](docs/test-plan.md) para las comprobaciones pendientes. El [plan de distribución](docs/distribution-plan.md) recoge los pasos para Claude, ChatGPT y otros agentes cuando terminen las pruebas; las [notas para mantenimiento](docs/maintainers.md) conservan los detalles de empaquetado.
