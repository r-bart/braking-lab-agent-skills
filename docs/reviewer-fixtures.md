# Cuenta del reviewer con contenido ficticio

**Pendiente de crear.** El propietario confirmó el 5 de octubre de 2026 que no existe cuenta de prueba y pidió dejar esta tarea preparada. No se han creado usuarios ni datos en producción durante esta preparación.

## Identidad y acceso

Crear una cuenta exclusiva para revisión, con correo bajo control de Braking Lab y verificado una vez por el operador. El reviewer debe poder entrar sin MFA, códigos por SMS ni confirmaciones de correo adicionales en cada acceso. La cuenta no contendrá información de pilotos reales, tarjetas ni acceso de administrador. Proporcionar el acceso existente necesario para los casos de revisión, con expiración posterior al período de revisión; no hacer que el reviewer compre un plan.

Guardar las credenciales en el campo seguro de testing del portal de OpenAI. Nunca en `plugin.json`, un ZIP, Git, una URL de vídeo o este documento. Mantener un responsable para desbloqueos y rotación posterior. El manifiesto no incorpora `testing_instructions` ni credenciales privadas.

## Contenido a preparar

| Elemento | Contenido ficticio | Aceptación |
| --- | --- | --- |
| Perfil | Nombre visible `Braking Lab Reviewer Demo` | `ray_whoami` devuelve esta cuenta; identidad distinta de la cuenta real. |
| Telemetría reciente | Una sesión sintética identificada como demo, circuito/coche/simulador compatibles; tres vueltas limpias con trazas de freno, velocidad y distancia coherentes | Última sesión seleccionable; `getSessionDetail`, `getBrakingZones` y `compareLaps` devuelven señales reales del fixture. No simular una medición ausente. |
| Señales incompletas | Otra sesión sintética, claramente marcada, sin una señal de freno | Una consulta a esa sesión explica la ausencia; no inventa un punto de frenada. Este es un recorrido adicional, no uno de los tres negativos de no invocación. |
| Calendario | Evento `Reviewer Demo Race` con fecha concreta siete días después del envío; contexto compatible con la sesión | `getUpcomingRaces({})` lo devuelve. Vincular práctica y preparar notas; refrescar su fecha si caduca durante revisión. |
| Setup propio LMU | `Reviewer Demo Setup`, dos versiones válidas y legibles, con procedencia sintética explícita | La biblioteca y las versiones son consultables. No atribuir una versión a una tanda si no existe evidencia verificable del vínculo. No incorporar corpus privados. |
| Notas de pista | Un único notepad `Reviewer Demo Notes`, con generalNotes base, una nota de curva, un pin y un vídeo público seguro opcional | P5 añade una sola línea y conserva los otros campos. El reviewer tiene permisos normales de escritura sobre este fixture. |
| Preferencias | Idioma inglés, unidades métricas, densidad comfortable | Cambiar ES/EN y unidades refleja preferencias; restaurar antes del vídeo. |

Generar/importar sesiones mediante las rutas normales de Capture y de importación compatibles con el simulador. Usar setups de prueba propios o fixtures que puedan compartirse legalmente. No copiar telemetría de la cuenta del propietario ni insertar a mano filas que omitan relaciones, objetos y permisos requeridos.

## Ejecución y mantenimiento

1. Seleccionar siempre la conexión demo y confirmar identidad antes de ejecutar los ocho prompts de `plugin.json`.
2. Guardar un registro redactado de resultado esperado/real; no guardar correo, tokens o credenciales en el reporte.
3. P1–P4 son lecturas. P5 edita únicamente el notepad demo; no borra carreras ni llama a imports/associations consent-sensitive.
4. Tras P5, leer de nuevo el notepad. Verificar una sola línea `Reviewer practice: check brake release consistency`, y que notas de curva, pins y vídeos no cambien.
5. Antes de cada nueva grabación, restaurar únicamente `generalNotes` del notepad demo al texto base mediante la ruta autorizada y verificar identidad/ID. Nunca hacer un reset masivo de tablas o tocar otros usuarios.
6. Mantener el evento futuro y los fixtures durante toda la revisión. Retirar o rotar el acceso después de cerrarla.

## Checklist del operador

- [ ] Cuenta demo creada y correo verificado.
- [ ] Acceso del reviewer probado en un navegador limpio, sin segundo factor.
- [ ] Fixtures completos y etiquetados como ficticios.
- [ ] Ocho casos ejecutados en ChatGPT con el MCP de producción candidato.
- [ ] Credenciales guardadas solo en el campo privado del portal.
- [ ] Responsable, fecha del evento y plan de restauración registrados fuera del paquete.
