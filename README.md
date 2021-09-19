# Youtube-Downloader
for anyone who wants to get an mp4 of their favorite vids

Setup instructions: 
Change your directory to root directory by running this in terminal (mac/linux/etc) or command prompt (windows) using 'cd /' for mac and backslash for windows

;O

Now that that hopefulllly worked, run the python installer for python 3 in command line to pull the python youtube packages necessary for the script to work: 
'pip3 install pytube'

Now, make sure that your python version is on 3.9 (I'm pretty sure that pytube doesn't work for older versions --> 'python --version'); if your version is too old, check online for different means of updating your version or consider installing 3.9 through brew if you have mac or linux (pyfix.txt is in this repository for mac/linux brew troubleshooting)

If you survived that without punching a hole in your computer from poring the pages of Stack, you can now move on to setting up the file on your filesystem.
There are two ways you can do this:

Go to Code on the front page of the repo, download the zip file, move the folder to wherever you want, and run the script there.
Or, for those command line oriented individuals, you change directory to one that you like (maybe desktop or something) and run 'git clone https://github.com/JeffreyW2468/Youtube-Downloader.git" --> this will pull the repository from the github site and download it directly to the current working directory

----

Now that you've done these steps, you can navigate to the folder that the script is in (Youtube-Downloader, in all probability) and run the script by running: 
'python3 yt_downloader.py'

Paste your youtube video link, wait a minute or two, and voila! Your favorite video is now in that folder :))
P.S. to have it download to a specific folder, edit the script and pass the full directory path as an argument in the parentheses of the .download() function (i.e. Users/jeff/blah/blah2). If it throws an error, just take a look at the pytube documentation for the download function online and work accordingly. 
