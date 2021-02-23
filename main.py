from pytube.cli import on_progress
from pytube import YouTube
import os

video_url = input("Past Your url here : ")
try:
    yt = YouTube(video_url, on_progress_callback=on_progress)
    yt.streams\
        .filter(file_extension='mp4')\
        .get_highest_resolution()\
        .download(os.path.curdir+"/video")

except EOFError as err:
    print(err)

else:
    print("Download Complete!")