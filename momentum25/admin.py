from django.contrib import admin
from .models import Delegate


@admin.register(Delegate)
class DelegateAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'lc', 'delegate_id', 'timestamp'
    )
    search_fields = ('full_name', 'email', 'lc', 'delegate_id')
    list_filter = ('lc', 'role', 'function', 'gender')
    readonly_fields = ('delegate_id', 'timestamp')

    fieldsets = (
        ("Personal Info", {
            'fields': ('full_name', 'email', 'phone_number', 'gender')
        }),
        ("AIESEC Info", {
            'fields': ('role', 'function', 'lc', 'lc_password')
        }),
        ("Health & Food", {
            'fields': ('allergies', 'allergy_details')
        }),
        ("Merch", {
            'fields': ('tshirt_size', 'tshirt_quantity', 'agree_policy')
        }),
        ("Documents", {
            'fields': ('id_front', 'id_back', 'indemnity_form')
        }),
        ("System", {
            'fields': ('delegate_id', 'timestamp')
        }),
    )
