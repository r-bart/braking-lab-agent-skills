# Guion del vídeo para revisión

**Pendiente de grabar y alojar.** No hay vídeo ni URL de demostración. Usar exclusivamente la cuenta ficticia descrita en [reviewer-fixtures.md](reviewer-fixtures.md), con el MCP 0.5.1 candidato ya desplegado y probado. No grabar la cuenta del propietario.

## Recorrido propuesto

1. Mostrar el nombre del plugin y explicar que los datos son ficticios. Conectar mediante OAuth mostrando los permisos de datos e identidad, sin grabar contraseñas, tokens, IDs privados o el campo de credenciales del portal.
2. **P1:** abrir el Paddock. Mostrar la cuenta conectada y los datos que realmente renderiza el host. Una llamada MCP correcta no es evidencia de UI visible. Si una fuente falla, debe mostrarse el aviso de disponibilidad parcial.
3. **P2:** revisar la sesión reciente con hasta tres prioridades y sin guardar informe. Mostrar límites de señales y distinguir hechos de hipótesis.
4. **P3:** comparar dos vueltas compatibles, indicando la referencia y la mayor diferencia medida.
5. **P4:** preparar la siguiente carrera y consultar versiones del setup propio. No afirmar que una versión fue conducida si no existe atribución.
6. **P5:** pedir la única edición de notas del manifiesto. Mostrar el texto antes y después y una lectura posterior; conservar curvas y pins.
7. Ejecutar **N1–N3**: edición de `.sto` cifrado, control físico del simulador/pedal y compra en el chat. Mostrar que cada petición se explica como no soportada sin invocar herramientas.
8. Como recorridos adicionales de Extensions, mostrar las preferencias nativas de idioma/unidades y el file opener con un `.svm` o export de garaje propio de prueba. Abrir un archivo es lectura; importar es otra acción y respeta la elicitación directa del cliente. No presentar aprobación escrita por el agente como consentimiento.
9. Desconectar/revocar el acceso y mostrar que una llamada posterior requiere autenticación. Restaurar solo las notas demo y las preferencias usadas para la grabación.

## Entrega

- Alojamiento HTTPS que el reviewer pueda abrir sin iniciar sesión en servicios adicionales.
- El vídeo debe reflejar el producto y servidor que se envían a revisión; no usar renders, mocks o grabaciones de una versión distinta.
- Comprobar el enlace desde una sesión no autenticada y añadirlo a `extensions.com.openai.review.demo_recording_url`.
- Volver a ejecutar `python scripts/verify_submission.py --ready`, reconstruir los ZIP y actualizar checksums.
- Registrar la fecha, versión MCP, versión del paquete y resultados reales en `docs/validation/`, sin secretos.
