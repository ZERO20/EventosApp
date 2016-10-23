from django.contrib import admin
from reversion.admin import VersionAdmin
from apps.Administracion.models import CatConceptoEstatus, CatCategoriasEspacios,CatEstatus

@admin.register(CatConceptoEstatus)
class CatConceptoEstatusAdmin(VersionAdmin):
    pass

@admin.register(CatEstatus)
class CatEstatusAdmin(VersionAdmin):
    pass

@admin.register(CatCategoriasEspacios)
class CatCategoriasEspaciosAdmin(VersionAdmin):
    pass
