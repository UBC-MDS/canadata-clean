import pytest
 
from canadata_clean import clean_phonenumber

def test_clean_phonenumber():
    """
    Test whether clean_phonenumber works with valid and invalid inputs. 
    
    Ensures that valid inputs are converted to the standard Canadian format "+1 (XXX) XXX-XXXX"
    and raises errors for invalid inputs such as empty strings, incorrect digit lengths, 
    non-numeric characters, and non-string inputs. 
    
    """
    #Valid Input
    string = "((123))-456.7890"
    expected = "+1 (123) 456-7890"
    actual = clean_phonenumber(string)
    assert  actual == expected, f"Expected {expected} but got {actual}"

    string = " 123 456 7890 "
    expected = "+1 (123) 456-7890"
    actual = clean_phonenumber(string)
    assert  actual == expected, f"Expected {expected} but got {actual}"

    string = "1234567890"
    expected = "+1 (123) 456-7890"
    actual = clean_phonenumber(string)
    assert  actual == expected, f"Expected {expected} but got {actual}"

    #Invalid Input
    with pytest.raises(ValueError):
        clean_phonenumber("123457")
    with pytest.raises(TypeError):
        clean_phonenumber(1234567890)
    with pytest.raises(ValueError):
        clean_phonenumber("")
    with pytest.raises(ValueError):
        clean_phonenumber("123abc4567")