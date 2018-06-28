
"""
Spyder Editor

This is a temporary script file.
"""
# first prog
print("sivakumari");

f = int(input('Enter the temp in fahrenheit:'))
c = (5/9)*(f-32)
print('temp in celsius' +str(c))
# second prog
firstname = input('Enter first name:')
lastname = input('Enter last name:')
print(lastname +' '+ firstname )
############

#third prog
time = int(input('Enter time in sec :'))
if time>3600:
    minu=time//60
    print(minu)
    sec=time%60
    hrs= minu//60
    minu=minu%60
    print('%d' %hrs+"hrs" +" "+'%d' %minu+"min" +" "+'%d' %sec+"sec")    
else:

     minu=time//60
     sec=time%60 ; print('%d' %minu+"min"+" "+'%d' %sec+"sec")
    
    
#print a sent
sentence =input("Enter a sentence:")
print(sentence)


# 4 ii lowercase sent

sentence =input("Enter a sentence:")
print(sentence.lower())
######rep vowel in capital
s =input("Enter a sentence :")
v=" "
vowels = ['a','e','i','o','u']
for i in s:
    if i in vowels:
        v = v+i.upper()
    else :
       v=v+i
print (v)
############ rev of a sent
sentence =input("Enter a sentence :")
result = sentence.split()
print(result)
result.reverse()
print(result)
stringg = " ".join(result)
print(stringg)
########### rep vowels with null
s =input("Enter a sentence :")
v=" "
vowels = ['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in vowels:
              s=s.replace(i,"") 
print(s)             
########### char replacement
str = input("Enter a word:")
lstr=str.lower()#converts given string to lowercase
newstr=""
for x in range(len(lstr)):
    if lstr[x]=='b':
        newstr+='v'#if the contains b then append the null string with v in place of b
        continue
    elif lstr[x]=='v':
        newstr+='b'#if the contains b then append the null string with v in place of b
        continue
    else:
        newstr+=lstr[x]
print(newstr)

##########to find lenth of a sentence
sentence =input("Enter a sentence :")
print(len(sentence))
##########
sentence = (input("Enter a sentence :"))
x=len(sentence)
for i in range(0,x,1):
     if i % 2 == 0:
          print( sentence[i].lower())
     else:
          print( sentence[i].upper())
################
d={'Mexico':'MexicoCity','China':'Beijing','France':'Paris','Belgium':'Brussels','Argentina':'Buenos'}       
d3=sorted(d.keys())
for key in d3:
    print("%s: %s" %(key, d[key])) 


####### 
list1 =[0,1,1.5,2,3.7,5.6,8,13,21.5,34,55]
rounded = map(round, list1)
print(rounded)
newlist = [round(x) for x in list1]
print(newlist)
result = filter(lambda x:x%2== 0,list1)
print(result)
odd=[x %2 != 0 for x in [87,98,90]]
print(odd)
############### call by bject
#python neither suprts call by value and call by reference
def increment(n):
    n=n+1
    print(n)
num=1    
increment(num)
print(num)
  ######3
