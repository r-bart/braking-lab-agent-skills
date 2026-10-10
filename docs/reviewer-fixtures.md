# Cuenta del reviewer con contenido ficticio

**Decisión vigente — 10 de octubre de 2026:** el propietario ha elegido un
correo ficticio sin buzón para Franz Hermann. Se conserva la cuenta sintética
existente de staging y su acceso por contraseña, sin MFA ni códigos por correo.
No se exige un buzón de recuperación para este recorrido. Braking Lab se ocupa
de los desbloqueos y de renovar el acceso durante la revisión; el operador debe
comprobar el login justo antes del envío. Las credenciales se proporcionan solo
en los campos protegidos del portal. La cuenta equivalente en producción aún
requiere autorización y aprovisionamiento; no reutilizar sus tokens de staging.
Esta decisión sustituye las referencias históricas a un buzón controlado abajo.

**Cuenta dedicada creada en staging el 6 de octubre de 2026; contenido parcial.** Usuario independiente sin administrador, membresía Ultra sintética hasta el 5 de diciembre de 2026, una carrera, un notepad con nota de curva y pin, una sesión sintética LMU con dos vueltas limpias y trazas, y dos setups iRacing comparables de prueba. El login real con contraseña y la lectura propia mediante RLS pasaron; la repetición de la herramienta conserva exactamente una carrera y un notepad. No hay cuenta reviewer en producción ni aceptación de estos casos en ChatGPT. El correo temporal `staging.test` sirve únicamente para pruebas de staging; falta un buzón controlado por Braking Lab para recuperación y revisión final.

## Identidad y acceso

Crear una cuenta exclusiva para revisión, con correo bajo control de Braking Lab y verificado una vez por el operador. El reviewer debe poder entrar sin MFA, códigos por SMS ni confirmaciones de correo adicionales en cada acceso. La cuenta no contendrá información de pilotos reales, tarjetas ni acceso de administrador. Proporcionar el acceso existente necesario para los casos de revisión, con expiración posterior al período de revisión; no hacer que el reviewer compre un plan.

Guardar las credenciales en el campo seguro de testing del portal de OpenAI. Nunca en `plugin.json`, un ZIP, Git, una URL de vídeo o este documento. Mantener un responsable para desbloqueos y rotación posterior. El manifiesto no incorpora `testing_instructions` ni credenciales privadas.

## Contenido a preparar

| Elemento | Contenido ficticio | Aceptación |
| --- | --- | --- |
| Perfil | Nombre de cuenta `Franz Hermann`; username `Franz_Hermann` | `ray_whoami` devuelve esta cuenta; identidad distinta de la cuenta real. |
| Telemetría reciente | Una sesión sintética identificada como demo, circuito/coche/simulador compatibles; dos vueltas limpias con trazas de freno, velocidad y distancia coherentes | Última sesión seleccionable; `getSessionDetail`, `getBrakingZones` y `compareLaps` devuelven señales reales del fixture. No simular una medición ausente. |
| Señales incompletas | Otra sesión sintética, claramente marcada, sin una señal de freno | Una consulta a esa sesión explica la ausencia; no inventa un punto de frenada. Este es un recorrido adicional, no uno de los tres negativos de no invocación. |
| Calendario | Evento `Reviewer Demo Race` con fecha concreta siete días después del envío; contexto compatible con la sesión | `getUpcomingRaces({})` lo devuelve. Vincular práctica y preparar notas; refrescar su fecha si caduca durante revisión. |
| Setup propio LMU (pendiente) | `Reviewer Demo Setup`, dos versiones válidas y legibles, con procedencia sintética explícita | La biblioteca y las versiones son consultables. No atribuir una versión a una tanda si no existe evidencia verificable del vínculo. No incorporar corpus privados. |
| Notas de pista | Un único notepad `Reviewer Demo Notes`, con generalNotes base, una nota de curva, un pin y un vídeo público seguro opcional | P5 añade una sola línea y conserva los otros campos. El reviewer tiene permisos normales de escritura sobre este fixture. |
| Preferencias | Idioma inglés, unidades métricas, densidad comfortable | Cambiar ES/EN y unidades refleja preferencias; restaurar antes del vídeo. |

Generar/importar sesiones mediante las rutas normales de Capture y de importación compatibles con el simulador. Usar setups de prueba propios o fixtures que puedan compartirse legalmente. Solo copiar telemetría del propietario con su autorización expresa, bajo IDs y objetos propios del reviewer y con procedencia real documentada. No insertar a mano filas que omitan relaciones, objetos y permisos requeridos.

