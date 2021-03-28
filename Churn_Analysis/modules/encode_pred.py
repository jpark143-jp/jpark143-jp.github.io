"""Module containing helper function(s) for feature engineering
"""


def encoding_Gender(Gender):
    """Function to encode Gender"""
    Gender_list={'Gender_F':0, 'Gender_M':0}
    if Gender == 'F':
        Gender_list['Gender_F']=1 
    elif Gender == 'M': 
        Gender_list['Gender_M']=1
    else : raise ValueError("Error: Wrong input")
    #Gender_list1= list(Gender_list.values())
    return(Gender_list)


def encoding_Education_Level(Education_Level):
    """Function to encode Education_Level"""
    Education_list= {'Education_Level_College' : 0, 'Education_Level_Doctorate':0, 'Education_Level_Graduate':0, 'Education_Level_High School':0, 
    'Education_Level_Post-Graduate':0, 'Education_Level_Uneducated':0, 'Education_Level_Unknown':0}
    
    if Education_Level == 'College':
        Education_list['Education_Level_College'] =  1 
    elif Education_Level == 'Doctorate': 
        Education_list['Education_Level_Doctorate'] = 1
    elif Education_Level == 'Graduate': 
        Education_list['Education_Level_Graduate'] = 1
    elif Education_Level == 'High School': 
        Education_list['Education_Level_High School'] = 1
    elif Education_Level == 'Post-Graduate': 
        Education_list['Education_Level_Post-Graduate'] = 1
    elif Education_Level == 'Uneducated': 
        Education_list['Education_Level_Uneducated'] = 1
    elif Education_Level == 'Unknown': 
        Education_list['Education_Level_Unknown'] = 1
    else : raise ValueError("Error: Wrong input")
    return(Education_list)

def encoding_Marital_Status(Marital_Status):
    """Function to encode Marital_Status"""
    Marital_Status_list={'Marital_Status_Divorced':0, 'Marital_Status_Married':0, 'Marital_Status_Single':0, 'Marital_Status_Unknown':0}
    if Marital_Status == 'Divorced':
        Marital_Status_list['Marital_Status_Divorced']=1 
    elif Marital_Status == 'Married': 
        Marital_Status_list['Marital_Status_Married']=1
    elif Marital_Status == 'Single': 
        Marital_Status_list['Marital_Status_Single']=1
    elif Marital_Status == 'Unknown': 
        Marital_Status_list['Marital_Status_Unknown']=1
    else : raise ValueError("Error: Wrong input")
    return(Marital_Status_list)


def encoding_Income_Category(Income_Category):
    """Function to encode Income_Category"""
    Income_Category_list={'Income_Category_$120K +':0, 'Income_Category_$40K - $60K':0, 'Income_Category_$60K - $80K':0, 'Income_Category_$80K - $120K':0, 'Income_Category_Less than $40K':0, 'Income_Category_Unknown':0}
    if Income_Category == '$120K +':
        Income_Category_list['Income_Category_$120K +']=1 
    elif Income_Category == '$40K - $60K': 
        Income_Category_list['Income_Category_$40K - $60K']=1
    elif Income_Category == '$60K - $80K': 
        Income_Category_list['Income_Category_$60K - $80K']=1
    elif Income_Category == '$80K - $120K': 
        Income_Category_list['Income_Category_$80K - $120K']=1
    elif Income_Category == 'Less than $40K': 
        Income_Category_list['Income_Category_Less than $40K']=1
    elif Income_Category == 'Unknown': 
        Income_Category_list['Income_Category_Unknown']=1
    else : raise ValueError("Error: Wrong input")
    return(Income_Category_list)

def encoding_Card_Category(Card_Category):
    """Function to encode Card_Category"""
    Card_Category_list={'Card_Category_Blue':0, 'Card_Category_Gold':0, 'Card_Category_Platinum':0, 'Card_Category_Silver':0}
    if Card_Category == 'Blue':
        Card_Category_list['Card_Category_Blue']=1 
    elif Card_Category == 'Gold': 
        Card_Category_list['Card_Category_Gold']=1
    elif Card_Category == 'Platinum': 
        Card_Category_list['Card_Category_Platinum']=1
    elif Card_Category == 'Silver': 
        Card_Category_list['Card_Category_Silver']=1
    else : raise ValueError("Error: Wrong input")
    return(Card_Category_list)

def onehotencoding_binding(Gender,Education_Level,Marital_Status,Income_Category,
       Card_Category):
    """Function to bind them altogether"""
    Gender_list=encoding_Gender(Gender)
    Education_list=encoding_Education_Level(Education_Level)
    Marital_Status_list=encoding_Marital_Status(Marital_Status)
    Income_Category_list=encoding_Income_Category(Income_Category)
    Card_Category_list=encoding_Card_Category(Card_Category)
    one_hot_encoding_binding={**Gender_list,**Education_list,**Marital_Status_list,
    **Income_Category_list,**Card_Category_list}
    return(one_hot_encoding_binding)
