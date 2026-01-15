"""
A test module for the location cleaning function.
"""
import pytest
import re
from canadata_clean.clean_location import clean_location
from canadata_clean.clean_location import remove_punctuation
from canadata_clean.clean_location import remove_spaces
from canadata_clean.clean_location import normalize_names
from canadata_clean.clean_location import score_predictions
from canadata_clean.clean_location import get_max
from canadata_clean.clean_location import try_variation
from canadata_clean.clean_location import try_variations

def test_clean_location():
    """
    Run the following tests to test the clean_location function.
    """

    empty()
    output_type()
    incomplete_input()
    capitalization()
    spaces_sides()
    spaces_middle()
    format()
    unidentified_province_territory()
    province_territory_replacement()
    same_distance_raises_error()

def empty():
    """
    Test that the function never returns an empty string.
    """

    assert clean_location("BC"), "Output should not be empty."
 
def capitalization():
    """
    Test that the output is always capitalized.
    """

    out = clean_location("bc")
    expected_out = "BC"
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def spaces_sides():
    """
    Test that the output string starts and ends in a non-space character.
    """

    out = clean_location("  manitoba   ")
    assert not out.startswith(" "), "Output should not begin with a space."
    assert not out.endswith(" "), "Output should not end with a space."

def spaces_middle():
    """
    Test that the output string does not have more than one space between characters.
    """

    assert not re.search(r" {2,}", clean_location("Newfoundland  and.   Labrador"))
    assert not re.search(r" {2,}", clean_location("Newfoundlandandlabrador"))
    assert not re.search(r" {2,}", clean_location("Newfoundland and Labrador"))

def format():
    """
    Test that the output is of the format '<two-letter code>'.
    """

    assert re.match(r"^[A-Z]{2}$", clean_location("Ont."))
    assert re.match(r"^[A-Z]{2}$", clean_location("New Brunswich"))
    assert re.match(r"^[A-Z]{2}$", clean_location("Saskatchewan"))
    assert re.match(r"^[A-Z]{2}$", clean_location("Yukon"))

def output_type():
    """
    Test that the output is of type string.
    """

    # output should be string if something was modified
    assert isinstance(clean_location("City BC"), str)
    # output should be string if nothing was modified
    assert isinstance(clean_location("City, BC"), str)

def wrong_input_type():
    """
    Test that a non-string input type throws a TypeError.
    """

    with pytest.raises(TypeError):
        clean_location(123)
    
    with pytest.raises(TypeError):
        clean_location(1.1)

    with pytest.raises(TypeError):
        clean_location(True)
    
    with pytest.raises(TypeError):
        clean_location(["First Location", "Second Location"])

def incomplete_input():
    """
    Test that empty strings throw a ValueError.
    """

    with pytest.raises(ValueError):
        clean_location("")
    
    with pytest.raises(ValueError):
        clean_location(" ")

def province_territory_replacement():
    """
    Test that the function correctly matches various province/territory names and abbreviations to the official two-letter code, including small and medium typos.
    """

    testing_province_territory_replacement = {
        "british columbia": "BC", # case insensitive
        "Ont.": "ON", # periods at end
        "P.E.I": "PE", # periods between letters
        "Prince Edward Isl.": "PE", # uncommon abbreviations that are close enough to the full name
        "Saskatch.": "SK", # uncommon abbreviations that are close enoguh to the full name
        "Nfld. Lab.": "NL", # multiple abbreviations for the same province/territory
        "Alberts": "AB", # small typos
        "siskachwin": "SK", # medium typos
        "north ws territry": "NT", # medium typos
        "brit columbia": "BC", # unknown abbreviations
        "newfoundlandandlabrador": "NL", # no spaces in text input
        "newfoundland": "NL", # incomplete text input
        "qc": "QC", # minimum valid input
        "Prince-Edward-Island": "PE", # hyphens between letters
        "Newfoundland & Labrador": "NL" # other punctuation
    }

    for key, value in testing_province_territory_replacement.items():
        out = clean_location(key)
        assert out == value, f"Expected {value} but got {out}"

