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

## Instala la beta pública

En macOS o Linux, ejecuta el instalador interactivo:

```sh
curl -fsSL https://www.brakinglab.com/install.sh | sh
```

Elige agente, ubicación y skills. El instalador descarga una versión fija, comprueba su SHA-256 y configura el MCP de Braking Lab en **Codex** o **Claude Code** si sus CLI están disponibles. Después autorizas tu cuenta de Braking Lab desde ese cliente. Para **Cursor** u otro agente local, instala las skills y muestra la URL del MCP; conéctalo en tu agente antes de preguntar por tus datos. [Detalles de instalación y comprobación](docs/install-cli.md).

También puedes usar [`npx skills add r-bart/braking-lab-agent-skills`](https://www.skills.sh/docs/cli) para instalar las skills con el CLI existente. Esa vía no configura el MCP. Para el plugin nativo de Claude Code, sigue la [guía de Claude](docs/install-claude.md). La ficha pública de ChatGPT sigue en preparación; consulta el [estado de ChatGPT](docs/install-chatgpt.md).

Necesitas una cuenta de Braking Lab para las respuestas basadas en datos. El instalador nunca pide tu contraseña ni un token de Braking Lab. OAuth ocurre en tu asistente.

Las skills guían tareas habituales. No limitan lo que puede hacer el MCP, no cambian tu plan ni conceden más acceso. Tu cliente conectado puede seguir usando otras funciones del Race Engineer. Las acciones que guardan o cambian datos siguen sujetas a los permisos de tu cuenta y a las confirmaciones del servidor. [Consulta a qué datos puede acceder el Race Engineer](https://www.brakinglab.com/es/docs/race-engineer/security).

## Estado de la beta

Las nueve skills superaron las comprobaciones de formato y catálogo MCP. ChatGPT completó OAuth y consultas de lectura en una cuenta; Codex en staging verificó alta, edición y borrado de una carrera con lectura posterior. Quedan por comprobar la primera respuesta con datos en Claude Code y los flujos completos de otros clientes. La [matriz de soporte](docs/validation/client-support-matrix.md) registra lo observado. Instalar las skills por sí solo no conecta el Race Engineer.

El código, el instalador y los archivos de versión están en este repositorio. Las [notas para mantenimiento](docs/maintainers.md) explican el empaquetado y las comprobaciones.
