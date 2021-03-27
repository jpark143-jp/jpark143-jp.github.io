"""Module for integration testing of 'onehotencode_bind'
   functions.
"""

import pytest
from final_modules.encode_pred import encoding_Gender, encoding_Education_Level, encoding_Marital_Status, encoding_Income_Category,\
                                                     encoding_Card_Category


def test_onehotencoding_binding_integration():
    """Integration test to check that we can get the final list of inputs
       after one-hot-encoding and bind them altogether.
    """
    expected_output ={'Gender_M': 1,
 'Gender_F': 0,
 'Education_Level_College': 1,
 'Education_Level_Doctorate': 0,
 'Education_Level_Graduate': 0,
 'Education_Level_High School': 0,
 'Education_Level_Post-Graduate': 0,
 'Education_Level_Uneducated': 0,
 'Education_Level_Unknown': 0,
 'Marital_Status_Divorced': 1,
 'Marital_Status_Married': 0,
 'Marital_Status_Single': 0,
 'Marital_Status_Unknown': 0,
 'Income_Category_$120K +': 1,
 'Income_Category_$40K - $60K': 0,
 'Income_Category_$60K - $80K': 0,
 'Income_Category_$80K - $120K': 0,
 'Income_Category_Less than $40K': 0,
 'Income_Category_Unknown':0,
 'Card_Category_Blue': 1,
 'Card_Category_Gold': 0,
 'Card_Category_Platinum': 0,
 'Card_Category_Silver': 0}
    output_after_Gender = encoding_Gender('M')
    output_after_Education_Level = {**output_after_Gender, **encoding_Education_Level('College')}
    output_after_Marital_Status = {**output_after_Education_Level, **encoding_Marital_Status('Divorced')}
    output_after_Income_Category = {**output_after_Marital_Status, **encoding_Income_Category('$120K +')}
    output_after_Card_Category = {**output_after_Income_Category, **encoding_Card_Category('Blue')}
    assert expected_output == output_after_Card_Category, \
        """Should show that the output is all encoded and binded altogether"""