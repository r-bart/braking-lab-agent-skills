# Guion del vídeo para revisión

**Grabación de producción en curso; vídeo final todavía no entregado ni alojado.**
La conexión de desarrollo de producción muestra la cuenta sintética Franz
Hermann, sus trazas y sus dos setups iRacing independientes. P1, P2, P3 y P4
produjeron respuestas verificadas de lectura. P5 mostró el borrador exacto,
recibió «apruebo» escrito por el piloto en ChatGPT y verificó el guardado mediante
readback, con la línea una sola vez y las curvas/pins/vídeos preservados.

El primer ensayo N1 sin invocación explícita de Ray ofreció comprobar el
descifrado de un `.sto`: no pasa. Al consultar expresamente las capacidades
MCP, ChatGPT corrigió la respuesta. N2 y N3 rechazaron respectivamente control
físico y compra/cargo. No presentar esos ensayos como cualificación del paquete
público guardado ni como prueba completa de ausencia de llamadas a herramientas.
La skill de setup-library ya declara que `.sto` nativo no está soportado.

La primera toma de OAuth capturó una ventana equivocada y fue descartada; no
es evidencia válida. Las tomas posteriores se verificaron por fotogramas del
producto real. El vídeo final debe excluir contraseñas, UUID internos,
marcadores e historial ajeno, y conservar los límites observados.

## Recorrido propuesto

1. Mostrar el nombre del plugin y explicar la procedencia: cuenta Franz de prueba, fixtures sintéticas y copias privadas autorizadas de notas/vueltas reales. Conectar mediante OAuth mostrando los permisos de datos e identidad, sin grabar contraseñas, tokens, IDs privados o el campo de credenciales del portal.
2. **P1:** abrir Braking Lab - Race Engineer. Mostrar la cuenta conectada y los datos que realmente renderiza el host. Una llamada MCP correcta no es evidencia de UI visible. Si una fuente falla, debe mostrarse el aviso de disponibilidad parcial.
3. **P2:** revisar la sesión reciente con hasta tres prioridades y sin guardar informe. Mostrar límites de señales y distinguir hechos de hipótesis.
4. **P3:** comparar dos vueltas compatibles, indicando la referencia y la mayor diferencia medida.
5. **P4:** comparar `Reviewer Demo Verified Garage A/B`, fijando sus dos versiones guardadas. Mostrar el único cambio observado y explicar que son imports independientes iRacing. No asociarlos a las vueltas LMU ni atribuir mejoras al setup.
6. **P5:** pedir la única edición de notas del manifiesto. Mostrar el borrador exacto, la aprobación del piloto, el texto guardado y una lectura posterior; conservar curvas y pins.
7. Ejecutar **N1–N3**: edición de `.sto` cifrado, control físico del simulador/pedal y compra en el chat. Mostrar que cada petición se explica como no soportada sin invocar herramientas.
8. Como recorridos adicionales de Extensions, mostrar las preferencias nativas de idioma/unidades y el file opener con un `.svm` o export de garaje propio de prueba. La previsualización del archivo es lectura; importar abre el flujo de la SPA. Las preferencias se guardan inmediatamente, sin borrador. No presentar aprobación escrita por el agente como consentimiento.
9. Desconectar/revocar el acceso y mostrar que una llamada posterior requiere autenticación. Restaurar solo las notas demo y las preferencias usadas para la grabación.

## Recorrido adicional con circuitos reales

- Abrir Silverstone en Notas de Pista: mapa canónico, Stowe y cuatro pins.
  «Repasar mis notas con Ray» entrega la referencia guardada al chat. La respuesta
  observada identifica a Franz, distingue la copia autorizada de su conducción,
  propone una comprobación y no escribe nada.
- Abrir la sesión de Silverstone Arena Grand Prix del 21 de septiembre con el
  BMW M4 G82 GT4 EVO. Seleccionar la vuelta 4 y comparar con la 6; mostrar la
  traza completa y zona 12. No confundir números de frenadas con nombres de curvas.
- Son 7.910 y 7.894 muestras reales. Ray reconstruye tiempos 2:11.840 y 2:11.559
  desde las trazas; el delta de la rejilla es una estimación distinta. No atribuir
  la diferencia a un setup ni prometer causalidad con solo dos vueltas.
- Road America añade profundidad de notas (11 curvas escritas). Evitar la curva
  11: conserva un valor original sospechoso de velocidad mínima `1150`, pendiente
  de revisión; no inventar su reemplazo ni tratarlo como recomendación.

Los originales del propietario se conservan. Las copias de reviewer son privadas;
no contienen vídeos, identidad del autor ni enlaces compartidos. Este recorrido
no sustituye los ocho casos del manifiesto sobre la versión pública exacta.

## Entrega

- Alojamiento HTTPS que el reviewer pueda abrir sin iniciar sesión en servicios adicionales.
- El vídeo debe reflejar el producto y servidor que se envían a revisión; no usar renders, mocks o grabaciones de una versión distinta.
- Comprobar el enlace desde una sesión no autenticada y añadirlo a `extensions.com.openai.review.demo_recording_url`.
- Volver a ejecutar `python scripts/verify_submission.py --ready`, reconstruir los ZIP y actualizar checksums.
- Registrar la fecha, versión MCP, versión del paquete y resultados reales en `docs/validation/`, sin secretos.
