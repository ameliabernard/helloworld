#Aggregating
#Merging
#Dates

#############################################
# Question 1:
# Consider the following dataframe
import pandas as pd
df1 = pd.DataFrame({'ID': [1,1,2,2,3,3],
                  'A': [1,2,3,4,4,4],
                  'B': [1,2,3,4,4,4]})
df1
#Group df1 by ID, compute the sum by group, and rename the columns to A_sum, B_sum
# Answer:
x=df1.groupby(by='ID').sum()
x
x.columns=['A_sum','B_sum']
x
#############################################
#Question 2:
# Consider the following dataframe
import pandas as pd
df1 = pd.DataFrame({'ID': [1,1,2,2,3,3],
                  'A': [1,2,3,4,4,4],
                  'B': [1,2,3,4,4,4]})
df1
#Group df1 by ID, compute the min, mean and max by group, and make sure the columns are single level
#Answer:
x=df1.groupby(by='ID').aggregate(min_A=('A',min),
                                mean_A=('A','mean'),
                                max_A=('A',max),
                                min_B=('B',min),
                                mean_B=('B','mean'),
                                max_B=('B',max))
x



#############################################
#Question 3:
import pandas as pd
df1 = pd.DataFrame({'ID': [1,3],
                  'A': [1,2],
                  'B': [1,4]})
df2 = pd.DataFrame({'ID': [1,2,3],
                  'A': [1,2,3],
                  'B': [1,4,4]})
#do a full outer merge on ID
# Answer:
pd.merge(left=df1,
        right=df2,
        how='outer',
        on='ID')


#############################################
#Question 4:
import pandas as pd
df1 = pd.DataFrame({'ID': [1,3],
                  'A': [1,2],
                  'B': [1,4]})
df2 = pd.DataFrame({'ID': [1,2,3],
                  'A': [1,2,3],
                  'B': [1,4,4]})
#do a left outer merge on ID
# Answer:
pd.merge(left=df1,
        right=df2,
        how='left',
        on='ID')



#############################################
#Question 5:
#STEP 1: Take this dataset, and read it in using pandas
'http://ballings.co/hidden/aCRM/data/chapter2/subscriptions.txt'
#STEP 2: Then compute the time elapsed between a customer's
#minimum StartDate and maximum StartDate. 
#Call this variable the "LOR" (length of relationship). 
#Since we need one row per customerid, we need to aggregate.
#STEP 3: Finally use seaborn to display the linear relationship between LOR and the customer's sum of TotalPrice.
#Answer:

data=pd.read_table('http://ballings.co/hidden/aCRM/data/chapter2/subscriptions.txt', delimiter=';', parse_dates = ['StartDate','EndDate'], 
infer_datetime_format = True)
data.head()
data.info()
LOR=data['StartDate'].max()-data['StartDate'].min()
data['StartDate'].min()

df_ag=pd.DataFrame()
df_ag=data.groupby('CustomerID').agg(min_sd=('StartDate',min),
max_ed=('EndDate',max),
price=('TotalPrice',sum))
df_ag['LOR']=df_ag['max_ed']-df_ag['min_sd']
df_ag.head()
df_ag['LOR']=df_ag['LOR'].dt.days

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

sns.lmplot(x='LOR',
            y='price',
            data=df_ag,
            fit_reg=True)
plt.show()
