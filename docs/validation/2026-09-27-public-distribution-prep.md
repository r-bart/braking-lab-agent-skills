# Preparación del lanzamiento conjunto — 27 de septiembre de 2026

El alcance acordado es publicar Claude, ChatGPT y la instalación por CLI para otras personas en el mismo lanzamiento. La release `v0.1.1` y el repositorio siguen privados. El CI `Verify package` del commit `fdcdbdd` pasó. Ninguna ficha pública de ChatGPT o Claude se da por publicada.

## CLI

Se ejecutó `DISABLE_TELEMETRY=1 npx --yes skills add <ruta-local-del-repo> --list`: detectó las nueve skills. Después, en un directorio temporal vacío, `npx --yes skills add <ruta-local-del-repo> --skill '*' --agent codex --yes` terminó con código 0 y creó nueve `SKILL.md` en `.agents/skills/`. El directorio temporal se eliminó al terminar. La prueba no cubre la descarga desde GitHub público ni la conexión MCP/OAuth; ambas requieren otra comprobación antes del lanzamiento.

## ChatGPT público

El portal de OpenAI Platform mostró «Complete identity verification» al intentar crear un borrador **With MCP**: no permite crearlo ni subir el paquete antes de verificar la identidad publicadora. El propietario eligió publicarlo como desarrollador individual y el trámite externo de Persona quedó abierto para que lo complete directamente. El repositorio mantiene pendientes el soporte de OAuth para restricciones de dominio de workspace, la prueba de dominio que genere el portal, una cuenta demo de producción, una grabación y los materiales de revisión. La aprobación y publicación del directorio dependen de OpenAI después del envío.

## Claude

El marketplace Git y el ZIP `v0.1.1` existen y se instalaron durante el piloto. La primera respuesta con datos en Claude sigue sin verificar por el límite de uso de la cuenta. Para distribuir a cualquier persona hay que abrir el repositorio, probar la instalación sin acceso previo y completar OAuth y una consulta real en cada superficie anunciada.
