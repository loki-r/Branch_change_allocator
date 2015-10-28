from django.contrib import admin
from branch.models import Info
# Register your models here.

from django.http import HttpResponseRedirect, HttpResponse

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=input_options.csv'
    writer = csv.writer(response)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    for obj in queryset:
        writer.writerow([
            smart_str(obj.roll_no),
            smart_str(obj.name),
            smart_str(obj.present_branch),
            smart_str(obj.cpi),
            smart_str(obj.category),
            smart_str(obj.pref_1),
            smart_str(obj.pref_2),
        ])
    return response
export_csv.short_description = u"Export CSV"

class MyModelAdmin(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(Info,MyModelAdmin)