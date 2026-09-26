# Instalar Race Engineer en ChatGPT

El paquete privado combina las nueve skills con el conector MCP de Braking Lab. La ficha pública aún no existe; durante el piloto se usa un archivo revisado.

1. Abre **Plugins** en ChatGPT y elige **Add → Upload plugin archive**.
2. Selecciona el archivo privado [`braking-lab-chatgpt-0.1.1.zip`](https://github.com/r-bart/braking-lab-agent-skills/releases/download/v0.1.1/braking-lab-chatgpt-0.1.1.zip). Comprueba que la ficha muestra **Braking Lab Race Engineer** y nueve skills.
3. Conecta tu cuenta de Braking Lab cuando ChatGPT lo solicite. Verifica que es la cuenta que contiene tus datos.
4. Pregunta: «Revisa mi última tanda en Spa y dame tres prioridades basadas en la telemetría».

La conexión personal MCP usada para el piloto se registró con la URL de producción `https://mcp.brakinglab.com/mcp`. Importar el archivo no autoriza la cuenta por sí solo. OAuth y varias consultas de lectura se probaron en la cuenta que registró la conexión; todavía no está comprobado que este archivo funcione en otra cuenta de ChatGPT. La ficha del directorio público se enviará por separado cuando terminen las pruebas y la revisión.

Si conectaste otra cuenta, desconecta Braking Lab desde la configuración de plugins de ChatGPT y vuelve a autorizar la correcta. Para actualizar durante el piloto, abre **More actions → Upload new version** en la ficha privada y selecciona el ZIP nuevo. Para retirarlo, desinstala el plugin en ChatGPT. La desinstalación no borra tus datos de Braking Lab.
