from django.contrib import admin
from django.utils.html import format_html
from .models import Activity, BookingActivity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_id', 'title', 'colored_category', 'price', 'price_display', 'is_active', 'display_order')
    list_filter = ('category', 'is_active')
    search_fields = ('activity_id', 'title', 'description')
    list_editable = ('price', 'is_active', 'display_order')
    ordering = ('category', 'display_order', 'title')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('activity_id', 'title', 'category', 'description')
        }),
        ('Pricing & Display', {
            'fields': ('price', 'duration', 'is_active', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    
    def colored_category(self, obj):
        colors = {
            'package': '#3b82f6',
            'activity': '#10b981',
            'transport': '#f59e0b',
            'accommodation': '#8b5cf6',
        }
        color = colors.get(obj.category, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: bold; font-size: 11px;">{}</span>',
            color,
            obj.get_category_display().upper()
        )
    colored_category.short_description = "Category"
    colored_category.admin_order_field = "category"
    
    def price_display(self, obj):
        return format_html('<span style="color: #10b981; font-weight: bold;">${}</span>', obj.price)
    price_display.short_description = "Price"
    price_display.admin_order_field = "price"


@admin.register(BookingActivity)
class BookingActivityAdmin(admin.ModelAdmin):
    list_display = ('booking', 'activity', 'quantity', 'subtotal_display')
    list_filter = ('activity__category',)
    search_fields = ('booking__reference_number', 'activity__title')
    readonly_fields = ('subtotal',)
    
    def subtotal_display(self, obj):
        return format_html('<span style="color: #10b981; font-weight: bold;">${}</span>', obj.subtotal)
    subtotal_display.short_description = "Subtotal"
