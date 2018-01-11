# sc-cops
Jedi Learning and Information Sharing System

- Prerequisites
   -Dropbox
   -WatchDog
  
- Installation (Requirements)
   --sudo pip install dropbox
   --sudo pip install watchdog
   
# How I G0t it running

1.) Created an App on Dropbox and got the authentication token to allow file upload and download from CLI/API.

2.) Set watchdog on a Local Directory which whenever updated pushes to DropBox.

3.) Set up a cron job to download the new files from DropBox every 2 minutes.

*/2 * * * * /usr/bin/python /home/arpan/gitProjects/FolderSync/fileDownload.py

