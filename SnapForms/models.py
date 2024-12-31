from django.db import models


class ExpenseReport(models.Model):
    # Status choices for the expense report
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('D', 'Denied'),
    ]

    employeeName = models.CharField(max_length=100)
    employeeId = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    date = models.DateField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)

    # Status field to track the state of the expense report
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P',  # Default status is 'Pending'
    )

    def __str__(self):
        return f"{self.employeeName} - {self.date} - {self.get_status_display()}"
