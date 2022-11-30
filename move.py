import os
import shutil


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

path = os.path.join(download_dir + "/", Pdf_folder)

for filename in list_download_dir:
    if filename.endswith(sort_pdf):
        shutil.move(download_dir + "/" + filename, path + "/" + filename)