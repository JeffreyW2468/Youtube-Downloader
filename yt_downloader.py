import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from pytube import YouTube
link = input("Enter URL: ")
video = YouTube(link)
#print("Title: ", video.title)
#print("Number of views: ", video.views)
#print("Length of video: ", video.length, "seconds")
#print("Description: ", video.description)
#print("Ratings: ", video.rating)
stream = video.streams.get_highest_resolution()
stream.download()
print("download finished") 
