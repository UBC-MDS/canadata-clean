"""
A test module that tests clean_postalcode module.

This test example provides a single test for the clean_postalcode.py module.
"""
from canadata_clean.clean_postalcode import clean_postalcode
import pytest

def test_clean_postalcode():
    """
    Canadian Postal Code Structure
    Format: A1A 1A1 (Letter-Number-Letter Space Number-Letter-Number).
    Characters: Uses 18 letters (excluding D, F, I, O, Q, U, W, Z in certain positions) and 10 numbers. 
    Forward Sortation Area (FSA) - First Three Characters (A1A) 
    First Letter: Denotes a province or major sector (e.g., 'M' for Toronto, 'G' for Eastern Quebec).
    Second Digit: Identifies if the area is urban (non-zero) or rural (zero).
    Third Letter: Specifies a more precise geographic district within the FSA (e.g., a city section, a specific rural area). 
    Local Delivery Unit (LDU) - Last Three Characters (1A1) 
    Identifies the smallest delivery point, like a city block, a few buildings, or a specific institution. 
    """
    # Valid postal codes
    assert clean_postalcode("K1A0B1") == "K1A 0B1"
    assert clean_postalcode(" K1A0B1 ") == "K1A 0B1"
    assert clean_postalcode("V5K-0A1") == "V5K 0A1"
    assert clean_postalcode("V1A/2B6") == "V1A 2B6"
    assert clean_postalcode("v1g2f4") == "V1G 2F4"
    assert len(clean_postalcode("K1A0B1")) == 7
    assert clean_postalcode("K1A0B1")[3] == " "

    # Invalid postal codes
    with pytest.raises(TypeError, match="Expected a string but got"):
        clean_postalcode(123457)

    with pytest.raises(ValueError, match="Invalid Canadian postal code prefix: Z"):
        clean_postalcode("Z5K0A1")

    with pytest.raises(ValueError, match="Postal code must be 6 alphanumeric characters long. Got: 4 characters."):
        clean_postalcode("Z5K 0")
    
    with pytest.raises(ValueError, match="Invalid Canadian postal code prefix: 1"):
        clean_postalcode("15K0A1")
    
    with pytest.raises(ValueError, match="Invalid Canadian postal code format: 'VKK0A1'. Expected format is 'A1A1A1'."):
        clean_postalcode("VKK0A1")

    with pytest.raises(ValueError, match="Invalid Canadian postal code format: 'V510A1'. Expected format is 'A1A1A1'."):
        clean_postalcode("V510A1")
    
    with pytest.raises(ValueError, match="Invalid Canadian postal code format: 'V5KAA1'. Expected format is 'A1A1A1'."):
        clean_postalcode("V5KAA1")

    with pytest.raises(ValueError, match="Invalid Canadian postal code format: 'V5K001'. Expected format is 'A1A1A1'."):
        clean_postalcode("V5K001")

    with pytest.raises(ValueError, match="Invalid Canadian postal code format: 'V5K0AA'. Expected format is 'A1A1A1'."):
        clean_postalcode("V5K0AA")