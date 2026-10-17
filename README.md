# Plan de alimentación con productos de Woolworths (Sydney)

Plan de comidas construido únicamente con productos reales que se venden en
Woolworths (woolworths.com.au), con precio e información nutricional
verificados directamente en la web de la tienda.

## Estructura

| Ruta | Contenido |
| --- | --- |
| `perfil.md` | Objetivos, restricciones, presupuesto y preferencias. Es la base del plan. |
| `productos/productos.csv` | Catálogo de productos verificados (precio, tamaño, valores por 100 g, enlace). |
| `planes/` | Planes semanales. `plantilla-semana.md` es el punto de partida. |
| `docs/verificacion.md` | Cómo se verifica cada producto en la web de Woolworths. |

## Reglas

1. Un producto solo entra en un plan si está en `productos/productos.csv` con
   `fecha_verificacion` rellenada.
2. Los valores nutricionales se copian del panel "Nutrition Information" de la
   página del producto (columna por 100 g / 100 ml), sin estimaciones.
3. Los precios cambian a menudo: un producto con verificación de más de 30 días
   se vuelve a comprobar antes de usarlo en un plan nuevo.
