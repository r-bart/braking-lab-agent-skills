# Validación del empaquetado — 2026-09-26

## Resultado comprobado

- `scripts/verify_package.py`: pasaron los esquemas Agent Plugins 1.0.0, las nueve skills con `agentskills validate`, la identidad de los manifiestos y la URL única de producción.
- `claude plugin validate` con `--strict`: pasaron el marketplace y el plugin en una carpeta temporal sin marketplace.
- El endpoint público `https://mcp.brakinglab.com/mcp` devolvió `401` sin autenticación. Las páginas públicas de producto, privacidad y términos devolvieron `200`.
- ChatGPT importó el primer archivo de prueba y mostró nueve skills. Este archivo incluía tanto la app registrada como el MCP portable y la ficha mostró dos entradas de conexión; por eso se separaron los archivos.
- ChatGPT importó una variante de prueba con **solo la app registrada** y mostró **Apps 1, Skills 9**, sin una entrada MCP duplicada. El manifiesto de prueba tenía un nombre interno distinto para evitar la colisión con el primer archivo ya importado. El archivo distribuible de ChatGPT usa la misma estructura y el nombre interno definitivo `braking-lab-race-engineer`.
- ChatGPT importó también el archivo definitivo `braking-lab-chatgpt-0.1.0.zip` en la cuenta Personal. La [ficha privada](https://chatgpt.com/plugins/Plugin_3ea10eecd6008191a6885f644dbdc9a2) mostró **Apps 1, Skills 9**, sin una segunda entrada MCP. Al pulsar «Install plugin», ChatGPT abrió el diálogo para conectar la app; se cerró antes de conceder acceso a datos de la cuenta.

## Pendiente antes de declarar soporte completo

- OAuth y `whoami` en la cuenta piloto; no se autorizó ninguna cuenta de Braking Lab durante esta validación.
- Primer debrief y una escritura ordinaria en ChatGPT, con lectura posterior; pruebas de límites y rechazo seguro según `docs/test-plan.md`.
- Instalación y prueba funcional en Claude Code. La validación local pasó, pero la ejecución del modelo quedó detenida por el límite mensual de Claude Code de esta cuenta.
- Instalación en Claude chat y en una segunda cuenta de ChatGPT; comprobar actualización y desinstalación.
- Confirmar la elegibilidad del mapeo de la app registrada al preparar el envío público de OpenAI. El registro personal sirve para el piloto, no equivale a una ficha publicada.

El repositorio y los archivos siguen privados. Esta validación prueba el empaquetado y la importación; no prueba la calidad de las respuestas ni los flujos autenticados.
