from PIL import Image
import pytesseract
import os
import pandas as pd

# Path is given for for 64 bit installer
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

f = []
t = []
input_dir = r'C:/Users/Mansi Lohiya/Desktop/SET2/img/'

with open('hello.text', mode='w') as file:
                    file.write("")

for root, dirs, filenames in os.walk(input_dir):
    for filename in filenames:
        try:
            print(filename)
            f.append(filename)
            img = Image.open(input_dir+ filename)
            text = pytesseract.image_to_string(img, lang = 'eng')
            t.append(text)
            print(text)
            print('-='*20)
            with open('hello.text', mode='a+') as file:
                    file.seek(0)
                    file.write(text)
                    file.write("\n")
                    
        except:
            continue


df = pd.DataFrame(list(zip(f, t)),columns=['file_Name','Text'])

print(df)


