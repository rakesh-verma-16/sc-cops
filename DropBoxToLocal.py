# Cron Job to download from DropBox

try:
import os
import sys
import dropbox
from config import TOKEN,LOCAL,DROPBOX_FOLDER
import time
	import unicodedata
except Exception as e:
	print e

dropbox_client = dropbox.Dropbox(TOKEN)

#We recursively check the dropbox folder to list all files.

results=dropbox_client.files_list_folder(DROPBOX_FOLDER,recursive=True).enteries

#iterate through the files on dropbox and obtain the respective file path.
for object in results:
	if isinstance(object,dropbox.files.FileMetadata):
		path_to_file = object.path_display
		# print path_to_file #/Apps/socialcopsync
		#convert unicode string into ascii
		path_to_file = unicodedata.normalize('NFKD', path_to_file).encode('ascii','ignore')
		
		#dowload the file from dropbox
	metadata, file_result = dropbox_client.files_download(path_to_file)
	file_result = file_result.content
		#set the local file path where we want the files to be synced and stored.
		path_to_file = path_to_file.replace(DROPBOX_FOLDER,"/Users/rakesh/Desktop/jedi")
		# print "Final path is: " . path_to_file
		#if file doesn't exist then create the respective directories before writing it to disk.
		if not os.path.exists(os.path.dirname(path_to_file)):
			try:
				os.makedirs(os.path.dirname(path_to_file))
			except OSError as exc: # Guard against race condition
				if exc.errno != errno.EEXIST:
					raise
		# print "writing to file now\n"
		with open(file_path, "w+") as f:
			f.write(file_result)

