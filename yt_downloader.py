import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from pytube import YouTube
from pytube.cli import on_progress

link = input("Enter URL: ")
video = YouTube(link,on_progress_callback=on_progress)
#print("Title: ", video.title)
#print("Number of views: ", video.views)
#print("Length of video: ", video.length, "seconds")
#print("Description: ", video.description)
#print("Ratings: ", video.rating)
print("starting download")
stream = video.streams.get_highest_resolution()
stream.download('/Users/jeff/Desktop/yt_downloader_and_vids/downloaded_vids')
print('\n' + "download finished") 