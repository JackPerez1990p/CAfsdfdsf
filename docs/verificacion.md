# Verificación de productos

Cada producto se comprueba en woolworths.com.au con Claude in Chrome, en el
navegador del ordenador del usuario.

## Pasos por producto

1. Buscar el producto en woolworths.com.au y abrir su página de detalle.
   La URL tiene la forma `https://www.woolworths.com.au/shop/productdetails/<stockcode>/<nombre>`.
2. Anotar en `productos/productos.csv`:
   - `stockcode` (el número de la URL) y `url`.
   - Nombre, marca y tamaño tal como aparecen en la página.
   - Precio actual y precio por unidad (p. ej. "$1.20 / 100g"). Si hay oferta,
     indicarlo en `notas` con su fecha de fin.
   - Valores de la tabla "Nutrition Information", columna por 100 g / 100 ml.
3. Poner la fecha del día en `fecha_verificacion`.
4. Si el producto no está disponible o no tiene panel nutricional, no se añade
   (o se marca en `notas` y no se usa en planes).

## Requisito técnico

Claude in Chrome tiene que ejecutarse en el ordenador del usuario. Una sesión
de Claude Code en la nube no puede conectarse con él. Para verificar productos,
abre la sesión en local: con la app de escritorio de Claude o ejecutando
`claude remote-control` en la carpeta del repositorio.
