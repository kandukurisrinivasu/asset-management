from django.contrib import admin
from .models import assetOwner

#from import_export.admin import ImportExportModelAdmin

#@admin.register(assetOwner)
#class assetAdmin(ImportExportModelAdmin):
#    list_display = ('sID', 'f_name', 'l_name', 'email', 'Mob', 'age', 'upload_photo','group','team_name')

admin.site.register(assetOwner)