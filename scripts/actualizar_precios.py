"""Aplica a productos.csv los precios de la consulta en el navegador.

Uso: python3 scripts/actualizar_precios.py precios.csv
Solo cambia productos vendidos por envase. Los de peso variable (p. ej. pollo)
se revisan a mano con el precio por kg de la columna precio_unidad.
"""
import csv
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PESO_VARIABLE = {"pollo_muslo", "boniato"}

ruta_cat = RAIZ / "productos" / "productos.csv"
with open(ruta_cat, newline="") as f:
    lector = csv.DictReader(f)
    campos, productos = lector.fieldnames, list(lector)
with open(sys.argv[1], newline="") as f:
    precios = {r["id"]: r for r in csv.DictReader(f)}

for p in productos:
    r = precios.get(p["id"])
    if not r or not r["precio"]:
        print(f"SIN PRECIO  {p['id']}: {r['nombre'] if r else 'no consultado'}")
        continue
    if r["disponible"].lower() == "false":
        print(f"NO DISPONIBLE  {p['id']}")
    if p["id"] in PESO_VARIABLE:
        print(f"REVISAR A MANO  {p['id']}: {r['precio']} ({r['precio_unidad']})")
        continue
    if p["precio_envase_aud"] != r["precio"]:
        print(f"{p['id']}: {p['precio_envase_aud']} -> {r['precio']}")
    p["precio_envase_aud"] = r["precio"]
    p["fuente_precio"] = f"woolworths.com.au {r['fecha']}"

with open(ruta_cat, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=campos)
    w.writeheader()
    w.writerows(productos)
