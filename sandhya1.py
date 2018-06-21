
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
     sec=time%60
     print('%d' %minu+"min"+" "+'%d' %sec+"sec")
    
    
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
vowels = ['a','e','i','o','u']
for i in s:
    if i in vowels:
              s=s.replace("i", "") 
print(s)             
###########
s=input("Enter a sentence :")
print(s.replace('v', 'b')) 
print(s.replace('b', 'v'))
     
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
###########addition
mat1=[[1,2,3],[4,5,3]]
mat2=[[1,2,3],[4,5,3]]
result=[[0,0,0],[0,0,0]]
print(len(mat1[0]))
       #result[i][j] = (mat1[i][j] + mat2[i][j])
result = [[mat1[i][j] + mat2[i][j]  for j in range(len(mat1[0]))] for i in range(len(mat1))]
for r in result:
    print(r)

###########substraction
#a=int(input("enter no.of rows:"))
#b=int(input("enter no.of columns:"))
#x= [[input("enter the elements of mat1:") for j in range(b)]for i in range(a)]
#y= [[input("enter the elements of mat2:") for j in range(b)]for i in range(a)]
#res =int[[[ 0 for j in range(b)]for i in range(a)[]]
#for i in range(a):
#   for j in range(b):
#        res[i][j] = x[i][j] - y[i][j]
#        print(res)
mat1=[[1,2],[4,5,]]
mat2=[[1,2],[4,5]]
result=[[0,0],[0,0]]
print(len(mat1[0])) #######gives no.of ele in first list in mat1
print(mat1)
for i in range(len(mat1)):
   for j in range(len(mat1[0])):
       result[i][j] = result = [[mat1[i][j] - mat2[i][j]  for j in range(len(mat1[0]))] for i in range(len(mat1))]
for r in result:
   print(r)   
   #######multiplication
mat1 = [[1,0],
        [0,1]]
mat2= [[1,0],
       [0,1]]

result = [[0,0],
         [0,0]]

# result[i][j] += mat1[i][k] * (mat2[k][j])
result = [[sum(a*b for a,b in zip(mat1_row,mat2_col)) for mat2_col in zip(*mat2)] for mat1_row in mat1]

for r in result:
   print(r)
   ####### transpose 
   X=   [[12,7,],
         [4 ,5,]]
result = [[0,0],
         [0,0]]    

for i in range(len(X)):
     for j in range(len(X[0])):
          result[j][i] = X[i][j]

for r in result:
     print(r)

 ######
n=int(input("enter a num:"))
for num in range(2,n + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
#########imp stack using list
san = ["sandhya", "Rohitha", "suchi","sarika"]
san.append("Ram")
san.append("sai")
print(san)
print(san.pop())
print(san)
print(san.pop())
print(san)        
 #########imp queue using list
sandhya = ["sandhya", "Rohitha", "suchi","sarika"]
sandhya.insert("Ram")
sandhya.insert("sai")
print(sandhya)
print(sandhya.pop())
print(sandhya)
print(sandhya.pop())
print(sandhya) 
##########
def bsort(nlist):
    for passnum in range(len(mylist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]> nlist[i+1]:
                nlist[i] =nlist[i]+nlist[i+1]
                nlist[i+1] =nlist[i]-nlist[i+1]
                nlist[i]=nlist[i]-nlist[i+1]
                 
mylist = [14,46,43,27,57,41,45,21,70]
bsort(mylist)
print(mylist)
#########ssort
sList = [1,5,6,3,42,98,75,32,12]
def selection_sort(List):
    for i in range(len(List)):
        min = i
        for k in range(i,len(List)):
            if List[k] < List[min]:
                min = k
        swap(List, min, i)
    print(List)
def swap(Lst, x, y):
    temp = Lst[x]
    Lst[x] = Lst[y]
    Lst[y] = temp

selection_sort(sList)
####### 



