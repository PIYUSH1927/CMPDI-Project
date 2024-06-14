from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    department_id = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.department_name

class Bill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=200, verbose_name="Contract No.")
    field2 = models.CharField(max_length=200, verbose_name="Item Description")
    field3 = models.CharField(max_length=200, verbose_name="Invoice No.")
    field4 = models.CharField(max_length=200, verbose_name="Invoice Date.")
    field41 = models.CharField(max_length=200, verbose_name="Vendor Name")
    field5 = models.CharField(max_length=200, verbose_name="Amount")
    field6 = models.CharField(max_length=200, verbose_name="Purchase Order")
    field7 = models.CharField(max_length=200, verbose_name="Service Entry Sheet")
    field8 = models.CharField(max_length=200, verbose_name="BC No.")
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('not_paid', 'Not Paid'),
    ]
    field9 = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, verbose_name="Payment Status")
    field10 = models.CharField(max_length=200, verbose_name="Payment Date")
    field11 = models.FileField(upload_to='invoices/', null=True, blank=True, verbose_name="Invoice pdf")

    def __str__(self):
        return f"{self.field1} - {self.field2}"