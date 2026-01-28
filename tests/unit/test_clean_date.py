import pytest
from canadataClean.clean_date import clean_date

# Theses tests assume the input date strings are in date formats, inviad formats will raise ValueError
def test_valid_date_formats():
    """Test various valid date formats and conversions, covering 4 edge cases: YYYY-MM-DD, DD/MM/YYYY, DD-MM-YYYY, and single-digit handling."""
    # YYYY-MM-DD 
    assert clean_date("1990-05-15") == "1990-05-15"
    # DD/MM/YYYY conversion
    assert clean_date("15/05/1990") == "1990-05-15"
    # DD-MM-YYYY conversion
    assert clean_date("15-05-1990") == "1990-05-15"
    # Single-digit day and month
    assert clean_date("5/8/1990") == "1990-08-05"

def test_whitespace_and_separator_normalization():
    """Test whitespace stripping and separator normalization, covering 4 edge cases: trailing/leading whitespace, spaces around slashes, spaces around hyphens, and combination."""
    # Trailing and leading whitespace
    assert clean_date("  1991-10-20  ") == "1991-10-20"
    # Spaces around slashes
    assert clean_date("15 / 05 / 1990") == "1990-05-15"
    # Spaces around hyphens
    assert clean_date("15 - 05 - 1990") == "1990-05-15"
    # Combination of both
    assert clean_date(" 5 / 8 / 1990 ") == "1990-08-05"

def test_invalid_dates_and_parsing_errors():
    """Test invalid dates and unparseable inputs, covering 4 edge cases: invalid leap year, logically invalid date, unparseable string, and unsupported MM/DD/YYYY."""
    # Invalid leap year (Feb 29 in non-leap year)
    with pytest.raises(ValueError, match="Unable to parse date"):
        clean_date("29/02/2021")
    # Logically invalid date (Feb 30)
    with pytest.raises(ValueError, match="Unable to parse date"):
        clean_date("30/02/1990")
    # Unparseable input
    with pytest.raises(ValueError, match="Unable to parse date"):
        clean_date("not a date")
    # Unsupported MM/DD/YYYY to avoid ambiguity
    with pytest.raises(ValueError, match="Unable to parse date"):
        clean_date("05/15/1990")

def test_year_and_future_validations():
    """Test year range and future date validations, covering 4 edge cases: below default min_year, below custom min_year, future date not allowed, future date allowed."""
    # Below default min_year (1900)
    with pytest.raises(ValueError, match="Date year 1850 is below minimum allowed year 1900"):
        clean_date("1850-05-15")
    # Below custom min_year
    with pytest.raises(ValueError, match="Date year 1850 is below minimum allowed year 1900"):
        clean_date("1850-05-15", min_year=1900)
    # Future date not allowed (default)
    with pytest.raises(ValueError, match="Date cannot be in the future"):
        clean_date("2035-01-01")
    # Future date allowed
    assert clean_date("2030-01-01", allow_future=True) == "2030-01-01"

def test_empty_and_none_inputs():
    """Test empty, whitespace-only, and None inputs, covering 3 edge cases: empty string, whitespace-only string, and None (though None raises TypeError, we handle as ValueError)."""
    # Empty string
    with pytest.raises(ValueError, match="Date string cannot be empty or None"):
        clean_date("")
    # Whitespace-only string
    with pytest.raises(ValueError, match="Date string cannot be empty or None"):
        clean_date("   ")
    # Singe whitespace string
    with pytest.raises(ValueError, match="Date string cannot be empty or None"):
        clean_date(" ")
    # None input (defensive handling)
    with pytest.raises(ValueError, match="Date string cannot be empty or None"):
        clean_date(None)