from django.urls import path
from .views import apply_for_job
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # List all jobs
    path('<int:job_id>/', views.job_detail, name='job_detail'),  # Job detail page
    path('<int:job_id>/apply/', apply_for_job, name='apply_for_job'),
]