## Ejecución y mantenimiento

1. Seleccionar siempre la conexión demo y confirmar identidad antes de ejecutar los ocho prompts de `plugin.json`.
2. Guardar un registro redactado de resultado esperado/real; no guardar correo, tokens o credenciales en el reporte.
3. P1–P4 son lecturas. P5 edita únicamente el notepad demo; no borra carreras ni llama a imports/associations consent-sensitive.
4. Tras P5, leer de nuevo el notepad. Verificar una sola línea `Reviewer practice: check brake release consistency`, y que notas de curva, pins y vídeos no cambien.
5. Antes de cada nueva grabación, restaurar únicamente `generalNotes` del notepad demo al texto base mediante la ruta autorizada y verificar identidad/ID. Nunca hacer un reset masivo de tablas o tocar otros usuarios.
6. Mantener el evento futuro y los fixtures durante toda la revisión. Retirar o rotar el acceso después de cerrarla.

## Checklist del operador

- [x] Cuenta staging dedicada creada y correo confirmado por el operador de pruebas.
- [ ] Cuenta final con buzón controlado, recuperación comprobada y entorno candidato autorizado.
- [ ] Acceso del reviewer probado en un navegador limpio, sin segundo factor.
- [ ] Fixtures completos y etiquetados como ficticios.
- [ ] Ocho casos ejecutados en ChatGPT con el MCP de producción candidato.
- [ ] Credenciales guardadas solo en el campo privado del portal.
- [ ] Responsable, fecha del evento y plan de restauración registrados fuera del paquete.

## Herramienta y evidencia del 6 de octubre

En el monorepo, desde `apps/mcp-server`:

```sh
pnpm exec tsx scripts/reviewer-staging.ts plan
pnpm exec tsx scripts/reviewer-staging.ts apply
pnpm exec tsx scripts/reviewer-staging.ts matrix
```

El operador prepara `~/.config/braking-lab-reviewer/staging-config.json` con permisos 0600: `expectedProjectRef`, `supabaseUrl`, `serviceRoleKey`, `email` y `expiresAt`. La referencia obligatoria es `vybwhglkqcnqjktnrolo`; URL HTTPS exacta, sin ruta, credenciales ni hosts alternativos. La expiración debe estar entre ahora y 90 días. El plan persiste ID y contraseña aleatorios en `staging-state.json`, también 0600, antes de contactar al servidor. Nunca copiar estos archivos al paquete o al repositorio. La CLI no imprime credenciales ni excepciones del proveedor.

`apply` recupera el mismo usuario ante incertidumbre, rechaza identidad o membresía inesperada y cualquier administrador, y no cambia la contraseña, los permisos ni las notas de una cuenta existente. Crea membresía de fixture en staging sin llamar a Stripe. Las notas y carrera se crean con los escritores normales de dominio. No usar los seeds compartidos `e2e-re-*`: la limpieza E2E puede borrarlos y pertenecen a otras identidades. Ejecutar un único operador a la vez.

`matrix` ejecuta lecturas RPC reales para Basic, Plus, Ultra y reviewer; no usa fixtures del navegador. Resultado observado: Basic sin raceStrategy/setupCoaching/aiSetupGenerator; Plus con coaching/generador, sin estrategia; Ultra y reviewer con los tres. `founding_active=false`. La matriz imprime expresamente que **no verifica transporte MCP ni ChatGPT**. Team seat, scopes read-only/write, cuotas agotadas, revocación OAuth y consentimiento requieren la batería de transporte y el recorrido del host por separado.

Telemetría completada mediante el flujo normal de Capture: device-code create/authorize/poll, sync-session, presign R2, PUT firmado y sync-lap. Lecturas reales de `getLapTrace` devuelven 200 puntos por vuelta; `compareTraces` devuelve 200 puntos y delta sintético de 700 ms. Pendiente: caso de señal ausente, importar dos versiones propias LMU por la ruta normal, la aceptación del recorrido en ChatGPT. La carrera/notas se han ajustado al contexto descriptivo LMU guardado y existe preparación demo. La carrera y notas usan el coche/circuito de la sesión sintética; la equivalencia de simulador usa el normalizador canónico. No se afirma identidad exacta de circuito/coche: los IDs canónicos faltan en este fixture. No se vinculan los setups iRacing a la sesión LMU. No saltarse el fence de uploads/reset ni copiar el corpus privado para completar fixtures. Renovar la fecha de carrera explícitamente si la revisión se retrasa; rerun no mueve fechas ni renueva acceso.

