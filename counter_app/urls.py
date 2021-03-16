from django.urls import path
from . import views

urlpatterns = [
    path('', views.counter),
    path('add_2_counter', views.add_2_counter),
    path('destroy_session', views.delete_session),
]