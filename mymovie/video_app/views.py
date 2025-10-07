

from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_app/video_list.html', {'videos': videos})



from django.shortcuts import render, redirect
from .forms import VideoForm

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'video_app/add_video.html', {'form': form})




from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm

def update_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm(instance=video)
    return render(request, 'video_app/update_video.html', {'form': form, 'video': video})




from django.shortcuts import render, redirect, get_object_or_404
from .models import Video

def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'video_app/delete_video.html', {'video': video})