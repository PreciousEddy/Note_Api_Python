import os
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator

from rest_framework import permissions

class NoteAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.base_path = ""
        
        if "LIVE" in os.environ:
            schema.schemes = ["https"]
        else: 
            schema.schemes = ["http"]
        
        return schema

members_schema_view = get_schema_view(
    openapi.Info(
        title = "Precious Edmund Note API",
        default_version = "v1",
        description = "Note API documentation endpoints",
        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(email="edmundprecious23@gmail.com"),
        license=openapi.License(name="Presh"), 
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    urlconf="API.urls",
    generator_class = NoteAPISchemaGenerator,
)

urlpatterns = [
    
    path("", members_schema_view.with_ui("swagger", cache_timeout=0),
         name="notes"),
    path('admin/', admin.site.urls),

    path('', include('API.urls')),
]
