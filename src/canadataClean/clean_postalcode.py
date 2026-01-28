def clean_postalcode(postal_code: str, region: str = None) -> str:
    """
    Clean and validate a free-text entry representing a Canadian postal code and convert it to the standard Canadian postal code format "A1A 1A1".

    The function accepts postal codes in a variety of formats, including with or without spaces, dashes, or lowercase letters. It first removes extraneous characters and normalizes the string to uppercase. If a `region` is provided, the function checks that the postal code matches the expected prefix for that province or territory. The postal code is then reformatted to the standard "A1A 1A1" format. If the postal code is invalid or does not match the specified region, a ValueError is raised.
    
    Postal code address guidelines reference: https://www.canadapost-postescanada.ca/cpc/en/support/articles/addressing-guidelines/postal-codes.page

    Parameters
    ----------
    postal_code : str
        The input string representing a Canadian postal code.
    region : str, optional
        The Canadian province or territory to validate the postal code against (default is None, which skips region-specific validation).

    Returns
    -------
    str
        The validated Canadian postal code in standard "A1A 1A1" format.

    Raises
    ------
    ValueError
        If the input does not match a valid Canadian postal code pattern,
        or if it does not match the specified region's postal code prefix.

    Examples
    --------
    >>> clean_postalcode("K1A0B1")
    'K1A 0B1'
    >>> clean_postalcode("k1a 0b1", region="ON")
    'K1A 0B1'
    >>> clean_postalcode("V5K0A1", region="ON")
    # Raises ValueError: Postal code does not match the specified region
    >>> clean_postalcode("12345")
    # Raises ValueError: Invalid Canadian postal code
    """
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

    # If postal code is not a string, raise TypeError
    if not isinstance(postal_code, str):
        raise TypeError(f"Expected a string but got {type(postal_code)}")
    
    # joining only alphanumeric characters and converting to uppercase
    postal_code_raw = ''.join(filter(str.isalnum, postal_code)).upper()  
    valid_geographic_prefix = ["A", "B", "C", "E", "G", "H", "J", "K", "L", "M", "N", "P", "R", "S", "T", "V", "X", "Y"]
  
    # if the length of the raw postal code is not 6 characters, raise ValueError
    if len(postal_code_raw) != 6:
        raise ValueError(f"Postal code must be 6 alphanumeric characters long. Got: {len(postal_code_raw)} characters.")
    # if the first character is not in the valid geographic prefix list, raise ValueError
    if (postal_code_raw[0] not in valid_geographic_prefix):
        raise ValueError(f"Invalid Canadian postal code prefix: {postal_code_raw[0]}")
    # check the A1A1A1 format, raise ValueError if it does not match
    if not (postal_code_raw[0].isalpha() and postal_code_raw[1].isdigit() and postal_code_raw[2].isalpha() and
            postal_code_raw[3].isdigit() and postal_code_raw[4].isalpha() and postal_code_raw[5].isdigit()):
        raise ValueError(f"Invalid Canadian postal code format: '{postal_code_raw}'. Expected format is 'A1A1A1'.")
    return f"{postal_code_raw[:3]} {postal_code_raw[3:]}"