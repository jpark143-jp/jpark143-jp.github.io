""" Module creates excel file with some columns
    Author : JungHwan Park
    Date : 08.05.2021
    Email : jpark143@g.ucla.edu
    Content : to excel
"""

import numpy as np
import openpyxl

result = {}
for d in data :
   result.update(d)
data_items = result.items()
data_list = list(data_items)

df = pd.DataFrame(data_list, columns = ['profile', 'consistency_score'])   

# Using pandas cut function to create references for consistency score.
cs = df.iloc[:,1]
num_days_for_1post = 1/cs

df['Grade']=pd.cut(df.num_days_for_1post,[0, 0.5, 1, 2, 7, 30, np.inf],labels=['A_Excellent','B_Good', 'C_Acceptable', 'D_Questionable', 'E_Poor', 'F_Unacceptable'], include_lowest=True)
description = []
for i in range(82):
    description.append(f'takes {round(df.num_days_for_1post[i],2)}days for 1 post : {df.Grade[i]}')
description
df['description'] = description

df.to_excel("Consistency_Score_updated5.xlsx")  # Create excel file which summarize consistency scores with the grade.