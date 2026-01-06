def clean_birthday(text: str) -> str:
    """
    Clean and validate a birthday string, converting common formats to the Canadian standard YYYY-MM-DD (ISO 8601).

    The function accepts birthday strings in the following formats:
    - YYYY-MM-DD (primary target format)
    - DD/MM/YYYY (common in many countries, including parts of Europe)
    - DD-MM-YYYY

    It performs the following steps:
    1. Strips leading/trailing whitespace.
    2. Attempts to parse the input using the supported formats.
    3. If parsing succeeds, reformats the date to YYYY-MM-DD.
    4. Validates that the resulting date is not in the future (i.e., on or before today's date).
    5. Validates that the date is plausible (e.g., year reasonable for a living person, typically 1900 or later).

    Parameters
    ----------
    text : str
        The input string representing a birthday in one of the supported formats.

    Returns
    -------
    str
        The validated birthday in strict YYYY-MM-DD format.

    Raises
    ------
    ValueError
        If the input cannot be parsed as a valid date in any supported format,
        if the resulting date is in the future,
        or if the date is otherwise invalid (e.g., February 30).

    Examples
    --------
    >>> clean_birthday("1990-05-15")
    '1990-05-15'
    >>> clean_birthday("15/05/1990")
    '1990-05-15'
    >>> clean_birthday("15-05-1990")
    '1990-05-15'
    >>> clean_birthday("  15 / 05 / 1990  ")
    '1990-05-15'
    >>> clean_birthday("2030-01-01")  # Future date
    # Raises ValueError: Birthday cannot be in the future
    >>> clean_birthday("invalid")
    # Raises ValueError: Unable to parse date
    """