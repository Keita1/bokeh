from django.urls import path
from . import views

app_name = 'app_plot'

urlpatterns = [
    path('', views.generate_plot),
]