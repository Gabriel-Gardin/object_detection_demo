import os
import glob


def rename_all(source):
    os.chdir(source)
    all_files = os.listdir(source)
    i = 0
    for file in glob.glob("*.jpeg"):
        try:
            #os.rename(file[:-3]+'xml','{}.xml'.format(i))
            os.rename(file,'{}.jpg'.format(i+2204))
            i += 1
        except Exception as e:
            os.remove(file)
            print(e)
    

if __name__ == "__main__":
    src = "/home/gardin/Documents/Estagio_LET/let_obj_detection/all_dataset_final"
    rename_all(src)
