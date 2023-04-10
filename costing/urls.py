from . import views
from django.urls import path

urlpatterns = [
    path('', views.search, name='search'),
    path('add_job', views.add, name='add_job'),
    path('update_job/<job_id>', views.update_job, name='update_job'),
    path('total_cost/<job_id>', views.total_cost, name='tota_cost')
]
