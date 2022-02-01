from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/users/", include("users.urls")),


] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
