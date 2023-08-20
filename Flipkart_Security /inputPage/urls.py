from django.urls import path
from . import views

app_name = 'input'

urlpatterns = [
    path('input/', views.input_view, name='input_view'),
    path('get text', views.form_view, name='text_view'),
    # path('save-text/', views.save_text, name='save_text'),
    path('/button_quick', views.button_quick, name='button_quick'),
    path('/button_full', views.button_full, name='button_full'),
    path('uploadForm/', views.form_view, name='form_view')
]
