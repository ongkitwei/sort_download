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
sort_zip = ".zip"
sort_doc = ".docx"
sort_ppt1 = ".ppt"
sort_ppt2 = ".pptx"
sort_text = ".txt"

vid_folder = "VIDEOS"
Pic_folder = "PICTURES"
Pdf_folder = "PDF"
Zip_folder = "ZIP"
Doc_folder = "DOCS"
ppt_folder = "PPT"
text_folder = "TEXT"

no_counter = 0
########################################### FUNCTIONS ###########################################
def generate_new_folder(sort_based_on):
    path = os.path.join(download_dir + "/", sort_based_on)
    
    if os.path.isdir(path) == True:
        return True
    else:
        os.makedirs(path)
        
    


def cut_files(sort_based_on):
    path = os.path.join(download_dir + "/", sort_based_on)
    shutil.move(download_dir + "/" + filename, path + "/" + filename)



def count_files(sort_based_on, counter1):
    path = os.path.join(download_dir + "/", sort_based_on)
    list_folder_dir = os.listdir(path)
    for filename in list_folder_dir:
        global counter1_value
        counter1 = counter1 + 1
        counter1_value = counter1

    
################################################################################################


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


for filename in list_download_dir:
    if filename.endswith(sort_zip):
        generate_new_folder(Zip_folder)
        cut_files(Zip_folder)
        

for filename in list_download_dir:
    if filename.endswith(sort_doc):
        generate_new_folder(Doc_folder)
        cut_files(Doc_folder)
        
        
for filename in list_download_dir:
    if filename.endswith(sort_ppt1) or filename.endswith(sort_ppt2):
        generate_new_folder(ppt_folder)
        cut_files(ppt_folder)
        

for filename in list_download_dir:
    if filename.endswith(sort_text):
        generate_new_folder(text_folder)
        cut_files(text_folder)
        

count_files(vid_folder, no_counter)
print(vid_folder + ": " + str(counter1_value))

count_files(Pic_folder, no_counter)
print(Pic_folder + ": " + str(counter1_value))

count_files(Pdf_folder, no_counter)
print(Pdf_folder + ": " + str(counter1_value))

count_files(Zip_folder, no_counter)
print(Zip_folder + ": " + str(counter1_value))

count_files(Doc_folder, no_counter)
print(Doc_folder + ": " + str(counter1_value))

count_files(ppt_folder, no_counter)
print(ppt_folder + ": " + str(counter1_value))

count_files(text_folder, no_counter)
print(text_folder + ": " + str(counter1_value))



