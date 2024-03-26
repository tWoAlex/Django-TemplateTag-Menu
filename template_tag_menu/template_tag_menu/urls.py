from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('example_usage.urls')),
    path('admin/', admin.site.urls),
]
