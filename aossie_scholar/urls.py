from django.contrib import admin
from django.urls import path,include
from aossie_scholar.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(),name='home'),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('metrics.api.urls'))
]