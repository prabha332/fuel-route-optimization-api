from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "status": "running",
        "message": "Fuel Route Optimizer API 🚀",
        "endpoints": {
            "optimize": "/api/optimize-route/"
        }
    })


urlpatterns = [
    path("", home),   # 👈 FIX ADDED HERE
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]