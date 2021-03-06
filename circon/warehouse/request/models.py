from django.db import models
from django.contrib.auth.models import User
from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog


class Request(models.Model):
    date_create = models.DateField(auto_now_add=True)
    date_request = models.DateField(null=True, blank=True)
    n_request = models.AutoField(primary_key=True)
    applicant = models.CharField(max_length=100, blank=True)
    observation = models.TextField(max_length=250, blank=True)
    status = models.CharField(max_length=1, default='0', blank=True)
    audit_log = AuditLog()

    def __str__(self):
        return self.date_request.strftime('%d-%m-%Y')


class RequestDetail(models.Model):
    relationship = models.ForeignKey(Request)
    products = models.ForeignKey('products.Products')
    quantity = models.DecimalField(max_digits=100, decimal_places=2, null=True,
                                   blank=True)
    quan_request = models.DecimalField(max_digits=10, decimal_places=2,
                                       null=True, blank=True)
    audit_log = AuditLog()
