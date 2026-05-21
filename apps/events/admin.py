from django.contrib import admin
from .models import Team, Event, Shift, ShiftAssignment


class ShiftInline(admin.TabularInline):
    model = Shift
    extra = 1


class AssignmentInline(admin.TabularInline):
    model = ShiftAssignment
    extra = 0
    readonly_fields = ("registered_at",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "leader")
    filter_horizontal = ("members",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "location", "is_active")
    list_filter = ("is_active",)
    inlines = [ShiftInline]


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ("title", "event", "team", "start_time", "end_time", "capacity", "confirmed_count", "free_spots")
    list_filter = ("event", "team")
    inlines = [AssignmentInline]


@admin.register(ShiftAssignment)
class ShiftAssignmentAdmin(admin.ModelAdmin):
    list_display = ("user", "shift", "status", "registered_at")
    list_filter = ("status",)
