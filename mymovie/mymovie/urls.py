# myvideostore/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This is the default admin URL
    path('', include('video_app.urls')), # This line routes requests to your app's URLs
]