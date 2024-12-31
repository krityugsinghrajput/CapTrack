from django.contrib import admin
from django.utils.html import format_html
from .models import ExpenseReport


# Customizing the ExpenseReport Admin
class ExpenseReportAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('employeeName', 'employeeId', 'department', 'amount', 'status', 'date', 'view_receipt')

    # Add filters for the status
    list_filter = ('status',)

    # Add search fields for convenience
    search_fields = ('employeeName', 'employeeId', 'department', 'category', 'status')

    # Allow bulk actions to update status
    actions = ['mark_as_approved', 'mark_as_pending', 'mark_as_denied']

    # Action to mark selected reports as Approved
    def mark_as_approved(self, request, queryset):
        queryset.update(status='A')

    mark_as_approved.short_description = "Mark selected reports as Approved"

    # Action to mark selected reports as Pending
    def mark_as_pending(self, request, queryset):
        queryset.update(status='P')

    mark_as_pending.short_description = "Mark selected reports as Pending"

    # Action to mark selected reports as Denied
    def mark_as_denied(self, request, queryset):
        queryset.update(status='D')

    mark_as_denied.short_description = "Mark selected reports as Denied"

    # Add a method to view the receipt PDF
    def view_receipt(self, obj):
        if obj.receipt:
            return format_html('<a href="{}" target="_blank">View Receipt</a>', obj.receipt.url)
        return "No Receipt"

    view_receipt.short_description = "Receipt"

# Register the model with the custom admin
admin.site.register(ExpenseReport, ExpenseReportAdmin)
