from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path ('task/<str:pk>/', views.task, name="task"),
    path('add-task/', views.add_task, name="add-task"),
    path('delete/<str:pk>/', views.delete_task, name="delete"),
    path('update-task/<str:pk>/', views.update_task, name="update-task"),
    path('completed-task/<str:pk>/', views.completed_task, name="completed-task"),

    path('register-register.html/', views.loginPage, name="login-register"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),


    path('welcome/', views.welcomePage, name="welcome"),
]