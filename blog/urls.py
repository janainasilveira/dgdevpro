from django.urls import path
from . import views

urlpatterns = [
#  path('', views.portao),
    path('', views.post_list, name='post_list'),
    path('sala', views.sala),
    path('quarto', views.quarto)
]