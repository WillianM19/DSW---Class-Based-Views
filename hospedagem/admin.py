from django.contrib import admin
from hospedagem.models import Cliente, Quarto, Hospedagem, Consumo

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Quarto)
admin.site.register(Hospedagem)
admin.site.register(Consumo)
