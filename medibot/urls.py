from dj_rest_auth.registration.views import RegisterView
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version="v1",
        description="Description of your API",
        terms_of_service="https://yourapi.com/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/register/", RegisterView.as_view(), name="auth-register"),
    path("chat/", include("chat.urls")),
    path("", schema_view.with_ui(), name="swagger-ui"),
]
