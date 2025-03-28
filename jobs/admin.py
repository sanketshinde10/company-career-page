from django.utils.html import format_html
from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "posted_on")
    search_fields = ("title", "location")

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "job", "status", "applied_on", "view_resume")  # ✅ Added view_resume
    list_filter = ("status", "job")
    search_fields = ("name", "email", "job__title")
    
    actions = ["approve_application", "reject_application"]

    def approve_application(self, request, queryset):
        queryset.update(status="Approved")
    approve_application.short_description = "Approve selected applications"

    def reject_application(self, request, queryset):
        queryset.update(status="Rejected")
    reject_application.short_description = "Reject selected applications"

    # ✅ Function to show resume download link
    def view_resume(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank">View Resume</a>', obj.resume.url)
        return "No Resume"
    
    view_resume.short_description = "Resume"
