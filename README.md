# canadataClean

|  |  |
|------------------------------------|------------------------------------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/canadataClean.svg)](https://test.pypi.org/project/canadataClean/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/canadataClean.svg)](https://test.pypi.org/project/canadataClean/) |
| Meta | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

canadataClean provides a collection of utility functions for cleaning and validating Canada-specific structured data in pandas DataFrames. The package is designed to help users efficiently standardize common Canadian data fields while identifying invalid or problematic entries.

## Summary

This package helps ensure data consistency for Canadian information by formatting and validating phone numbers, postal codes, and city or province names, and by checking dates or dates of birth against Canadian date formats, highlighting any invalid entries.

When a value does not meet the required Canadian format, canadataClean raises a warning-type error to flag the invalid entry while allowing data processing to continue. This makes it easy to identify and address data quality issues without interrupting workflows, while still producing clean, analysis-ready datasets.

## Installation

To reproduce the environment, run:

``` bash
conda env create -f environment.yml
conda activate canadataClean
```

You can install this package into your preferred Python environment using pip:

``` bash
$ pip install canadataClean
```

To use canadataClean in your code:

``` python
from canadataClean import clean_date, clean_location, clean_phonenumber, clean_postalcode
```

## Functions

``` python
clean_date(date)
```

This function cleans and validates a date string, converting common formats to the Canadian standard YYYY-MM-DD (ISO 8601).

``` python
clean_postalcode(postal_code)
```

This function cleans and validates a Canadian postal code string field to ensure that it matches the Canadian postal code format. This is a six-character code defined and maintained by Canada Post Corporation (CPC) for the purpose of sorting and delivering mail. The characters are arranged in the form 'ANA NAN', where 'A' represents an alphabetic character and 'N' represents a numeric character (e.g., K1A 0T6). More information about Canadian postal codes can be found [here](https://www150.statcan.gc.ca/n1/pub/92-154-g/2015001/tech-eng.htm).

``` python
clean_location(location)
```

This function cleans and validates a free-text entry representing Canadian province or territory and returns the two letter province or territory code, e.g. "BC" for "British Columbia". The abbrieviations for Canadian provinces and territories can be found [here](https://www.noslangues-ourlanguages.gc.ca/en/writing-tips-plus/abbreviations-canadian-provinces-and-territories).

``` python
clean_phonenumber(phone_number)
```

This function cleans and validates a phone number string field to ensure that it matches the Canadian phone number format ("+1 (XXX) XXX-XXXX") which includes the country code (+1) followed by a 10-digit number.

## To run the tests

You can run the tests for this package using `pytest`. First, install the testing dependencies:

``` bash
$ pip install -e.[test]
```

Then, run the tests with:

```         
$ pytest
```

To view the test coverage, run the following command:

```         
$ pytest --cov=src/canadata_clean
```

## Documentation

The online documentation for this package can be found [here.](https://ubc-mds.github.io/canadataClean/)

To generate and preview the reference documentation, use the following command:

``` bash
quartodoc build --watch
quarto preview
```

## Usage

1.  Standardizing Dates: The clean_date function standardizes a string to the Canadian format YYYY-MM-DD (ISO 8601)

``` python
from canadataClean.clean_date import clean_date
clean_date = clean_date("date") # Replace date with the actual date
```

2.  Standardizing Postal Code: The clean_postalcode function standardizes a string to the Canadian postal code format (e.g., "A1A 1A1")

``` python
from canadataClean.clean_postalcode import clean_postalcode
clean_postalcode = clean_postalcode("postal_code") # Replace postal_code with the actual postal_code
```

3.  Standardizing Provinces and Territories: The clean_location function standardizes a string to the two letter province or territory code (e.g. "BC" for "British Columbia")

``` python
from canadataClean.clean_location import clean_location
clean_location = clean_location("location") # Replace location with the actual province or territory
```

4.  Standardizing Phone Number: The clean_phonenumber function standardizes a string to the Canadian phone number format ("+1 (XXX) XXX-XXXX")

``` python
from canadataClean.clean_phonenumber import clean_phonenumber
clean_phonenumber = clean_phonenumber("phone_number") # Replace phone number with the actual phone number
```

## Where This Fits in the Python Ecosystem

canadataClean fits into the broader Python data processing and data quality ecosystem, alongside libraries such as [pandas](https://pandas.pydata.org/) and data validation tools like [pydantic](https://docs.pydantic.dev/latest/) . While pandas provides flexible, general-purpose tools for data manipulation, and pydantic offers highly configurable rule-based systems, canadataClean focuses on a lightweight and targeted approach to data cleaning.

The package specializes in Canada-specific data standardization and validation, including postal codes, phone numbers, provinces, cities, and date formats. Unlike more general or schema-heavy validation libraries, canadataClean offers simple, string-based utility functions that can be easily integrated into existing pandas workflows. It is designed for users who need fast, consistent cleaning of Canadian datasets without configuring complex validation pipelines, making it well-suited for practical data preparation and preprocessing tasks.

### Dependencies

-   [python == 3.13.7](https://www.python.org/downloads/release/python-3137/)

## Contributors

-   Molly Kessler
-   Raymond Wang
-   Sasha S
-   Randall Lee

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`canadataClean` was created by Molly Kessler, Raymond Wang, Sasha S, Randall Lee. It is licensed under the terms of the [MIT License](./LICENSE).

## Credits

`canadataClean` was created with [`pyopensci`](https://www.pyopensci.org/python-package-guide/tutorials/create-python-package.html).
