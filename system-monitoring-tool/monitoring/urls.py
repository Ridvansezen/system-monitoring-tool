from django.urls import path
from .views import SystemDataView

urlpatterns = [
    path('', SystemDataView, name='system_data_view'),
]