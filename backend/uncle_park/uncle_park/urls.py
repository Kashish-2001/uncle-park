from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls')),
    path('api/spot/', include('spot.urls')),
]
