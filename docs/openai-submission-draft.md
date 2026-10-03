# Borrador del envío público a OpenAI

Estado: preparación interna. No enviar hasta que la identidad esté aprobada y las pruebas con la cuenta demo de producción reproduzcan los resultados esperados. El portal será la fuente final para los campos y la prueba de dominio.

## Ficha

- Nombre: **Braking Lab Race Engineer**
- Descripción breve: **Understand your laps and prepare your next race.**
- Descripción: **Review your Braking Lab sessions, compare laps, prepare races and explore setup changes using your own data. Race Engineer makes the evidence and its limits clear, so you know what to try next.**
- Sitio: `https://www.brakinglab.com/en/features/race-engineer`
- Privacidad: `https://www.brakinglab.com/en/privacy`
- Términos: `https://www.brakinglab.com/en/terms`
- MCP universal: `https://mcp.brakinglab.com/mcp`
- Icono: `assets/braking-lab-v5.png`
- Categoría propuesta: Productivity. Confirmar las categorías disponibles en el portal.
- Soporte: confirmar una URL pública de ayuda antes de rellenar el campo.

Los textos de la ficha son propuestas sujetas a comprobar el comportamiento final. El publicador será Roberto como desarrollador individual cuando OpenAI apruebe su verificación.

## Prompts iniciales

1. “Review my latest session and show where I lost time.”
2. “Compare my last two laps and explain the biggest difference.”
3. “What should I practice before my next race?”

## Casos positivos para revisión

Cada caso empieza comprobando `whoami` para evitar interpretar datos de otra cuenta. Sustituir las referencias genéricas por identificadores y datos reales de la cuenta demo, y ejecutar cada prompt antes de copiarlo al portal.

| Caso            | Prompt para el revisor                                                                                                           | Comportamiento esperado                                                                                                                                           | Datos que debe tener la cuenta demo                                                                                                                 |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1 · debrief    | “Review my latest telemetry session. Give me up to three practice priorities.”                                                   | Seleccionar la última sesión propia, consultar sus señales disponibles y explicar observaciones, hipótesis y límites; no guardar un informe sin pedirlo.          | Una sesión reciente con telemetría y análisis disponible.                                                                                           |
| P2 · vueltas    | “Compare my best clean lap with another lap from that same session. Where was the largest measured difference?”                  | Identificar dos vueltas compatibles, fijar la referencia, usar `compareLaps` y describir diferencias medidas sin inventar datos nulos.                            | Dos vueltas propias comparables y limpias en una sesión.                                                                                            |
| P3 · carrera    | “What should I practice for my next race?”                                                                                       | Seleccionar la próxima carrera, revisar preparación y sesiones vinculadas y proponer un plan breve sin presentar combustible o neumáticos no medidos como hechos. | Una carrera futura y datos de preparación o práctica vinculada.                                                                                     |
| P4 · setup      | “Show me the versions of my latest LMU setup and explain what is known about each.”                                              | Encontrar el setup propio y mostrar versiones, origen y límites; no afirmar que una versión fue conducida sin atribución.                                         | Un setup LMU con al menos dos versiones.                                                                                                            |
| P5 · calendario | “Add a test race named Reviewer Demo to my calendar for [fecha futura concreta], using [simulador, coche y circuito concretos].” | Comprobar duplicados, crear un único evento y devolver su identidad; la lectura posterior confirma el alta.                                                       | Cuenta demo con permiso de calendario; elegir una fecha y un contexto fijo antes del envío. Restaurar el estado de la cuenta demo entre revisiones. |

## Casos negativos para revisión

| Caso                | Prompt o situación                                                                | Comportamiento esperado                                                                                                   | Por qué no se completa                                                                   |
| ------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| N1 · datos ausentes | “Tell me my exact braking point for Turn 3 from a session with no braking trace.” | Indicar que falta la señal; no inventar un punto exacto.                                                                  | La telemetría disponible no sustenta esa medida. Preparar una sesión demo sin esa señal. |
| N2 · causalidad     | “Prove that my setup change caused the lap-time improvement from these two runs.” | Presentar la comparación como observacional y explicar qué atribución y repetición faltan.                                | Dos tandas no prueban causalidad ni constituyen evidencia A/B/A.                         |
| N3 · borrado        | “Delete my next race right now.”                                                  | Identificar la carrera exacta y explicar consecuencias; pedir confirmación explícita antes de llamar a `deleteRaceEvent`. | El borrado es irreversible y puede quitar preparación, estrategia y enlaces.             |

## Antes de enviar

- Confirmar identidad aprobada y abrir un borrador **With MCP**.
- Verificar en producción el catálogo y las anotaciones de todas las herramientas; volver a escanear después de cualquier cambio.
- Completar OAuth para dominios de workspace y probar el UserInfo Endpoint.
- Servir el token exacto que genere el portal en `/.well-known/openai-apps-challenge`.
- Crear la cuenta demo de producción con credenciales de revisor sin MFA ni confirmación por correo; cargar solo datos sintéticos y ejecutar los ocho casos.
- Grabar la demostración y completar país, soporte, ficha, políticas y notas de la versión inicial.
- Revisar la ficha completa antes de seleccionar **Submit for Review**. La aprobación de OpenAI y la publicación posterior son estados distintos.
