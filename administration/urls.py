# administration/urls.py

from django.urls import path
from .views import ComputerLogListView

urlpatterns = [
    path('logs/', ComputerLogListView.as_view(), name='computer_logs'),
]
