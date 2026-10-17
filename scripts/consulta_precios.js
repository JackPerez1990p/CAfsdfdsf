// Consulta los precios actuales en woolworths.com.au.
// Uso: abre https://www.woolworths.com.au con tu sesión iniciada, pulsa F12,
// pestaña Console, pega este script y pulsa Enter. El resultado se copia al
// portapapeles: pégalo en precios.csv del repo (o en el chat).
// Regenerar tras cambiar el catálogo: python3 scripts/generar_consulta_precios.py
(async () => {
  const productos = [
  ["avena", "79402"],
  ["leche_sl", "553273"],
  ["platano", "133211"],
  ["huevo", "313900"],
  ["pollo_muslo", "121947"],
  ["arroz", "72779"],
  ["verduras", "93915"],
  ["carne_picada", "577862"],
  ["alubias", "907048"],
  ["tomate", "311488"],
  ["boniato", "147071"],
  ["atun", "178886"],
  ["wrap", "634919"],
  ["yogur_sl", "85067"],
  ["aceite", "903638"]
  ];
  const lineas = ["id,stockcode,nombre,precio,precio_unidad,disponible,fecha"];
  const hoy = new Date().toISOString().slice(0, 10);
  for (const [id, sc] of productos) {
    try {
      const r = await fetch(`/apis/ui/product/detail/${sc}`, { credentials: "include" });
      if (!r.ok) throw new Error("HTTP " + r.status);
      const d = await r.json();
      const p = d.Product || d;
      const nombre = String(p.DisplayName || p.Name || "").replaceAll('"', "'");
      lineas.push([id, sc, `"${nombre}"`, p.Price ?? "", `"${p.CupString || ""}"`, p.IsAvailable ?? "", hoy].join(","));
    } catch (e) {
      lineas.push([id, sc, `"ERROR ${e.message}"`, "", "", "", hoy].join(","));
    }
    await new Promise(res => setTimeout(res, 500));
  }
  const csv = lineas.join("\n");
  console.log(csv);
  try { copy(csv); console.log("Copiado al portapapeles."); } catch (e) {}
})();
