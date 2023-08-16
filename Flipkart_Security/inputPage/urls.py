from django.urls import path
from . import views

app_name = 'input'

urlpatterns = [
    path('input/', views.input_view, name='input_view'),
]
