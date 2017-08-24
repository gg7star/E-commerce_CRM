from django import forms
from ecommerce_crm.catalog.models import Category

import itertools

from ecommerce_crm.config import _PARENT_CATEGORY
from ecommerce_crm.config import _SUB_CATEGORY