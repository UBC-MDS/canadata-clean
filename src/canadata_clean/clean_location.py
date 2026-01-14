from thefuzz import fuzz

"""
names_and_abbreviations adapted from the following sources:
https://en.wikipedia.org/wiki/Canadian_postal_abbreviations_for_provinces_and_territories
https://www.noslangues-ourlanguages.gc.ca/en/writing-tips-plus/abbreviations-canadian-provinces-and-territories
"""
names_and_abbreviations = {
    "AB": ["ab", "alberta", "alta.", "alb."],
    "BC": ["bc", "british columbia", "c.-b."],
    "MB": ["mb", "manitoba", "man."],
    "NB": ["nb", "new brunswick", "n.-b."],
    "NL": ["nl", "newfoundland and labrador", "nfld.", "lab.", "t.-n.-l.", "newfoundland", "labrador", "nfld. lab."],
    "NT": ["nt", "northwest Ttrritories", "northwest territory", "north west territories", "north west territory", "nw territories", "nw territory", "n.w.t", "t.n.-o.", "nw"],
    "NS": ["ns", "nova scotia", "n.-e"],
    "NU": ["nu", "nunavut", "nvt.", "nt"],
    "ON": ["on", "ontario", "ont."],
    "PE": ["pe", "prince edward island", "prince edward", "p.e.i", "i.-p.-e."],
    "QC": ["qc", "quebec", "que.", "pq"],
    "SK": ["sk", "saskatchewan", "sask."],
    "YT": ["yt", "yukon", "yuk.", "yn", "yk"]
}

def clean_location(text: str):
    """
    Identify a free-text entry representing a province or territory in Canada using fuzzy matching and return the two letter unique identifier.
    
    The function accepts a province or territory in a variety of English formats, including full spelling, common abbreviations, and minor misspellings. It performs fuzzy matching between the input string and a dictionary of province and territory names, acronyms, and shorthands. If a province or territory cannot be identified, the function will raise an error. 

    This program can only process English text entries, containing the 26 characters of the English alphabet. It may not process French characters, including accents, and may not match French province/territory names correctly.

    Parameters
    ----------
    text : str
        The input string representing a province/territory in Canada.

    Returns
    -------
    str
        The cleaned and validated province/territory.

    Raises
    ------
    ValueError
        If a valid Canadian province/territory cannot be identified from the input.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> clean_location("British Columbia")
    'BC'
    >>> clean_location("B.C.")
    'BC'
    >>> clean_location("Not A Province")
    # Raises ValueError: Province or territory could not be identified.
    >>> clean_location(1)
    # Raises TypeError: Input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected input to be str, got {type(text)}")
    
    text = " ".join(text.split()).lower()

    if not text:
        raise ValueError("Text cannot be empty.")
    
    return identify_province_territory(text)

def remove_periods(text: str) -> str:
    return text.replace(".", "")

def remove_spaces(text: str) -> str:
    return text.replace(" ", "")

def normalize_names(names: dict, function) -> dict:
    """
    Apply a string transform to every abbreviation in the dictionary.
    """
    return {
        key: [function(v) for v in values]
        for key, values in names.items()
    }

def try_variation(text:str, function, threshold: int):
    text = remove_periods(text)
    names = normalize_names(names_and_abbreviations, function)
    predictions = score_predictions(text, names)
    max_key, max_value = get_max(predictions)

    if isinstance(max_key, str) and max_value > threshold:
        return max_key
    else:
        return "No Match"

def try_variations(text:str , threshold: int):
    result = try_variation(text, remove_periods, threshold)
    if result != "No Match":
        return result
    
    result = try_variation(text, remove_spaces, threshold)
    if result != "No Match":
        return result

    predictions_partial = score_predictions(text, names_and_abbreviations, scorer = fuzz.partial_ratio)
    max_key, max_value = get_max(predictions_partial)

    # use a higher threshold for partial matches
    if isinstance(max_key, str) and max_value > (threshold + ((100 - threshold) / 2)):
        return max_key

    raise ValueError(f"No unique province/territory identified for '{text}'.")

def get_max(predictions: dict):
    max_value = max(predictions.values())
    max_keys = [k for k, v in predictions.items() if v == max_value]

    if len(max_keys) > 1:
        return max_keys, max_value
    else:
        return max_keys[0], max_value

def identify_province_territory(text: str, threshold: int = 90):

    predictions = score_predictions(text, names_and_abbreviations)
    
    max_value = max(predictions.values())
    max_keys = [k for k, v in predictions.items() if v == max_value]

    if max_value < 80:
        return try_variations(text, threshold)
    else:
        if len(max_keys) == 1:
            return max_keys[0]
        else:
            return try_variations(text, threshold)

def score_predictions(text: str, names: dict, scorer = fuzz.ratio):
    predictions = {}

    for key, values in names.items():
        best = 0
        for item in values:
            ratio = scorer(text, item)
            if ratio > best:
                best = ratio
        predictions[key] = best

    return predictions