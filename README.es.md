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

## Prueba Race Engineer

El paquete privado de prueba incluye las nueve skills y la conexión al MCP de Race Engineer. Sigue la guía para [Claude](docs/install-claude.md), [ChatGPT](docs/install-chatgpt.md) u [otro agente](docs/install-other-agents.md). Después inicia sesión en la cuenta de Braking Lab donde están tus datos y pregunta con tus propias palabras.

Las skills guían tareas habituales. No limitan lo que puede hacer el MCP, no cambian tu plan ni conceden más acceso. Tu cliente conectado puede seguir usando otras funciones del Race Engineer. Las acciones que guardan o cambian datos siguen sujetas a los permisos de tu cuenta y a las confirmaciones del servidor. [Consulta a qué datos puede acceder el Race Engineer](https://www.brakinglab.com/es/docs/race-engineer/security).

## Estado actual

Los paquetes para Claude y Agent Plugins se construyen desde las mismas nueve skills. Sus manifiestos y estructura han pasado la validación local. Faltan las pruebas reales con una cuenta autenticada, incluida la selección de skills, los límites del plan y las confirmaciones. Ningún plugin tiene aún una ficha pública en su directorio.

Sigue el [plan de pruebas](docs/test-plan.md) para las comprobaciones pendientes. El [plan de distribución](docs/distribution-plan.md) recoge los pasos para Claude, ChatGPT y otros agentes cuando terminen las pruebas; las [notas para mantenimiento](docs/maintainers.md) conservan los detalles de empaquetado.
