"""Regenera scripts/consulta_precios.js con los stockcodes de productos.csv."""
import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
plantilla = (RAIZ / "scripts" / "consulta_precios.js").read_text()
inicio = plantilla.index("const productos = [") + len("const productos = [")
fin = plantilla.index("];", inicio)
with open(RAIZ / "productos" / "productos.csv", newline="") as f:
    items = ",\n  ".join(f'["{r["id"]}", "{r["stockcode"]}"]' for r in csv.DictReader(f))
(RAIZ / "scripts" / "consulta_precios.js").write_text(
    plantilla[:inicio] + "\n  " + items + "\n  " + plantilla[fin:])
