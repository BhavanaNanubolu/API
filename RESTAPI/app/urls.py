from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('edit/<int:id>',views.update),
]