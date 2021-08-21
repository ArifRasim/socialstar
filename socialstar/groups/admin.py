from django.contrib import admin

# Register your models here.
from socialstar.groups.models import Group, GroupMember


class GroupMemberInline(admin.TabularInline):
    model=GroupMember


admin.site.register(Group)
