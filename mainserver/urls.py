from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('srform/', views.srform_page, name='srform_page'),
]