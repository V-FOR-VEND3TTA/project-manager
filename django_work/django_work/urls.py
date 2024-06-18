from django.contrib import admin
from django.urls import path
from projects.views import current_time

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', current_time),
]
