from . import views
from django.urls import path


app_name = 'job'

urlpatterns = [
    path('', views.job_list),
    path('<int:id>', views.job_details, name='job-details')
]
