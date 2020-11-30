#OS walking a directory tree
import os
for folderName, subfolders, filenames in os.walk('C:\\Example'):
#There are three values in the loop, which are folder name the subfolders and files in that folder.
#They are ordered as shown above. Foldername is a string and the other two are lists.
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()
