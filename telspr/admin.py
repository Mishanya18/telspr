from django.contrib import admin
from telspr.models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('surname','first_name','ats_ogv')
    list_display_links = ('surname',)
    search_fields = ('surname','first_name')

admin.site.register(Person, PersonAdmin)
