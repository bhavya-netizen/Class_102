import cv2
import dropbox
import time
import random

from numpy import False_

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    vco = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = vco.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    vco.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BHDuUgqwizFhjUyDBO0nyxU3UwBkBxV8RzMItzjrK2AnTnhcb2_IExCxZ_iwOxTHEOpx9EAfCcFMay8NKpQj3XcyWgmy65zPBXQk7I8wIV8Hs-TXsnK6MkNw-vRrRykeYP1FjOis8YQZ"
    file  = img_name
    file_from = file
    file_to = "/c102/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
    