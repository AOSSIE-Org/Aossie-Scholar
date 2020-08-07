from django.contrib import admin

from .models import ScholarData, StarredScholar

admin.site.register(ScholarData)
admin.site.register(StarredScholar)