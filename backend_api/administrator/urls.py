from django.urls import path
from administrator import views

urlpatterns = [
    path('', views.CreateAdministratorView.as_view(), name='administrator'),
    path('<int:pk>/', views.AdministratorReadUpdateDestroyView.as_view()),
    path('get-all-administrator/', views.GetAllAdministrators.as_view()),
]
