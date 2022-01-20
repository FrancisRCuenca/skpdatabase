from django.contrib import admin

from .models import Beneficiary

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BeneficiaryResource(resources.ModelResource):

    class Meta:
        model = Beneficiary

class BeneficiaryAdmin(ImportExportModelAdmin):
    resource_class = BeneficiaryResource

# Register your models here.
admin.site.register(Beneficiary, BeneficiaryAdmin)
