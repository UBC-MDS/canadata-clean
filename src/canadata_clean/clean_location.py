from thefuzz import fuzz

def clean_location(text: str) -> str:
    """
    Clean and validate a free-text entry representing a general location in Canada (municipality name and province or territory) entered in English and convert it to the format "MunicipalityName, TwoLetterProvinceOrTerritoryCode".
    
    The function accepts locations in a variety of formats, so long as the municipality name comes before the province/territory name in the string. First, it performs fuzzy matching (starting at the end of the string and moving backward) to identify the specified province or territory using a dictionary of province and territory names, including acronyms and shorthands. If a province or territory cannot be identified, the function will raise an error and require the user to add or modify the province or territory before proceeding. Once a province or territory has been identified, the string is sliced to remove the characters indicating the province or territory. The modified string is standardized to title case and appropriate white space, and compass directions are standardized using fuzzy matching to a dictionary. Note that there is no validation performed on the municipality name.

    This program can only process English provinces/territories and municipalities, containing the 26 characters of the English alphabet. It cannot process French characters, including accents, and may not match French province/territory names correctly.

    Parameters
    ----------
    text : str
        The input string representing a location, municipality and providence/territory, in Canada.

    Returns
    -------
    str
        The cleaned and validated location.

    Raises
    ------
    ValueError
        If a valid Canadian province/territory cannot be identified from the input.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> clean_location("North Van British Columbia")
    'North Vancouver, BC'
    >>> clean_location("Not A City BC")
    'Not A City, BC'
    >>> clean_location("Vancouver BX")
    # Raises ValueError: Province or territory could not be identified.
    >>> clean_location(1)
    # Raises TypeError: Input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected input to be str, got {type(text)}")
    
    if not text.strip():
        raise ValueError("Text cannot be empty.")

    return str()

def standardize():
    # strip spaces
    # title case
    return

def identify_compass_directions():
    """
    compass_directions adapted from the following source:
    https://www.canadapost-postescanada.ca/cpc/en/support/articles/addressing-guidelines/symbols-and-abbreviations.page
    """
    compass_directions = {
        "East": ["E"],
        "North": ["N"],
        "Northeast": ["NE", "Northeast", "North East"],
        "Northwest": ["NW", "North West"],
        "South": ["S"],
        "Southeast": ["SE", "South East"],
        "Southwest": ["SW", "South West"],
        "West": ["W"]
    }
    return

def identify_province_territory():
    """
    names_and_abbreviations adapted from the following sources:
    https://en.wikipedia.org/wiki/Canadian_postal_abbreviations_for_provinces_and_territories
    https://www.noslangues-ourlanguages.gc.ca/en/writing-tips-plus/abbreviations-canadian-provinces-and-territories
    """
    # check province/territory against list

    names_and_abbreviations = {
        "AB": ["Alberta", "Alta.", "Alb."],
        "BC": ["British Columbia", "C.-B."],
        "MB": ["Manitoba", "Man."],
        "NB": ["New Brunswick", "N.-B."],
        "NL": ["Newfoundland and Labrador", "Nfld.", "Lab.", "T.-N.-L."],
        "NT": ["Northwest Territories", "Northwest Territory", "North West Territories", "North West Territory", "NW Territories", "NW Territory", "N.W.T", "T.N.-O."],
        "NS": ["Nova Scotia", "N.-E"],
        "NU": ["Nunavut", "Nvt.", "Nt"],
        "ON": ["Ontario", "Ont."],
        "PE": ["Prince Edward Island", "Prince Edward", "P.E.I", "I.-P.-E."],
        "QC": ["Quebec", "Que.", "Qc", "PQ"],
        "SK": ["Saskatchewan", "Sask."],
        "YT": ["Yukon", "Yuk.", "Yn", "YK"]
    }

    # add check here: if province/territory identified but no characters remaining, then throw valueerror for missing municipality

    return