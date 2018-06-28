# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:45:46 2018

@author: user
"""
###########addition
a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
mat1= [[input("enter the elements of mat1:") for j in range(b)] for i in range(a)]
mat2=[[input("enter the elements of mat2:") for j in range(b)] for i in range(a)]
result = [[int(mat1[i][j]) + int(mat2[i][j]) for j in range(0,b)] for i in range(0,a)]
for r in result:
    print(r)
###########substraction
a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
x= [[input("enter the elements of mat1:") for j in range(b)] for i in range(a)]
y=[[input("enter the elements of mat2:") for j in range(b)] for i in range(a)]
result = [[int(x[i][j]) - int(y[i][j]) for j in range(0,b)] for i in range(0,a)]
for r in result:
   print(r)   
#######multiplication
a=int(input("enter no.of rows:"))
b=int(input("enter no.of columns:"))
mat1=[[input("enter the elements of mat1:") for j in range(b)]for i in range(a)]
mat2=[[input("enter the elements of mat2:") for j in range(b)]for i in range(a)]
result=[[int(sum(a*b for a,b in zip(mat1,mat2))) for mat2 in zip(*mat2)] for mat1 in mat1]
for r in result:
   print(r) 
#result[i][j] += mat1[i][k] * (mat2[k][j])
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
######prime numbers
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
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]> nlist[i+1]:              #swapping using 2 variables
                nlist[i] =nlist[i]+nlist[i+1]
                nlist[i+1] =nlist[i]-nlist[i+1]
                nlist[i]=nlist[i]-nlist[i+1]
                 
mylist = [14,46,43,27,578,41,45,21,70]
bsort(mylist)
print(mylist)
#########ssort
sList = [1,5,6,43,42,98,75,32,12]
def ssort(List):
    for i in range(len(List)):
        min = i
        for k in range(i,len(List)):
            if List[k] < List[min]:
                min = k
        swap(List, min, i)
def swap(Lst, x, y):
    temp = Lst[x]      #swapping using a temp variable
    Lst[x] = Lst[y]
    Lst[y] = temp
ssort(sList)
print(sList)
#################BFS
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            print (s, end = " ")
 
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)
#########heapsort
def swap(i, j):                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 

def heapify(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and sqc[i] < sqc[l]:   
        max = l   
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heap_sort():     
    end = len(sqc)   
    start = end // 2 - 1 
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)   
       
sqc = [2, 7, 1, -2, 56, 5, 3]
heap_sort()
print(sqc)
############DFS
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited[v]= True
        print(v,x)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    def DFS(self,v):
        visited = [False]*(len(self.graph))
        self.DFSUtil(v,visited)
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3) 
print("DFS from (starting from vertex 2)")
g.DFS(2)
###############quicksort
def partition(arr,low,high):
    i = ( low-1 )         
    pivot = arr[high]     # pivot
    for j in range(low , high):          # If current element is smaller than or
                                         # equal to pivot
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]) 