Evidencia local: 8 tests de guardas/reanudación, typecheck y lint de los archivos. Evidencia remota: dos aplicaciones sin duplicados, login de contraseña real, RLS de lectura de sus propios dos documentos y matriz RPC. Pendientes: transporte MCP con esta identidad, UI real ChatGPT, vídeo, cuenta final y portal.

### Límite del setup LMU sintético

La carga normal `POST https://app-staging.brakinglab.com/api/setups/upload` se comprobó contra el despliegue SPA `430c58219af4a3b3473de21a192c376619f36b5c`. Rechazó el fixture mínimo del parser con `SVM_VEHICLE_DIRECTORY_INVALID`. Además de estructura válida, el endpoint exige identidad y esquema exactos de un modelo admitido; un fichero con parámetros inventados no basta. No se ha añadido un modelo falso al corpus ni se han copiado valores privados para superar el control. Hace falta un export LMU propio y legalmente compartible de un modelo admitido, dos versiones de prueba y el recorrido normal de importación. La segunda versión dentro de la misma línea debe usar el flujo admitido y su confirmación si procede; no existe atribución automática a las vueltas demo.

Las cuotas se consultaron sin cambiar planes reales: Basic devuelve 0 sesiones/0 vueltas disponibles; Plus/Ultra están activos, reviewer mantiene Ultra con cancelación programada y tiene 1 sesión/2 vueltas. Esto no cualifica transiciones futuras de cancelación, downgrade, `past_due` ni team seat. El token Capture e IDs de objetos están en un ledger privado 0600, fuera del paquete.

### Setups iRacing comparables completados

Se importaron `Reviewer Demo Verified Garage A` y `B` mediante la API normal de SPA, con operationId estable y el flujo completo de parse, hash, fingerprint y reserva/finalización de upload. Fuente: fixture committed y descrito como privacy-safe `packages/setup-fingerprint/fixtures/iracing/bmwm4evogt4-synthetic-toe-fractions/garage.htm`; B cambia un único valor de camber. Se retiró la prosa de notas y se identificó el contenido como prueba. No se usó corpus privado.

Las lecturas remotas reales devolvieron 61 parámetros por versión, identidad conocida, adaptador revisado elegible y comparación disponible con un cambio. Son dos setups propios independientes, cada uno con su versión inicial; no son una relación padre/hijo ni están atribuidos a las vueltas LMU. Dos imports mínimos anteriores (`Reviewer Demo Garage A/B`, cuatro parámetros) permanecen como casos de identidad desconocida y comparación no disponible, correctamente explicada.

**P4 actualizado el 6 de octubre:** manifiesto, draft y guion comparan los dos setups iRacing independientes, con versión explícita y sin atribuirlos a las vueltas LMU. Las lecturas remotas ya prueban el par; P4 en ChatGPT sigue pendiente hasta ejecutarlo en el host. El import LMU continúa como cobertura adicional pendiente; no se registra como caso aprobado.

### Carrera y preparación

Se verificaron las filas de la sesión por ID y propietario, y las únicas carrera/notas demo por propietario e ID. Los escritores normales actualizaron el contexto descriptivo a BMW_M4_LMGT3 y Reviewer Demo Circuit; el simulador coincide mediante el normalizador canónico (`lmu`/`le_mans_ultimate`). Falta identidad numérica de coche/circuito, por lo que no se presenta esa coincidencia de campos como atribución exacta. Se creó una preparación con plantilla admitida y se comprobó la reanudación sin duplicados. No se ejecutó asociación de setup, uso o sesión.

Validación del paquete tras adaptar P4: 31 tests; `verify_package`, `verify_contract` y `verify_submission` pasan con dependencias de `requirements-dev.txt`. `verify_submission --ready` falla exclusivamente por la URL real del vídeo pendiente. No implica aceptación del portal ni prueba del P4 en ChatGPT.

## Identidad Franz Hermann y telemetría autorizada

El propietario pidió renombrar el reviewer como Franz Hermann el 6 de octubre. El username es `Franz_Hermann` porque la SPA no admite espacios; el nombre completo de Auth es `Franz Hermann`. Login y lecturas propias por RLS comprobados después del cambio.

El propietario autorizó usar su telemetría de staging. El perfil coincidente en el staging canónico es `robertodzbt_staging`, actualmente sin sesiones ni vueltas almacenadas. No se copiaron datos reales ni se consultó producción; se conservan las dos vueltas sintéticas hasta identificar otra cuenta de staging o sincronizar la telemetría. Las credenciales permanecen exclusivamente en almacenamiento privado.
