from django.contrib import admin


# Register your models here.
from .models import infotech
@admin.register(infotech)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["firstname","secondname", "mobile1", "mobile2", "village","district","total_days","booking_days",]