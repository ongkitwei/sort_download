import os 
import shutil
#from tkinter import *


download_dir = r"C:\Users\ASUS\Downloads"       #change this according to ur download dir
list_download_dir = os.listdir(download_dir)



sort_vid = ".mp4"
sort_pic1 = ".png"
sort_pic2 = ".jpeg"
sort_pic3 = ".jpg"
sort_pdf = ".pdf"

vid_folder = "Videos"
Pic_folder = "Pictures"
Pdf_folder = "PDF"


def generate_new_folder(sort_based_on):
    path = os.path.join(download_dir + "/", sort_based_on)
    
    if os.path.isdir(path) == True:
        return True
    else:
        os.makedirs(path)
        
    


def cut_files(sort_based_on):
    path = os.path.join(download_dir + "/", sort_based_on)
    shutil.move(download_dir + "/" + filename, path + "/" + filename)




for filename in list_download_dir:
    if filename.endswith(sort_pic1) or filename.endswith(sort_pic2) or filename.endswith(sort_pic3):
        generate_new_folder(Pic_folder)
        cut_files(Pic_folder)
        

for filename in list_download_dir:
    if filename.endswith(sort_vid):
        generate_new_folder(vid_folder)
        cut_files(vid_folder)


for filename in list_download_dir:
    if filename.endswith(sort_pdf):
        generate_new_folder(Pdf_folder)
        cut_files(Pdf_folder)
        















"""
root = Tk()

#creating a label widget
myLabel = Label(root, text="Hello world!")

#reflecting it onto the screen
myLabel.pack()

root.mainloop()

#print(list_download_dir)
"""
