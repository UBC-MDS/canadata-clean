# canadataClean

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/canadataClean.svg)](https://pypi.org/project/canadataClean/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/canadataClean.svg)](https://pypi.org/project/canadataClean/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

canadataClean provides a collection of utility functions for cleaning and validating Canada-specific structured data in pandas DataFrames. The package is designed to help users efficiently standardize common Canadian data fields while identifying invalid or problematic entries.

## Summary

This package helps ensure data consistency for Canadian information by formatting and validating phone numbers, postal codes, and city or province names, and by checking dates or dates of birth against Canadian date formats, highlighting any invalid entries.

When a value does not meet the required Canadian format, canadataClean raises a warning-type error to flag the invalid entry while allowing data processing to continue. This makes it easy to identify and address data quality issues without interrupting workflows, while still producing clean, analysis-ready datasets.

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install canadataClean
```

To use canadataClean in your code:

```python
from canadataClean import clean_date, clean_location, clean_phonenumber, clean_postalcode
```

### Functions
```python
clean_date(date)
```
This function cleans and validates a date string, converting common formats to the Canadian standard YYYY-MM-DD (ISO 8601).

```python
clean_postalcode(postal_code)
```
This function cleans and validates a Canadian postal code string field to ensure that it matches the Canadian postal code format (e.g., "A1A 1A1").

```python
clean_location(location)
```
This function cleans and validates a free-text entry representing Canadian province or territory and returns the two letter province or territory code, e.g. "BC" for "British Columbia".

```python
clean_phonenumber(phone_number)
```
This function cleans and validates a phone number string field to ensure that it matches the Canadian phone number format ("+1 (XXX) XXX-XXXX").

## To run the tests

You can run the tests for this package using `pytest`. First, install the testing dependencies:

```bash
$ pip install -e.[test]
```

Then, run the tests with:
```
$ pytest
```

## Where This Fits in the Python Ecosystem

canadataClean fits into the broader Python data processing and data quality ecosystem, alongside libraries such as [pandas](https://pandas.pydata.org/) and data validation tools like [pydantic](https://docs.pydantic.dev/latest/) . While pandas provides flexible, general-purpose tools for data manipulation, and pydantic offers highly configurable rule-based systems, canadataClean focuses on a lightweight and targeted approach to data cleaning.

The package specializes in Canada-specific data standardization and validation, including postal codes, phone numbers, provinces, cities, and date formats. Unlike more general or schema-heavy validation libraries, canadataClean offers simple, string-based utility functions that can be easily integrated into existing pandas workflows. It is designed for users who need fast, consistent cleaning of Canadian datasets without configuring complex validation pipelines, making it well-suited for practical data preparation and preprocessing tasks.

### Dependencies
- [python == 3.13.7](https://www.python.org/downloads/release/python-3137/)

## Contributors
- Molly Kessler
- Raymond Wang
- Sasha S
- Randall Lee

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`canadataClean` was created by Molly Kessler, Raymond Wang, Sasha S, Randall Lee. It is licensed under the terms of the [MIT License](./LICENSE).

## Credits

`canadataClean` was created with [`pyopensci`](https://www.pyopensci.org/python-package-guide/tutorials/create-python-package.html).