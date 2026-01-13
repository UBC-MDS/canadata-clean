import pytest
from canadata_clean.clean_date import clean_date

def test_whitespace():
    """Test that leading and trailing whitespace is stripped."""
    out = clean_date(" 1991-10-20")
    expected_out = "1991-10-20"
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_dd_mm_yyyy_format():
    """Test conversion from DD/MM/YYYY to YYYY-MM-DD."""
    out = clean_date("15/05/1990")
    expected_out = "1990-05-15"
    assert out == expected_out, f"Expected {expected_out} but got {out}"
    
def test_single_digit_day_month():
    """Test handling of single-digit days and months."""
    out = clean_date("5/8/1990")
    expected_out = "1990-08-05"
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_leap_year_valid():
    """Test that valid leap year date (Feb 29) is accepted."""
    out = clean_date("29/02/2020")
    expected_out = "2020-02-29"
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_year_below_minimum():
    """Test that dates below min_year (default 1900) raise ValueError."""
    with pytest.raises(ValueError) as exc_info:
        clean_date("1850-05-15")
    assert "1850" in str(exc_info.value) and ("minimum" in str(exc_info.value).lower() or "below" in str(exc_info.value).lower())
