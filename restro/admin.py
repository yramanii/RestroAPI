from django.contrib import admin
from .models import Customer, Punjabi, Gujarati, South_Indian, Italian

# Register your models here.
admin.site.register(Punjabi)
admin.site.register(Gujarati)
admin.site.register(South_Indian)
admin.site.register(Italian)
# admin.site.register(Menu)
admin.site.register(Customer)
# admin.site.register(Billing)