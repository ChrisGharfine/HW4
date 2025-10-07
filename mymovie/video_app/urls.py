# video_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # READ: Displays a list of all videos
    path('', views.video_list, name='video_list'),

    # CREATE: Handles adding a new video
    path('add/', views.add_video, name='add_video'),

    # UPDATE: Handles updating an existing video
    path('update/<int:pk>/', views.update_video, name='update_video'),

    # DELETE: Handles deleting a video
    path('delete/<int:pk>/', views.delete_video, name='delete_video'),
]