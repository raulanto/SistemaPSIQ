from django.contrib import admin
from django.urls import path

from core.views import DashboardView

app_name = 'app'

urlpatterns = [
    path('core/', DashboardView.as_view(), name='dashboard'),
]
