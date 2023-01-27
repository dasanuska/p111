import os
import shutil

#.exe, .msi, .gif, .png, .jpg, .jpeg, .csv, .pdf, .xsl, .xlsx, .ppt, .pptx

from_dir ="c:/users/ADMIN/Downloads"
to_dir ="c:/whitehatjr/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

#Move ALL Image file from Downloads Folder To Another Folder
for file_name in list_of_files:

    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
