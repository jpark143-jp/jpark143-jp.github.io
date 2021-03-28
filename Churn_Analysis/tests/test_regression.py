"""Module for unit, regression testing of 'onehotencode_bind'
   functions.
"""

import pytest
from final_modules.encode_pred import encoding_Gender, encoding_Education_Level, encoding_Marital_Status, encoding_Income_Category,\
                                                     encoding_Card_Category

def test_onehotencoding_binding_Gender_throws_error():
    """Unit test to showcase edge case behavior of throwing an error when
       Gender input is wrong.
    """
    with pytest.raises(ValueError):
        encoding_Gender('X')

def test_onehotencoding_binding_Education_Level_throws_error():
    """Unit test to showcase edge case behavior of throwing an error when
       Education_Level input is wrong.
    """
    with pytest.raises(ValueError):
        encoding_Education_Level('X')

def test_onehotencoding_binding_Marital_Status_throws_error():
    """Unit test to showcase edge case behavior of throwing an error when
       Marital_Status input is wrong.
    """
    with pytest.raises(ValueError):
        encoding_Marital_Status('X')

def test_onehotencoding_binding_Income_Category_throws_error():
    """Unit test to showcase edge case behavior of throwing an error when
       Income_Category input is wrong.
    """
    with pytest.raises(ValueError):
        encoding_Income_Category('X')

def test_onehotencoding_binding_Card_Category_throws_error():
    """Unit test to showcase edge case behavior of throwing an error when
       Card_Category input is wrong.
    """
    with pytest.raises(ValueError):
        encoding_Card_Category('X')
