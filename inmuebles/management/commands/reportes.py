from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
from inmuebles.models import Region, Comuna, Inmueble  # para obtener nombres de tabla

HEADER = "== Reporte de Inmuebles Disponibles =="

class Command(BaseCommand):
    help = "Genera reportes en .txt usando SQL crudo: por_comuna | por_region"

    def add_arguments(self, parser):
        parser.add_argument("tipo", choices=["por_comuna", "por_region"])
        parser.add_argument("--out", default="reporte.txt", help="Ruta de salida .txt")

    def handle(self, *args, **opts):
        tipo = opts["tipo"]
        out_path = Path(opts["out"]).resolve()
        t_inm = Inmueble._meta.db_table
        t_com = Comuna._meta.db_table
        t_reg = Region._meta.db_table

        if tipo == "por_comuna":
            sql = f"""
                SELECT c.nombre AS grupo, COALESCE(i.descripcion, '') AS descripcion
                FROM {t_inm} i
                JOIN {t_com} c ON c.id = i.comuna_id
                WHERE i.disponible = TRUE
                ORDER BY c.nombre, i.descripcion NULLS LAST;
            """
            group_label = "comuna"
        else:
            sql = f"""
                SELECT r.nombre AS grupo, COALESCE(i.descripcion, '') AS descripcion
                FROM {t_inm} i
                JOIN {t_com} c ON c.id = i.comuna_id
                JOIN {t_reg} r ON r.id = c.region_id
                WHERE i.disponible = TRUE
                ORDER BY r.nombre, i.descripcion NULLS LAST;
            """
            group_label = "region"

        with connection.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()  # [(grupo, descripcion), ...]
        groups = {}
        for grp, desc in rows:
            groups.setdefault(grp, []).append(desc or "(sin descripción)")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{HEADER}\n\n")
            for grp in sorted(groups.keys()):
                f.write(f"[{grp.upper()}]\n")
                for desc in groups[grp]:
                    f.write(f" - {desc}\n")
                f.write("\n")

        self.stdout.write(self.style.SUCCESS(f"Reporte generado: {out_path}"))
