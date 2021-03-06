from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/api_docs/', include_docs_urls(
        title="Sunfri API",
        description="Sunfri API documentation",
    )),
    path('v1/api/schema/', get_schema_view(
        title="Sunfri API Schema",
        description="Sunfri API schema",
        version="1.0.0"
    ), name='api_schema'),
    path("v1/users/", include("users.urls")),
    path("v1/characters/", include("characters.urls")),


] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
