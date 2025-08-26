from django.contrib import admin

# Register your models here.
from .models import ESPECIALIDADE, MEDICO
admin.site.register(ESPECIALIDADE)
admin.site.register(MEDICO)