def same_distance_raises_error():
    """
    Test that the function raises a ValueError if the input has equal
    partial matches to two or more province/territories.
    """
    with pytest.raises(ValueError):
        clean_location("VB")

def unidentified_province_territory():
    """
    Test that the function throws a ValuError if it cannot identify a province/territory, including significant typos.
    """

    with pytest.raises(ValueError):
        clean_location("XX")
    
    with pytest.raises(ValueError):
        clean_location("C")

    with pytest.raises(ValueError):
        clean_location("Not A Province")

    with pytest.raises(ValueError):
        clean_location("alllbita")

    with pytest.raises(ValueError):
        clean_location("b colum")

# Added additional tests for helper functions as suggested by ChatGPT. I wrote the tests myself: ChatGPT only provided the suggestion that I test these functions independently.
def test_remove_punctuation():
    """
    Test that the helper function remove_punctuation removes all punctuation in the string.
    """
    assert remove_punctuation("P.E.I.") == "PEI"
    assert remove_punctuation("N.-W.-T.") == "NWT"
    assert remove_punctuation("Prince-Edward-Island") == "PrinceEdwardIsland"
    assert remove_punctuation("Newfoundland & Labrador") == "Newfoundland  Labrador"

def test_remove_spaces():
    """
    Test that the helper function remove_spaces removes all spaces in the string.
    """
    assert remove_spaces("newfoundland and labrador") == "newfoundlandandlabrador"
    assert remove_spaces("newfoundland and      labrador") == "newfoundlandandlabrador"

def test_normalize_names():
    """
    Test that the helper function normalize_names applie the correct function and does not
    do any other modifications to the dictionary.
    """
    names = {
        "AB": ["alberta", "alta."],
        "BC": ["british columbia"],
        "ON": ["ont.", "ontario"]
    }
    out = normalize_names(names, remove_spaces)

    assert set(out.keys()) == {"AB", "BC", "ON"}
    assert len(out["AB"]) == 2
    assert len(out["BC"]) == 1
    assert out["BC"][0] == "britishcolumbia"

def test_score_predictions():
    """
    Test that the helper function score_predictions gives a score of 100
    for an exact match and a score less than 100 for a non-match.
    """
    names = {"ON": ["ont.", "ontario"], "BC": ["british columbia"]}
    out = score_predictions("ontario", names)

    assert out["ON"] == 100
    assert out["BC"] < 100
    assert set(out.keys()) == {"ON", "BC"}

def test_get_max():
    """
    Test that the helper function get_max returns the maximum key and value if there
    is one maximum, and the maximum keys and value if there are multiple keys tied for
    maximum.
    """
    # one maximum
    preds = {"ON": 90, "BC": 80}
    key, value = get_max(preds)

    assert key == "ON"
    assert value == 90

    # tied keys
    preds = {"ON": 90, "BC": 90}
    keys, value = get_max(preds)

    assert set(keys) == {"ON", "BC"}
    assert value == 90

def test_try_variation():
    """
    Test that the helper function try_variation applies the specified function and returns 
    the appropriate key if a match is found, and returns 'No Match' if a match is not found.
    """
    # should match properly
    assert try_variation("b.c.", remove_punctuation, threshold=85) == "BC"
    # should not match
    assert try_variation("notaprovince", remove_punctuation, threshold=85) == "No Match"
    # should not match because threshold is too high
    assert try_variation("albrta", remove_punctuation, threshold=98) == "No Match"

def test_try_variations():
    """
    Test that the helper function try_variations returns the appropriate key if a match is found
    and raises a ValueError if no match is found.
    """
    # should match
    assert try_variations("b.c.", threshold=85) == "BC"
    assert try_variations("newfoundlandandlabrador", threshold=85) == "NL"
    assert try_variations("north west territor", threshold=85) == "NT"

    # should raise ValueError because no match
    with pytest.raises(ValueError):
        try_variations("b", threshold=85)

    # should raise ValueError because no match
    with pytest.raises(ValueError):
        try_variations("notaprovince", threshold=85)