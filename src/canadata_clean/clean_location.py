from thefuzz import fuzz
import string

"""
The data for names_and_abbreviations was adapted from the following sources:
https://en.wikipedia.org/wiki/Canadian_postal_abbreviations_for_provinces_and_territories
https://www.noslangues-ourlanguages.gc.ca/en/writing-tips-plus/abbreviations-canadian-provinces-and-territories
"""
names_and_abbreviations = {
    "AB": ["ab", "alberta", "alta.", "alb."],
    "BC": ["bc", "british columbia", "c.-b."],
    "MB": ["mb", "manitoba", "man."],
    "NB": ["nb", "new brunswick", "n.-b."],
    "NL": ["nl", "newfoundland and labrador", "nfld.", "lab.", "t.-n.-l.", "newfoundland", "labrador", "nfld. lab."],
    "NT": ["nt", "northwest territories", "northwest territory", "north west territories", "north west territory", "nw territories", "nw territory", "n.w.t", "t.n.-o.", "nw"],
    "NS": ["ns", "nova scotia", "n.-e"],
    "NU": ["nu", "nunavut", "nvt."],
    "ON": ["on", "ontario", "ont."],
    "PE": ["pe", "prince edward island", "prince edward", "p.e.i", "i.-p.-e."],
    "QC": ["qc", "quebec", "que.", "pq"],
    "SK": ["sk", "saskatchewan", "sask."],
    "YT": ["yt", "yukon", "yuk.", "yn", "yk"]
}

def clean_location(text: str, threshold = 85):
    """
    Identify a free-text entry representing a province or territory in Canada using fuzzy matching and return the two letter unique identifier.
    
    The function accepts a province or territory in a variety of English formats, including full spelling, common abbreviations, and minor misspellings. It performs fuzzy matching between the input string and a dictionary of province and territory names, acronyms, and shorthands. If a province or territory cannot be identified, the function will raise an error. 

    This program can only process English text entries, containing the 26 characters of the English alphabet. It may not process French characters, including accents, and may not match French province/territory names correctly.

    Parameters
    ----------
    text : str
        The input string representing a province/territory in Canada.
    threshold : int
        The baseline cutoff threshold for accepting a fuzzy match, up to 100 (perfect match). Default is 85.

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
    
    predictions = score_predictions(text, names_and_abbreviations)
    
    max_key, max_value = get_max(predictions)

    if isinstance(max_key, str) and max_value > threshold:
        return max_key
    else:
        return try_variations(text, threshold)

def remove_punctuation(text: str) -> str:
    """
    Remove all ASCII punctuation characters from a string.

    This function strips characters defined in ``string.punctuation`` while
    preserving letters, numbers, and whitespace. It is used as a normalization
    step prior to fuzzy matching, in the event that significant punctuation prevented
    a match in the first round of matching.

    Parameters
    ----------
    text : str
        Input string to normalize.

    Returns
    -------
    str
        The input string with all punctuation removed.

    Examples
    --------
    >>> remove_punctuation("P.E.I.")
    'PEI'
    """
    return text.translate(str.maketrans("", "", string.punctuation))

def remove_spaces(text: str) -> str:
    """
    Remove all space characters from a string.

    This function is used to handle inputs where province or territory names
    may be concatenated without spaces and previous fuzzy matching attempts
    have not found a match.

    Parameters
    ----------
    text : str
        Input string to normalize.

    Returns
    -------
    str
        The input string with all spaces removed.

    Examples
    --------
    >>> remove_spaces("newfoundland and labrador")
    'newfoundlandandlabrador'
    """

    return text.replace(" ", "")

def normalize_names(names: dict, function) -> dict:
    """
    Apply a string normalization function to all values in a mapping.

    This helper applies a transformation (e.g., removing punctuation or spaces)
    to every abbreviation or name associated with each province or territory in
    the names_and_abbreviations dictionary.

    Parameters
    ----------
    names : dict
        Dictionary mapping province/territory codes to lists of name variants.
    function : callable
        A function that takes a string and returns a transformed string.

    Returns
    -------
    dict
        A new dictionary with the same keys as ``names`` and transformed values.

    Examples
    --------
    >>> normalize_names({"ON": ["ont.", "ontario"]}, remove_punctuation)
    {'ON': ['ont', 'ontario']}
    """
    return {
        key: [function(v) for v in values]
        for key, values in names.items()
    }

def try_variation(text:str, function, threshold: int):
    """
    Attempt to identify a province or territory using a specific normalization strategy.

    This applies the specified function to both the input text and the names dictionary, then scores fuzzy matches against the dictionary.

    Parameters
    ----------
    text : str
        Input string.
    function : callable
        A normalization function applied to the input string and the names
        dictionary.
    threshold : int
        Minimum fuzzy match score required to accept a result.

    Returns
    -------
    str
        The identified province/territory code if a confident match is found,
        otherwise the string "No Match".
    """
    text = function(text)
    names = normalize_names(names_and_abbreviations, function)
    predictions = score_predictions(text, names)
    max_key, max_value = get_max(predictions)

    if isinstance(max_key, str) and max_value > threshold:
        return max_key
    else:
        return "No Match"

def try_variations(text:str , threshold: int):
    """
    Attempt multiple normalization and fuzzy-matching strategies in sequence.

    This function tries increasingly permissive matching approaches, including
    punctuation removal, space removal, and partial fuzzy matching. It raises
    an error if no unique province or territory can be identified after all three
    matching strategies.

    Parameters
    ----------
    text : str
        Normalized input string.
    threshold : int
        Base fuzzy matching threshold.

    Returns
    -------
    str
        The identified province/territory code.

    Raises
    ------
    ValueError
        If no unique province or territory can be identified.
    """
    result = try_variation(text, remove_punctuation, threshold)
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
    """
    Identify the key(s) associated with the maximum value in a dictionary.

    Parameters
    ----------
    predictions : dict
        Dictionary mapping keys to numeric scores.

    Returns
    -------
    tuple
        If a unique maximum exists, returns (key, value).
        If multiple keys share the maximum value, returns (list_of_keys, value).
    """
    max_value = max(predictions.values())
    max_keys = [k for k, v in predictions.items() if v == max_value]

    if len(max_keys) > 1:
        return max_keys, max_value
    else:
        return max_keys[0], max_value

def score_predictions(text: str, names: dict, scorer = fuzz.ratio):
    """
    Compute fuzzy matching scores between an input string and reference dictionary.

    For each province or territory, the highest fuzzy match score across all
    associated name variants is retained.

    Parameters
    ----------
    text : str
        Input string to match.
    names : dict
        Dictionary mapping province/territory codes to lists of name variants.
    scorer : callable, optional
        Fuzzy matching function from ``thefuzz`` (default is ``fuzz.ratio``).

    Returns
    -------
    dict
        Dictionary mapping province/territory codes to their best match score.
    """
    predictions = {}

    for key, values in names.items():
        best = 0
        for item in values:
            ratio = scorer(text, item)
            if ratio > best:
                best = ratio
        predictions[key] = best

    return predictions