from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from reports.register_generator import GenerateRegister
from reports.search import SearchResult
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ecommerce_crm.catalog.views.index', name='home'),
    url(r'^catalog/', include('ecommerce_crm.catalog.urls')),
    url(r'^useraccounts/', include('useraccounts.urls')),
    url(r'^print/', include('ecommerce_crm.prints.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/','ecommerce_crm.reports.views.search_form'),
    url(r'^search_result/', SearchResult.as_view(), name='search_result'),
    url(r'^save_fields', 'ecommerce_crm.reports.views.save_fields'),
    url(r'^list_saved_registers', 'ecommerce_crm.reports.views.list_saved_registers'),
    url(r'daily_result', 'ecommerce_crm.reports.register.daily_report_result', name='daily_report_result'),
    url(r'consultancy_funds_report', 'ecommerce_crm.reports.register.consultancy_funds_report', name='consultancy_funds_report'),    
    url(r'tds_report', 'ecommerce_crm.reports.register.tds_report_result', name='tds_report_result'),    
    url(r'payment_report', 'ecommerce_crm.reports.register.payment_register', name='payment_register'),
    url(r'suspense_clearance_register', 'ecommerce_crm.reports.register.suspense_clearance_register'),
    url(r'servicetax', 'ecommerce_crm.reports.register.servicetax_register'),
    url(r'^main_register', 'ecommerce_crm.reports.register.main_register', name='main_register'),
    url(r'^proforma_register', 'ecommerce_crm.reports.register.proforma_register'),
    url(r'^non_payment_register', 'ecommerce_crm.reports.register.non_payment_register'),
    url(r'^client_register', 'ecommerce_crm.reports.register.client_register', name='client_register'),
    url(r'^material_report', 'ecommerce_crm.reports.register.material_report'),
    url(r'^lab_report', 'ecommerce_crm.reports.register.lab_report'),
    url(r'^suspense_register', 'ecommerce_crm.reports.register.suspense_register'),
    url(r'^registered_users', 'ecommerce_crm.reports.register.registered_users'),
    url(r'^filter_sub_category/', 'ecommerce_crm.reports.views.filter_sub_category'),
    url(r'^bill/', 'ecommerce_crm.prints.views.bill'),
    url(r'^suspense_bill/', 'ecommerce_crm.prints.views.suspense_bill'),
    url(r'^quoted_bill/', 'ecommerce_crm.prints.views.quoted_bill'),
    url(r'^tax/', 'ecommerce_crm.prints.views.tax'),
    url(r'^bills/', include('ecommerce_crm.bills.urls')),
    url(r'^suspense/', include('ecommerce_crm.suspense.urls')),
    url(r'^generate_register/', GenerateRegister.as_view(), name='view_register'),
    url(r'^history/','ecommerce_crm.reports.previous_history.history'),
    url(r'^details/','ecommerce_crm.reports.previous_history.details'),
    url(r'^proforma_details/','ecommerce_crm.reports.previous_history.proforma_details'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^voucher/', include('ecommerce_crm.voucher.urls')),
    url(r'^receipt/', 'ecommerce_crm.prints.views.receipt'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^programmeletter/', 'ecommerce_crm.programmeletter.views.programmeletter'),
    url(r'pending_clearance_register', 'ecommerce_crm.reports.register.pending_clearance_register'),
    url(r'tada_register', 'ecommerce_crm.reports.register.tada_register'),
    url(r'tada_othercharges_register', 'ecommerce_crm.reports.register.tada_othercharges_register'),
    url(r'client_details_according_to_amount', 'ecommerce_crm.reports.register.client_details_according_to_amount'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)