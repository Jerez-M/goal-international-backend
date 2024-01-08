from django.urls import path
from organisation import views

urlpatterns = [
    path('', views.CreateOrganisationView.as_view(), name='create_organisation'),
    path('<int:pk>/', views.OrganisationReadUpdateDestroyView.as_view()),
    path('get-all-organisations/', views.GetAllOrganisations.as_view()),
    # path('get-organisation-logo/<int:organisationId>/', views.GetOrganisationLogo.as_view()),
    # path('update-organisation-logo/<int:organisationId>/', views.update_organisation_logo),
]
