from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions, authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="GOAL INTERNATIONAL BACKEND API",
        default_version='v1',
        description="GOAL INTERNATIONAL DATABASE API",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/organisations/', include('organisation.urls')),
    path('api/v1/superusers/', include('superuser.urls')),
    path('api/v1/administrators/', include('administrator.urls')),
    path('api/v1/general-employees/', include('general_employee.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
