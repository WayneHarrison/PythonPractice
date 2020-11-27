import shutil
shutil.copy('D:\\Personal Files\\Documents\\Python Projects\\hello.txt','D:\\Personal Files\\Documents\\Python Projects\\Copy')
#Built in copy function allowing you to copy files to other places on the harddrive we can rename it by specifying a file name too.
shutil.copytree('D:\\Personal Files\\Documents\\Python Projects\\Copy', 'D:\\Personal Files\\Documents\\Python Projects\\CopyBackup')
#Copy the entire folder and it's contents.
shutil.move()#The move function built int shutil.
#File deletion
import os
os.unlink() #Deletes one file. Can be passed a relative or absolute filepath.
os.rmdir() #Deletes one directory or folder. Folder must be empty.

shutil.rmtree() #This will delete a folder and all of it's content.
#The files deleted using these methods will not go to the recycling bin.

#Third party modules.

import send2trash
send2trash.send2trash()
#This third party module will send the files to the recycling bin instead of deleting them permanently.
