from django.contrib import admin
from .models import Customer, Punjabi, Gujarati, South_Indian, Italian

# Register your models here.
admin.site.site_header = 'Restro Administration'

class punjabiAdmin(admin.ModelAdmin):
    list_display = ['Sabji_Name', 'Price']
    search_fields = ['Sabji_Name']

class gujaratiAdmin(admin.ModelAdmin):
    list_display = ['Sabji_Name', 'Price']
    search_fields = ['Sabji_Name']

class SouthIndianAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Price']
    search_fields = ['Name']

class ItalianAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Price']
    search_fields = ['Name']

class customerAdmin(admin.ModelAdmin):
    list_display = ['Name']
    search_fields = ['Name']

admin.site.register(Punjabi, punjabiAdmin)
admin.site.register(Gujarati, gujaratiAdmin)
admin.site.register(South_Indian, SouthIndianAdmin)
admin.site.register(Italian, ItalianAdmin)
# admin.site.register(Menu)
admin.site.register(Customer, customerAdmin)
# admin.site.register(Billing)