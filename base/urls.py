from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name="add-task"),
    path('delete/<str:pk>/', views.delete_task, name="delete"),
    path('update-task/<str:pk>/', views.update_task, name="update-task"),

]