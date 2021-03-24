#subsetting

#Note: 
#when I say the second element, I mean the element with index 1
#when I say element two, I mean the element with index 2


import pandas as pd
import numpy as np


# Question 1: consider the following list
a = [1,2,3,4,45,5,3,5,6,7,77]
# select the third element using square brackets and a positive index 
a[2]

# select the third element using square brackets and a negative index
a[-9]


# Question 2: consider the following list
a = [1,2,3,4,45,5,3,5,6,7,77]
# select the third item to the seventh
a[2:7]



# Question 3: consider the following list
a = [1,2,3,4,45,5,3,5,6,7,77]
# select the 5th and 7th item
[a[x] for x in [4,6]]



# Question 4: consider the following list
a = [1,2,3,4,45,5,3,5,6,7,77]
#extend it with this list: [5,5,9]
a[len(a):] = [5,5,9]
a



#Use the following data frame for subsequent questions
df = pd.DataFrame(np.arange(0,100).reshape(25,4), columns = list('wxyz'))
df


#Question 5
#List all the column labels.

list(df.columns.values)

#Question 6:
#Select column x.
df['x']


#Question7:
#select columns x and z
df[['x','z']]

#Question 8:
#select rows 20 to 23
df[20:24]

#Question 9:
#select rows 20 to 23 for column w and y
df.iloc[20:24,[0,2]]

#Question 10:
#select all rows where column x has either value 61,73, or 89
df[df['x'].isin([61,73,89])]



#Use the following numpy array for subsequent questions
#numpy
a = np.arange(100).reshape(50,2) #2D
a

#Question is 11
#select rows 1, 2, 5, of column 1
a[[1,2,5],1]

#Question 12
#prepare a tuple including a slice for row 10 to 13
#and also limit the output to column 1
#use that tuple to subset a
a[10:14,1]
