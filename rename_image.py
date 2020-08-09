import os
import glob


def rename_all(source):
    os.chdir(source)
    all_files = os.listdir(source)
    files_len = len(all_files)/2
    i = 0
    for file in glob.glob("*.jpg"):
        try:
            #os.rename(file[:-3]+'xml','{}.xml'.format(i))
            os.rename(file,'{}.jpg'.format(i))
        except Exception as e:
            os.remove(file)
            print(e)
    
        i += 1
    

if __name__ == "__main__":
    src = "/home/gardin/Desktop/placas"
    rename_all(src)
