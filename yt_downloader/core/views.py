from django.shortcuts import render, redirect
from pytube import *
from pytube.cli import on_progress

def youtube(request): 
  
    # checking whether request.method is post or not 
    if request.method == 'POST': 
        
        # getting link from frontend 
        link = request.POST['link'] 
        video = YouTube(link,on_progress_callback=on_progress) 
  
        # setting video resolution 
        stream = video.streams.get_lowest_resolution() 
          
        # downloads video 
        stream.download('~/Downloads') 
  
        # returning HTML page 
        return render(request, 'index.html') 
    return render(request, 'index.html')