from tkinter import *
from tkinter import filedialog
from PIL import Image
import codecs
from pytesseract import image_to_string
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
#path='C:/Users/user/Desktop/rules.png'
text = image_to_string(Image.open(root.filename), lang='tel')
print(text)
file=codecs.open('img2.txt', 'w' ,'utf_8').write(text)
    