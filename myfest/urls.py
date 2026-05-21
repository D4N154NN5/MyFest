from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("events/", include("apps.events.urls")),
    path("", include("apps.accounts.urls")),
]
