from django.contrib import admin
from django.contrib.auth.admin import *

from ecommerce_crm.reports.models import SavedRegisters

admin.autodiscover()

admin.site.register(SavedRegisters)
