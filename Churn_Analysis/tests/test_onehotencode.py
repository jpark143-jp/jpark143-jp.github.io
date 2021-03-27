"""Module for unit, regression and paramterized testing of 'adjust_price'
   functions.
"""

import pytest
from final_modules.encode_pred import encoding_Gender, encoding_Education_Level, encoding_Marital_Status, encoding_Income_Category,\
                                                     encoding_Card_Category

def test_onehotencoding_Gender():
    """Unit test to showcase functionality of one-hot-encoding Gender."""
    expected_output={'Gender_F': 0, 'Gender_M': 1}
    output = encoding_Gender('M')
    assert expected_output == output, \
        """Should show that Gender encoded."""

def test_onehotencoding_Education_Level():
    """Unit test to showcase functionality of one-hot-encoding Education_Level."""
    expected_output={'Education_Level_College': 1,
 'Education_Level_Doctorate': 0,
 'Education_Level_Graduate': 0,
 'Education_Level_High School': 0,
 'Education_Level_Post-Graduate': 0,
 'Education_Level_Uneducated': 0,
 'Education_Level_Unknown': 0}
    output = encoding_Education_Level('College')
    assert expected_output == output, \
        """Should show that the Education_Level encoded."""

def test_onehotencoding_Marital_Status():
    """Unit test to showcase functionality of one-hot-encoding Marital_Status."""
    expected_output={'Marital_Status_Divorced': 1, 'Marital_Status_Married': 0, 'Marital_Status_Single': 0, 'Marital_Status_Unknown': 0}
    output = encoding_Marital_Status('Divorced')
    assert expected_output == output, \
        """Should show that Marital_Status encoded."""

def test_onehotencoding_Income_Category():
    """Unit test to showcase functionality of one-hot-encoding Income_Category."""
    expected_output={'Income_Category_$120K +': 1,
 'Income_Category_$40K - $60K': 0,
 'Income_Category_$60K - $80K': 0,
 'Income_Category_$80K - $120K': 0,
 'Income_Category_Less than $40K': 0,
 'Income_Category_Unknown': 0}
    output = encoding_Income_Category('$120K +')
    assert expected_output == output, \
        """Should show that Income_Category is encoded."""

def test_onehotencoding_Card_Category():
    """Unit test to showcase functionality of one-hot-encoding Card_Category."""
    expected_output={'Card_Category_Blue': 1, 'Card_Category_Gold': 0, 'Card_Category_Platinum': 0, 'Card_Category_Silver': 0}
    output = encoding_Card_Category('Blue')
    assert expected_output == output, \
        """Should show that Card_Category is encoded."""




