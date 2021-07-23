from django.contrib import admin
from django.urls import path, include
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('summary/', views.order_summary, name="summary"),
    path('package_select/<package_id>', views.package_selection, name="package_selection"),
    path('confirmation/<order_id>', views.order_confirmation, name="order_confirmation"),
    path('create_subscription', views.create_stripe_subscription, name="create_subcription"),
    path('update_subscription', views.update_stripe_subscription, name="update_subscription"),
    path('invoices', views.list_stripe_invoices, name="my_invoices"),
    path('wh/', webhook, name="webhook")
]