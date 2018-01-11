



# The following script uses watchdog which helps in firing an event whenever 
# a directory undergoes any modification. Whenever a new file/directory is created
# we push the change onto dropbox which will help us in synchronizing contents across
# various systems.

# This script has to be run in the background as a daemon.

try:
import os
import time
import dropbox
from config import TOKEN,LOCAL,DROPBOX_FOLDER
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

except Exception as e:
	print e

client = dropbox.Dropbox(TOKEN)

# https://stackoverflow.com/questions/18599339/python-watchdog-monitoring-file-for-changes
# Help taken from the link mentioned above.
class MyHandler(FileSystemEventHandler):
	#event which gets fired whenever our specifies directory undergoes any change
	#specify the directory name to be watched in the config.py file
	
	def on_modified(self,event):
		# Iterating over all the files in my local directory.
for filename in os.listdir(LOCAL):
	DB_PATH = DROPBOX_FOLDER + "/" + filename
	# print DB_PATH
	try:
		with open(os.path.join(LOCAL, filename), 'rb') as f:
			data=f.read()
		client.files_upload(data,DB_PATH,mode=dropbox.files.WriteMode.overwrite)
	except Exception as e:        
		print e

if __name__ == "__main__":    
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=LOCAL, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()