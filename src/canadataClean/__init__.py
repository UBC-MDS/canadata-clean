# MIT License
#
# Copyright (c) 2026 Molly Kessler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
canadataClean

A collection of utility functions for cleaning and validating Canada-specific structured data
in pandas DataFrames. This package helps standardize common Canadian data fields, including
phone numbers, postal codes, location names (cities and provinces), and dates, while identifying
invalid or problematic entries.

Functions in this package ensure data consistency by:
- Formatting and validating phone numbers and postal codes according to Canadian standards.
- Normalizing city and province names for consistent analysis.
- Checking dates or dates of birth against Canadian date formats.
- Highlighting invalid entries with warnings or exceptions, allowing workflows to continue
  without interruption.

This package is intended to make datasets analysis-ready while helping users identify and
correct data quality issues in Canadian datasets.
"""

from canadataClean.clean_phonenumber import clean_phonenumber
from canadataClean.clean_postalcode import clean_postalcode
from canadataClean.clean_location  import clean_location
from canadataClean.clean_date import clean_date
from .__version__ import __version__
__all__ = ["clean_phonenumber", "clean_postalcode", "clean_location", "clean_date", "__version__"]