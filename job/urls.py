from . import views
from django.urls import path


app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job-list'),
    path('add', views.add_job, name='add-job'),
    path('<str:slug>', views.job_details, name='job-details'),
]
