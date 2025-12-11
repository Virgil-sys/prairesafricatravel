from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'message', 'rating', 'is_approved', 'created_at')
    list_filter = ['is_approved', 'rating', 'created_at']
    search_fields = ['name', 'location', 'message']
    readonly_fields = ['created_at']
    actions = ['approve_testimonials', 'reject_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} testimonial(s) approved.")
    approve_testimonials.short_description = "Approve selected testimonials"

    def reject_testimonials(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f"{queryset.count()} testimonial(s) rejected.")
    reject_testimonials.short_description = "Reject selected testimonials"
