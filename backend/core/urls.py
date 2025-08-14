from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from items.api import api as items_api
from django.conf import settings
from django.conf.urls.static import static

api = NinjaAPI()
api.add_router("/items/", items_api)  # Add your router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),  # Use NinjaAPI.urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
