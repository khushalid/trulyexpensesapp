from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='monthly_cost'),
    path('get_cost_data/',views.get_cost_data, name='get_cost_data')
]
