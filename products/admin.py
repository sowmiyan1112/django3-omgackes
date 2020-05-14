from django.contrib import admin
from .models import Cakes
from .models import Homepage


class CakesAdmin(admin.ModelAdmin):
    list_display = ('name','price')


admin.site.register(Cakes,CakesAdmin)
admin.site.register(Homepage)

