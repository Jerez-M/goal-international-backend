from django.urls import path
from general_employee import views

urlpatterns = [
    path('', views.CreateGeneralEmployeeView.as_view(), name='create_general_employee'),
    path('<int:pk>/', views.GeneralEmployeeReadUpdateDestroyView.as_view()),
    path('get-all-general_employees/', views.GetAllGeneralEmployees.as_view()),
]
