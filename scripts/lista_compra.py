"""Genera macros diarias por persona y la lista de la compra semanal.

Uso: python3 scripts/lista_compra.py planes/semana-1.json
"""
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def cargar_productos():
    with open(RAIZ / "productos" / "productos.csv", newline="") as f:
        return {p["id"]: p for p in csv.DictReader(f)}


def factor(p, cantidad):
    # Valores nutricionales por unidad para "ud", por 100 g/ml en el resto.
    return cantidad if p["unidad"] == "ud" else cantidad / 100


def main(ruta_plan):
    productos = cargar_productos()
    plan = json.loads(Path(ruta_plan).read_text())
    dias = plan["dias"]
    total = defaultdict(float)

    print("## Macros diarias\n")
    print("| Persona | kcal | Proteína (g) | Carbohidratos (g) | Grasa (g) |")
    print("| --- | --- | --- | --- | --- |")
    for persona, comidas in plan["personas"].items():
        m = defaultdict(float)
        for items in comidas.values():
            for pid, cant in items.items():
                p = productos[pid]
                f = factor(p, cant)
                for k in ("kcal", "proteina", "carbohidratos", "grasa"):
                    m[k] += float(p[k]) * f
                total[pid] += cant * dias
        print(f"| {persona} | {m['kcal']:.0f} | {m['proteina']:.0f} | "
              f"{m['carbohidratos']:.0f} | {m['grasa']:.0f} |")
    for pid, cant in plan.get("cocina", {}).items():
        total[pid] += cant

    print("\n## Lista de la compra\n")
    print("| Producto | Necesario | Envases | Precio (AUD) | Subtotal (AUD) |")
    print("| --- | --- | --- | --- | --- |")
    coste = 0.0
    for pid, cant in total.items():
        p = productos[pid]
        envases = math.ceil(cant / float(p["cantidad_util_envase"]) - 1e-9)
        sub = envases * float(p["precio_envase_aud"])
        coste += sub
        print(f"| [{p['nombre']}]({p['url']}) | {cant:.0f} {p['unidad']} | "
              f"{envases} | {float(p['precio_envase_aud']):.2f} | {sub:.2f} |")
    print(f"\n**Total estimado:** {coste:.2f} AUD")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else RAIZ / "planes" / "semana-1.json")
