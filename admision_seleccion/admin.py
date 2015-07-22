from django.contrib import admin
from admision_seleccion.models.Postulante import Postulante
# Register your models here.


class PostulanteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo")
    search_fields = ("nombre",  "codigo")


admin.site.register(Postulante, PostulanteAdmin)
