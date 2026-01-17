import re
from datetime import date,datetime

def clean_date(text: str, min_year: int = 1900, allow_future: bool = False) -> str:
    """
    Clean and validate a date string, converting common formats to the Canadian standard YYYY-MM-DD (ISO 8601).

    The function accepts date strings in the following formats: 
    - YYYY-MM-DD (primary target format, ISO 8601)
    - DD/MM/YYYY (common in countries influenced by British standards)
    - DD-MM-YYYY (alternative separator)
    - D/M/YYYY, DD/M/YYYY, D/MM/YYYY (single-digit days/months with forward slash)
    - D-M-YYYY, DD-M-YYYY, D-MM-YYYY (single-digit days/months with hyphen)

    Note: This function intentionally does NOT support MM/DD/YYYY (US format) to avoid 
    ambiguity.  Dates like "01/02/1990" are interpreted as DD/MM/YYYY (1 February 1990), 
    not MM/DD/YYYY (2 January 1990).

    It performs the following steps:
    1. Strips leading/trailing whitespace and normalizes internal spaces around separators.
    2. Attempts to parse the input using the supported formats in order.
    3. If parsing succeeds, reformats the date to YYYY-MM-DD. 
    4. Validates that the resulting date is logically valid (e.g., no February 30, correct leap years).
    5. Validates that the year is within the acceptable range (min_year to current year).
    6. Validates that the date is not in the future (unless allow_future=True).

    Parameters
    ----------
    text : str
        The input string representing a date in one of the supported formats.
        Leading/trailing whitespace is permitted and will be stripped.
        Spaces around separators (e.g., "15 / 05 / 1990") are normalized. 
    min_year : int, optional
        The minimum acceptable year (default: 1900). Dates with years below this value
        will raise a ValueError.  Adjust this for historical data or specific use cases.
    allow_future : bool, optional
        If False (default), dates in the future will raise a ValueError.
        If True, future dates are accepted. 

    Returns
    -------
    str
        The validated date in strict YYYY-MM-DD format.

    Raises
    ------
    ValueError
        If the input is None, empty, or contains only whitespace: 
            "Date string cannot be empty or None"
        
        If the input cannot be parsed as a valid date in any supported format: 
            "Unable to parse date:  '{text}'.  Expected formats:  YYYY-MM-DD, DD/MM/YYYY, or DD-MM-YYYY"
        
        If the parsed date is logically invalid (e.g., February 30, invalid leap year):
            "Invalid date:  {details} (e.g., 'February 30 does not exist')"
        
        If the year is below min_year:
            "Date year {year} is below minimum allowed year {min_year}"
        
        If the resulting date is in the future and allow_future=False:
            "Date cannot be in the future:  {date} is after {today}"

    Examples
    --------
    Basic usage: 
    >>> clean_date("1990-05-15")
    '1990-05-15'
    
    >>> clean_date("15/05/1990")
    '1990-05-15'
    
    >>> clean_date("15-05-1990")
    '1990-05-15'
    
    Single-digit days/months:
    >>> clean_date("5/8/1990")
    '1990-08-05'
    
    >>> clean_date("5-8-1990")
    '1990-08-05'
    
    With whitespace:
    >>> clean_date("  15 / 05 / 1990  ")
    '1990-05-15'
    
    Leap year validation:
    >>> clean_date("29/02/2020")  # Valid leap year
    '2020-02-29'
    
    >>> clean_date("29/02/2021")  # Invalid leap year
    # Raises ValueError: Invalid date: day is out of range for month
    
    Future date validation:
    >>> clean_date("2030-01-01")  # Future date (assuming today is before 2030)
    # Raises ValueError: Date cannot be in the future:  2030-01-01 is after 2026-01-12
    
    >>> clean_date("2030-01-01", allow_future=True)  # Allow future dates
    '2030-01-01'
    
    Invalid dates:
    >>> clean_date("30/02/1990")  # February 30 doesn't exist
    # Raises ValueError: Invalid date: day is out of range for month
    
    >>> clean_date("1850-05-15")  # Below minimum year
    # Raises ValueError: Date year 1850 is below minimum allowed year 1900
    
    >>> clean_date("1850-05-15", min_year=1800)  # Custom minimum year
    '1850-05-15'
    
    >>> clean_date("")  # Empty string
    # Raises ValueError: Date string cannot be empty or None
    
    >>> clean_date("not a date")  # Unparseable
    # Raises ValueError: Unable to parse date: 'not a date'.  Expected formats: YYYY-MM-DD, DD/MM/YYYY, or DD-MM-YYYY
    """
    
    if text is None or not isinstance(text, str) or not text.strip():
        raise ValueError("Date string cannot be empty or None")
    
    # Normalize whitespace: strip leading/trailing, and remove spaces around / or -
    text = text.strip()
    text = re.sub(r'\s*/\s*', '/', text)
    text = re.sub(r'\s*-\s*', '-', text)
    
    formats = [
        '%Y-%m-%d',    # 1990-05-15
        '%d/%m/%Y',    # 15/05/1990
        '%d-%m-%Y',    # 15-05-1990
    ]
    
    date_obj = None
    for fmt in formats:
        try:
            date_obj = datetime.strptime(text, fmt).date()
            break
        except ValueError:
            continue
    if date_obj is None:
        raise ValueError(f"Unable to parse date: '{text}'. Expected formats: YYYY-MM-DD, DD/MM/YYYY, or DD-MM-YYYY")
    
    # Check year
    if date_obj.year < min_year:
        raise ValueError(f"Date year {date_obj.year} is below minimum allowed year {min_year}")
    
    # Check future
    today = date.today()
    if not allow_future and date_obj > today:
        raise ValueError(f"Date cannot be in the future: {date_obj} is after {today}")
    
    return date_obj.isoformat()
    

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         user_input = sys.argv[1]
#         print(clean_date(user_input))
#     else:
#         print("Please provide a date string as a command-line argument.")