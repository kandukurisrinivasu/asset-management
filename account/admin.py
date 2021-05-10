from django.contrib import admin
from .models import UserProfile,Asset_details,Lab_event,Setup_details,EventMember

#from import_export.admin import ImportExportModelAdmin

#@admin.register(assetOwner)
#class assetAdmin(ImportExportModelAdmin):
#    list_display = ('sID', 'f_name', 'l_name', 'email', 'Mob', 'age', 'upload_photo','group','team_name')

# Registering the models in the django admin
admin.site.register(UserProfile)
admin.site.register(Asset_details)
class EventMemberAdmin(admin.ModelAdmin):
    model=EventMember
    display=['event','user']
admin.site.register(Lab_event)
admin.site.register(Setup_details)


admin.site.register(EventMember,EventMemberAdmin)

