# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
x,y=np.loadtxt('book.csv',unpack= True, delimiter=',')
plt.plot(x,y)
plt.title('first program')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.show()
plt.legend(loc='upper left',title='Legend')
plt.annotate('highest point',xy=(14,26),xytext=(10,28),
             arrowprops=dict(facecolor='red',shrink=0.05),)
plt.xticks([2,4,6,8,10,12,14,16]) 
plt.xlim(3)
plt.savefig('out1.jpeg')
plt.show()
#############scatterplot
import matplotlib.pyplot as plt
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sz=90
plt.scatter(marks_range, math_marks, sz,label='Math marks', color='c')
plt.scatter(marks_range, science_marks, label='Science marks', color='r')
plt.title('Scatter Plot')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()
##########4
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(x, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language")
plt.show()
##############5 pie
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.title("PopularitY of Programming Language")
plt.pie(popularity,labels=x,autopct='%0.2f%%')
plt.show()

###################
import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('book.csv', delimiter=',')
plt.bar(data[:,0], data[:,1],)
plt.ylabel('Frequency')
plt.xlabel('Words')
plt.title('Title')

plt.show()

