from django.contrib import admin
from charitydonation.models import Institution


# Register your models here.
@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    class Meta:
        def __str__(self):
            return self.name
