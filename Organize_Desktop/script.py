try:
    import shutil as sh
    import os
except ImportError:
    os.system("pip install pytest-shutil")
print("D for Organize Desktop\nC for Custom Location\nP for present Directory\n(Wrong Input will organize Desktop)")
choice = (input())
if choice == 'c' or choice == 'C':
    print("Give Custom Location as full path:")
    source = input()
elif choice == 'p' or choice == 'P':
    source = os.getcwd()
else:
    source = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') #This will take your OS's default Desktop Location if you have OneDrive Sync on then its suggested to give that address in source
txt_path = source + "/TXTs"
pdf_path = source + "/PDFs"
img_path = source + "/IMGs"
vid_path = source + "/Videos"
zip_path = source + "/Zip"
ipynb_path = source + "/ipynb Files"

#number of files var
no_txt = 0
no_pdf = 0
no_img = 0
no_vid = 0
no_zip = 0
no_ipy = 0


for f in os.listdir(source):
    name, ext = os.path.splitext(f)
    print(ext)

    try:
        if not ext:
            pass
        elif ext in {".txt"}:
            try: 
                os.mkdir(txt_path) 
            except:
                pass
            sh.move(os.path.join(source, f), os.path.join(txt_path, f))
            no_txt = no_txt + 1
        elif ext in {".pdf"}:
            try: 
                os.mkdir(pdf_path) 
            except:
                pass
            sh.move(os.path.join(source, f), os.path.join(pdf_path, f))
            no_pdf = no_pdf + 1
        elif ext in {".jpeg",".jpg",".gif",".png",".tiff",".svg"}:
            try: 
                os.mkdir(img_path) 
            except:
                pass
            sh.move(os.path.join(source, f), os.path.join(img_path, f))
            no_img = no_img + 1
        elif ext in {".mp4",".avi",".wmv",".flv",".mov"}:
            try: 
                os.mkdir(vid_path) 
            except:
                pass
            sh.move(os.path.join(source, f), os.path.join(vid_path, f))
            no_vid = no_vid + 1
        elif ext in {".zip",".rar",".7z",".tar.xz",".xapk",".taz"}:
            try: 
                os.mkdir(zip_path) 
            except:
                pass
            sh.move(os.path.join(source, f), os.path.join(zip_path, f))
            no_zip = no_zip + 1
        elif ext in {".ipynb"}:
            try: 
                os.mkdir(ipynb_path) 
            except:
                pass
            sh.move(os.path.join(source, f), os.path.join(ipynb_path, f))
            no_ipy = no_ipy + 1
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        pass

print("Files Number type wise which are moved are\n")
print("TXT -> " + str(no_txt))
print("PDF -> " + str(no_pdf))
print("IMG -> " + str(no_img))
print("VID -> " + str(no_vid))
print("ZIP -> " + str(no_zip))
print("IPYNB -> " + str(no_ipy))
