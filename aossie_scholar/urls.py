from django.contrib import admin
from django.urls import path, include
from .router import router
from metrics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('metrics/', include('metrics.urls')),
    path('api/', include(router.urls)),
    path('scholarly/',views.author_search,name="author_search")
]
