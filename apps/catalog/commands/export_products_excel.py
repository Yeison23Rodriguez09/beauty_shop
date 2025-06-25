# beauty_shop\apps\catalog\commands\export_products_excel.py
import pandas as pd
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from apps.catalog.models import Product

class Command(BaseCommand):
    help = "Exporta el catálogo a media/exports/products.xlsx"

    def handle(self, *args, **options):
        qs = Product.objects.select_related('category', 'brand')
        data = [
            {
                "ID":        p.id,
                "Nombre":    p.name,
                "Categoría": p.category.name if p.category else "",
                "Marca":     p.brand.name if p.brand else "",
                "Precio":    float(p.price),
                "Activo":    p.is_active,
                "Creado":    p.created_at.strftime('%Y-%m-%d'),
            }
            for p in qs
        ]
        df = pd.DataFrame(data)
        export_dir  = settings.PRODUCT_EXPORT_PATH
        export_dir.mkdir(parents=True, exist_ok=True)
        file_path = export_dir / 'products.xlsx'
        df.to_excel(file_path, index=False)
        self.stdout.write(self.style.SUCCESS(f'Excel generado en {file_path}'))
