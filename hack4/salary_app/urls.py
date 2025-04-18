from django.urls import path
from . import views

urlpatterns = [
    path('', views.salary_form, name='salary_form'),              # http://127.0.0.1:8000/
    path('result/', views.calculate_salary, name='calculate_salary'),
    path('jumble/', views.jumble_word, name='jumble_word'),       # http://127.0.0.1:8000/jumble/
]
