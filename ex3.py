# 1.pwd  verification prog
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):#shld cntn atleat one lowercase ltr
        break
    elif not re.search("[0-9]",p):#shld cntn atleat one digit
        break
    elif not re.search("[A-Z]",p):#shld cntn atleat one uppercaseltr
        break
    elif not re.search("[$#@]",p):#shld cntn atleat one spcl sym 
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")
#######
fname = input("Enter file name: ") #enter the path of the text file (path\txtfilename.txt)
num = 0  
with open(fname, 'r') as f: #
    for line in f:
        words = line.split()
        num += len(words)
print("Number of words:")
print(num)   
######## 
fname = input("Enter file name: ") 
places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']
fh=open('fname', 'w')   
    for item in places:
       fh.write('%s\n' % listitem)