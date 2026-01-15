import pytest
 
from canadata_clean import clean_phonenumber

def test_clean_phonenumber():
    """
    Test that clean_phonenumber works as expected.
    
    """
    string = "123-456-7890"
    expected = "+1 (123) 456-7890"
    actual = clean_phonenumber(string)
    assert  actual == expected, f"Expected {expected} but got {actual}"

    string = "123 456 7890"
    expected = "+1 (123) 456-7890"
    actual = clean_phonenumber(string)
    assert  actual == expected, f"Expected {expected} but got {actual}"

    string = "1234567890"
    expected = "+1 (123) 456-7890"
    actual = clean_phonenumber(string)
    assert  actual == expected, f"Expected {expected} but got {actual}"

    string = "(123)4567890"
    expected = "+1 (123) 456-7890"
    actual = clean_phonenumber(string)
    assert  actual == expected, f"Expected {expected} but got {actual}"

    string = 1234567890
    expected = "+1 (123) 456-7890"
    actual = clean_phonenumber(string)
    assert  actual == expected, f"Expected {expected} but got {actual}"

def test_clean_phonenumber_wrong_input():
    with pytest.raises(ValueError):
        clean_phonenumber("123456")
