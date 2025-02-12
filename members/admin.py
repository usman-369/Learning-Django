from django.contrib import admin
from .models import Member

# Register your models here.
# TODO: add amin files


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date", "phone",)
    prepopulated_fields = {"slug": ("firstname", "lastname")}


admin.site.register(Member, MemberAdmin)
