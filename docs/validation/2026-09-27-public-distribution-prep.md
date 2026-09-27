# Preparación del lanzamiento conjunto — 27 de septiembre de 2026

El alcance acordado es publicar Claude, ChatGPT y la instalación por CLI para otras personas en el mismo lanzamiento. La release `v0.1.1` y el repositorio siguen privados. El CI `Verify package` del commit `fdcdbdd` pasó. Ninguna ficha pública de ChatGPT o Claude se da por publicada.

## CLI

Se ejecutó `DISABLE_TELEMETRY=1 npx --yes skills add <ruta-local-del-repo> --list`: detectó las nueve skills. Después, en un directorio temporal vacío, `npx --yes skills add <ruta-local-del-repo> --skill '*' --agent codex --yes` terminó con código 0 y creó nueve `SKILL.md` en `.agents/skills/`. El directorio temporal se eliminó al terminar. La prueba no cubre la descarga desde GitHub público ni la conexión MCP/OAuth; ambas requieren otra comprobación antes del lanzamiento.

## ChatGPT público

El propietario eligió publicarlo como desarrollador individual y completó el trámite externo de Persona. Al actualizar la página de la organización, OpenAI Platform mostraba «Identity in review». Un nuevo intento de crear el borrador **With MCP** seguía mostrando «Complete identity verification»; por tanto, la identidad está enviada pero todavía no aprobada y el portal no permite crear el borrador. El repositorio mantiene pendientes el soporte de OAuth para restricciones de dominio de workspace, la prueba de dominio que genere el portal, una cuenta demo de producción, una grabación y los materiales de revisión. La aprobación y publicación del directorio dependen de OpenAI después del envío.

## Claude

El marketplace Git y el ZIP `v0.1.1` existen y se instalaron durante el piloto. La primera respuesta con datos en Claude sigue sin verificar por el límite de uso de la cuenta. Para distribuir a cualquier persona hay que abrir el repositorio, probar la instalación sin acceso previo y completar OAuth y una consulta real en cada superficie anunciada.
