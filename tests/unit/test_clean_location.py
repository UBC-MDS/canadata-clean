"""
A test module for the location cleaning functions.
"""
import pytest
import re
from canadata_clean.clean_location import clean_location

def test_clean_location():
    """
    Test that clean_location works as expected.
    """

    test_empty()
    test_output_type()
    test_incomplete_input()
    test_capitalization()
    test_spaces_sides()
    test_spaces_middle()
    test_format()
    test_unidentified_province_territory()
    test_province_territory_replacement()
    test_compass_directions_replacement()

def test_empty():
    """
    Test that the function never returns an empty string.
    """

    assert clean_location("City, BC"), "Output should not be empty."
 
def test_capitalization():
    """
    Test that the municipality name is converted to title case.
    """

    out = clean_location("my ciTy, BC")
    expected_out = "My City, BC"
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_spaces_sides():
    """
    Test that the output string starts and ends in a non-space character.
    """

    out = clean_location("  City, BC   ")
    assert not out.startswith(" "), "Output should not begin with a space."
    assert not out.endswith(" "), "Output should not end with a space."

def test_spaces_middle():
    """
    Test that the output string does not have more than one space between characters.
    """

    assert not re.search(r" {2,}", clean_location("Lots  of    spaces, BC"))
    assert not re.search(r" {2,}", clean_location("NoSpaces, BC"))
    assert not re.search(r" {2,}", clean_location("One Space, BC"))

def test_format():
    """
    Test that the output is of the format '<any characters>, <two-letter code>'.
    """

    assert re.match(r"^.+, [A-Z]{2}$", clean_location("My City British Columbia"))
    assert re.match(r"^.+, [A-Z]{2}$", clean_location("My City, BC"))
    assert re.match(r"^.+, [A-Z]{2}$", clean_location("My, Comma, City British Columbia"))
    assert re.match(r"^.+, [A-Z]{2}$", clean_location("A British Columbia"))

def test_output_type():
    """
    Test that the output is of type string.
    """

    # output should be string if something was modified
    assert isinstance(clean_location("City BC"), str)
    # output should be string if nothing was modified
    assert isinstance(clean_location("City, BC"), str)

def test_wrong_input_type():
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

def test_incomplete_input():
    """
    Test that incomplete inputs, i.e. inputs that do not contain both a province/territory 
    and a municipality, throw a ValueError. There is some overlap between this test and
    the test_unidentified_province_territory test.
    """

    with pytest.raises(ValueError):
        clean_location("")
    
    with pytest.raises(ValueError):
        clean_location(" ")
    
    with pytest.raises(ValueError):
        clean_location("BC")
    
    with pytest.raises(ValueError):
        clean_location("My City")

def test_unidentified_province_territory():
    """
    Test that the function throws a ValuError if it cannot identify a province/territory, including if a
    province/territory is not specified.
    """

    with pytest.raises(ValueError):
        clean_location("My City, XX")
    
    with pytest.raises(ValueError):
        clean_location("My City")

    with pytest.raises(ValueError):
        clean_location("My City, Not A Province")
    
    # significant typos will not match correctly
    with pytest.raises(ValueError):
        clean_location("My City, norht west terr")

def test_province_territory_replacement():
    """
    Test that the function correctly matches various province/territory names and abbreviations to the
    official two-letter code, including small typos.
    """

    testing_province_territory_replacement = {
        "City british columbia": "City, BC", # function should be case insensitive
        "City Manitoba": "City, MB",
        "City Man.": "City, MB",
        "City Ont.": "City, ON",
        "Quebec City Quebec": "Quebec City, QC", # municipality name contains province/territory
        "City P.E.I": "City, PE",
        "City Sask.": "City, SK",
        "City Nfld. Lab.": "City, NL", # multiple abbreviations for the same province/territory
        "City N.B.": "City, NB", # punctuation around two-letter-code
        "City Alberts": "City, AB" # small typos should be matched using fuzzy matching
    }

    for key, value in testing_province_territory_replacement.items():
        out = clean_location(key)
        assert out == value, f"Expected {value} but got {out}"

def test_compass_directions_replacement():
    """
    Test that the compass direction replacement dictionary properly replaces abbreviated compass
    directions and those with extra spaces.
    """

    testing_compass_directions = {
        "NW City, BC": "Northwest City, BC",
        "South east City, BC": "Southeast City, BC",
        "N City, BC": "North City, BC",
        "W West City, BC": "West City, BC",
        "Northeast City, BC": "Northeast City, BC"
    }

    for key, value in testing_compass_directions.items():
        out = clean_location(key)
        assert out == value, f"Expected {value} but got {out}"