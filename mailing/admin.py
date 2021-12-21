from django.contrib import admin

from mailing.models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['name', 'number', 'address', 'create_at']
    readonly_fields = ['text', 'lopd_check']


admin.site.register(Contact, ContactAdmin)
