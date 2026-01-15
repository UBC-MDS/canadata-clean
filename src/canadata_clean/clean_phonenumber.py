def clean_phonenumber(text: str) -> str:
    """
    Clean and validate a free-text entry phone number and convert it to the standard Canadian format "+1 (XXX) XXX-XXXX".

    The function accepts phone number in a variety of formats, including with or without parentheses, spaces, dashes. 

    Parameters
    ----------
    text : str
        The input string representing a Canadian phone number.

    Returns
    -------
    text: str
        The validated Canadian phone number in standard "+1 (XXX) XXX-XXXX" format.
    
    Raises
    ------
    ValueError
        If the input does not contain exactly 10 digits.
    

    Examples
    --------
    >>> clean_phonenumber("123-456-7890")
    '+1 (123) 456-7890'
    >>> clean_phonenumber("1234567890")
    '+1 (123) 456-7890'
    >>> clean_phonenumber("(123) 456-7890")
    '+1 (123) 456-7890'
    >>> clean_phonenumber("123 456 7890")
    '+1 (123) 456-7890'
    >>> clean_phonenumber("123456")
    # Raises ValueError: Invalid phone number length
    """

    cleaned = ""

    if not isinstance(text, str):
        raise ValueError("Phone number must be provided as a string.")

    for t in text:
        if t.isdigit():
            cleaned += t

    if len(cleaned) != 10:
        raise ValueError ("Invalid phone number length: exactly 10 digits are required.")
    
    area = cleaned[0:3]
    extension = cleaned[3:6]
    line = cleaned[6:]
    output = f"+1 ({area}) {exchange}-{line}"
    
    return output