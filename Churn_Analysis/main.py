""" Module serve as Feature engineering + Random Forest(Final Model)
    prepared for the streaming input;
    - Sample usage : python main.py 54 1 40 2 3 1 1438.3 808 630.3 0.997 705 19 0.9 0.562 F Graduate Married 'Less than $40K' Blue
    - important notes for input spec is on README.md
    Author : JungHwan Park
    Date : 03.05.2021
    Email : jpark143@g.ucla.edu
    Content : Final model prediction
"""

import urllib.request
import sys

import numpy as np
import joblib

from final_modules.encode_pred import onehotencoding_binding

if __name__ == "__main__":

    CUSTOMER_AGE = float(sys.argv[1])
    DEPENDENT_COUNT = float(sys.argv[2])
    MONTHS_ON_BOOK = float(sys.argv[3])
    TOTAL_RELATIONSHIP_COUNT = float(sys.argv[4])
    MONTHS_INACTIVE_12_MON = float(sys.argv[5])
    CONTACTS_COUNT_12_MON = float(sys.argv[6])
    CREDIT_LIMIT = float(sys.argv[7])
    TOTAL_REVOLVING_BAL = float(sys.argv[8])
    AVG_OPEN_TO_BUY = float(sys.argv[9])
    TOTAL_AMT_CHNG_Q4_Q1 = float(sys.argv[10])
    TOTAL_TRANS_AMT = float(sys.argv[11])
    TOTAL_TRANS_CT = float(sys.argv[12])
    TOTAL_CT_CHNG_Q4_Q1 = float(sys.argv[13])
    AVG_UTILIZATION_RATIO = float(sys.argv[14])
    GENDER = sys.argv[15]
    EDUCATION_LEVEL = sys.argv[16]
    MARITAL_STATUS = sys.argv[17]
    INCOME_CATEGORY = sys.argv[18]
    CARD_CATEGORY = sys.argv[19]

    #
    # --- Print them out, for validation:
    print(f"CUSTOMER_AGE: {CUSTOMER_AGE}")
    print(f"DEPENDENT_COUNT: {DEPENDENT_COUNT}")
    print(f"MONTHS_ON_BOOK: {MONTHS_ON_BOOK}")
    print(f"TOTAL_RELATIONSHIP_COUNT: {TOTAL_RELATIONSHIP_COUNT}")
    print(f"MONTHS_INACTIVE_12_MON: {MONTHS_INACTIVE_12_MON}")
    print(f"CONTACTS_COUNT_12_MON: {CONTACTS_COUNT_12_MON}")
    print(f"CREDIT_LIMIT: {CREDIT_LIMIT}")
    print(f"TOTAL_REVOLVING_BAL: {TOTAL_REVOLVING_BAL}")
    print(f"AVG_OPEN_TO_BUY: {AVG_OPEN_TO_BUY}")
    print(f"TOTAL_AMT_CHNG_Q4_Q1: {TOTAL_AMT_CHNG_Q4_Q1}")
    print(f"TOTAL_TRANS_AMT: {TOTAL_TRANS_AMT}")
    print(f"TOTAL_TRANS_CT: {TOTAL_TRANS_CT}")
    print(f"TOTAL_CT_CHNG_Q4_Q1: {TOTAL_CT_CHNG_Q4_Q1}")
    print(f"AVG_UTILIZATION_RATIO: {AVG_UTILIZATION_RATIO}")
    print(f"GENDER: {GENDER}")
    print(f"EDUCATION_LEVEL: {EDUCATION_LEVEL}")
    print(f"MARITAL_STATUS: {MARITAL_STATUS}")
    print(f"INCOME_CATEGORY: {INCOME_CATEGORY}")
    print(f"CARD_CATEGORY: {CARD_CATEGORY}")
    #
    # --- Create final variables for validation:
    ONEHOTENCODING_LIST = onehotencoding_binding(GENDER, EDUCATION_LEVEL, MARITAL_STATUS,
                                                 INCOME_CATEGORY, CARD_CATEGORY)
    ALLBINDED_LIST = {'Customer_Age':CUSTOMER_AGE,
                      'Dependent_count':DEPENDENT_COUNT,
                      'Months_on_book':MONTHS_ON_BOOK,
                      'Total_Relationship_Count':TOTAL_RELATIONSHIP_COUNT,
                      'Months_Inactive_12_mon':MONTHS_INACTIVE_12_MON,
                      'Contacts_Count_12_mon':CONTACTS_COUNT_12_MON,
                      'Credit_Limit':CREDIT_LIMIT,
                      'Total_Revolving_Bal':TOTAL_REVOLVING_BAL,
                      'Avg_Open_To_Buy':AVG_OPEN_TO_BUY,
                      'Total_Amt_Chng_Q4_Q1':TOTAL_AMT_CHNG_Q4_Q1,
                      'Total_Trans_Amt':TOTAL_TRANS_AMT,
                      'Total_Trans_Ct':TOTAL_TRANS_CT,
                      'Total_Ct_Chng_Q4_Q1':TOTAL_CT_CHNG_Q4_Q1,
                      'Avg_Utilization_Ratio':AVG_UTILIZATION_RATIO,
                      **ONEHOTENCODING_LIST}
    FINAL_LIST = list(ALLBINDED_LIST.values())
    MODEL_INPUT = np.reshape(FINAL_LIST, (1, -1))

    URL = "https://stats404-junghwanpark.s3.ap-northeast-2.amazonaws.com/rf_Bankchurners.joblib"
    FILENAME = "rf_Bankchurners.joblib"
    # Save the file
    with open(FILENAME, 'wb') as file:
        joblib.dump(URL, file)

    urllib.request.urlretrieve(URL, FILENAME)
    # Load from file
    with open(FILENAME, 'rb') as file:
        MODEL = joblib.load(file)

    FINAL_PRED = MODEL.predict(MODEL_INPUT)
    print(f"Final_predicted_outcome : {FINAL_PRED}")
