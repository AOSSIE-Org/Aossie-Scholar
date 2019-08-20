from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('metrics/', include('metrics.urls')),
    path('api/', include(router.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
