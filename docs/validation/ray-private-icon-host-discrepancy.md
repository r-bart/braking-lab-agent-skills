# Icono del piloto privado: reproducción para soporte

Este documento es un borrador técnico; no se ha enviado a terceros.

El piloto personal privado Braking Lab - Race Engineer · Staging conserva su
identidad y conexión. Versión 1.1.5, release
`pluginrel_6ac4ec23cff4819186849fe7f3d99bff`.

Resultado esperado: isotipo canónico del pedal naranja con contorno crema en la
ficha y el selector de complementos. Resultado observado: SVG amarillo genérico.
La cabecera del workspace real sí muestra el isotipo nuevo.

El paquete contiene un PNG RGBA de 512 × 512 px, 9.813 bytes, hash
`b744b0d7bc6bf99501489cde9e5000eb9d1137ccbde42f9289c314d2d10ea5a6`.
Los manifests raíz/compatibilidad apuntan al mismo archivo contenido:
`./assets/braking-lab-isotype.png`. Se conservan diez skills, tres prompts,
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
