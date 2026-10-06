# Icono del piloto privado: reproducción para soporte

Este documento es un borrador técnico; no se ha enviado a terceros.

El piloto personal privado Braking Lab - Race Engineer · Staging conserva su
identidad y conexión. Versión actual 1.1.7, release
`pluginrel_6ac51d0061888191a05effe76c1f4208`.

Resultado esperado: isotipo canónico del pedal naranja con contorno crema en la
ficha y el selector de complementos. Resultado observado: SVG amarillo genérico.
La cabecera del workspace real sí muestra el isotipo nuevo.

El paquete contiene un PNG RGBA de 512 × 512 px, 9.813 bytes, hash
`b744b0d7bc6bf99501489cde9e5000eb9d1137ccbde42f9289c314d2d10ea5a6`.
Los manifests raíz/compatibilidad apuntan al mismo archivo contenido:
`./assets/braking-lab-isotype-v5.png`. Se conserva el archivo anterior como
activo sin uso; la actualización por overlay no permite borrarlo. Se conservan diez skills, tres prompts,
propiedad personal, audiencia privada y dependencia de staging.

La subida manual de 1.1.4 y la actualización 1.1.5 se verificaron mediante lectura
de fuente y catálogo oficial. La versión local/remota coincide; `logoUrl`,
`logoUrlDark` y `composerIconUrl` están registrados. Los paths locales nulos en
el resumen remoto no demuestran ausencia de los assets.

La ficha real sigue usando el genérico tras renovar herramientas y volver a
abrir el piloto. No hay control visible de carga de icono en los ajustes de la
conexión. El piloto personal no aparece en los catálogos de las organizaciones
existentes; su enlace de gestión devuelve plugin no encontrado en esa
organización. No se ha cambiado la propiedad ni creado un reemplazo.

No se incluyen credenciales, URLs de assets firmadas, capturas con datos de
pilotos ni contenido privado. Las capturas de prueba permanecen localmente.
Una corrección debe conservar el plugin y su conexión; no ensayar nuevas
versiones sin una hipótesis documentada ni declarar arreglado un renderizado
que no se haya observado.

Las lecturas HTTP sin credenciales a las URLs registradas devolvieron 403.
Esto no demuestra por sí solo que fallen en el navegador autenticado: no se
copiaron cookies ni credenciales entre clientes para repetirlas. No se afirma
que los bytes remotos se hayan verificado contra el hash del paquete.

## Intentos acotados del 6 de octubre

Se aplicó una actualización guardada con Plugin Creator desde la release exacta
1.1.5 a 1.1.6. El cambio se limitó a sincronizar la versión y las cuatro rutas
logo/logoDark/composerIcon/composerIconDark hacia un nombre nuevo, manteniendo
los mismos bytes canónicos. La hipótesis era evitar la referencia previa de
activos y probar el actualizador oficial. La lectura de archivos confirmó el
PNG de 9.813 bytes; sin embargo, plugin/list y plugin/read no devolvían URLs de
branding en esa release.

Se corrigió esa regresión importando el paquete completo 1.1.7 mediante «Subir
nueva versión» en la misma ficha de ChatGPT. La importación devolvió «Nueva
versión subida». Las URLs de branding volvieron a estar registradas; versiones
local/remota coinciden. Read-back confirmó los diez SKILL.md byte a byte,
la dependencia .app.json, la propiedad USER/PRIVATE, los tres prompts y la
presentación conservados. No hubo despliegue de MCP, reconexión OAuth, cambio
de audiencia ni reemplazo del plugin.

Tras una recarga completa de la ficha 1.1.7, las cuatro imágenes accesibles con
el nombre del piloto siguen siendo el SVG genérico embebido, con anchura natural 24. Esto prueba el fallback visible, no su causa. El inventario de pageAssets
permitió recuperar cuatro PNG de otros elementos de la página; ninguno coincide
con el hash canónico de Ray. No se afirma que se haya verificado la descarga del
logo de Ray mediante el navegador autenticado. No usar las URLs firmadas ni
copiar cookies para repetir solicitudes fuera del navegador.

Revisión posterior: identidad, prompts, skills y binding preservados; PNG válido,
rutas contenidas y manifests sincronizados. Resultado: configuración de la
release corregida, renderizado de la ficha **sin resolver**. Se preparó una
captura local de la cabecera sin correo ni telemetría para una incidencia a
soporte. El envío requiere autorización explícita y aún no se ha realizado.

Formato de branding contrastado con la documentación oficial:
[Package your plugin](https://developers.openai.com/plugins/build/plugins) y
[Upload and submit](https://developers.openai.com/plugins/deploy/submission).
No se ensayan más versiones sin un diagnóstico nuevo.
