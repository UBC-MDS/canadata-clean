# canadata-clean

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/canadata-clean.svg)](https://pypi.org/project/canadata-clean/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/canadata-clean.svg)](https://pypi.org/project/canadata-clean/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

canadata-clean provides a collection of utility functions for cleaning and validating Canada-specific structured data in pandas DataFrames. The package is designed to help users efficiently standardize common Canadian data fields while identifying invalid or problematic entries.

## Summary

This package helps ensure data consistency for Canadian information by formatting and validating phone numbers, postal codes, and city or province names, and by checking birthdays or dates of birth against Canadian date formats, highlighting any invalid entries.

When a value does not meet the required Canadian format, canadata-clean raises a warning-type error to flag the invalid entry while allowing data processing to continue. This makes it easy to identify and address data quality issues without interrupting workflows, while still producing clean, analysis-ready datasets.

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install canadata-clean
```

To use canadata-clean in your code:

```python
import canadata-clean
```

### Functions
```python
clean_birthay(date)
```
This function cleans and validates a date string, converting common formats to the Canadian standard YYYY-MM-DD (ISO 8601).

```python
clean_postcode(postal_code)
```
This function cleans and validates a Canadian postal code string field to ensure that it matches the Canadian postal code format (e.g., "A1A 1A1").

```python
clean_location(location)
```
This function cleans and validates a free-text entry representing a general location (municipality name and province or territory) in Canada and convert it to the format "MunicipalityName, TwoLetterProvinceOrTerritoryCode"

```python
clean_phonenumber(phone_number)
```
This function cleans and validates a phone number string field to ensure that it matches the Canadian phone number format.

## Where This Fits in the Python Ecosystem

canadata-clean fits into the broader Python data processing and data quality ecosystem, alongside libraries such as [pandas](https://pandas.pydata.org/) and data validation tools like [pydantic](https://docs.pydantic.dev/latest/) . While pandas provides flexible, general-purpose tools for data manipulation, and pydantic offers highly configurable rule-based systems, canadata-clean focuses on a lightweight and targeted approach to data cleaning.

The package specializes in Canada-specific data standardization and validation, including postal codes, phone numbers, provinces, cities, and date formats. Unlike more general or schema-heavy validation libraries, canadata-clean offers simple, string-based utility functions that can be easily integrated into existing pandas workflows. It is designed for users who need fast, consistent cleaning of Canadian datasets without configuring complex validation pipelines, making it well-suited for practical data preparation and preprocessing tasks.

## Contributors
- Molly Kessler
- Raymond Wang
- Sasha S
- Randall Lee

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`canadata-clean` was created by Molly Kessler, Raymond Wang, Sasha S, Randall Lee. It is licensed under the terms of the [MIT License](./LICENSE).

## Credits

`canadata-clean` was created with [`pyopensci`](https://www.pyopensci.org/python-package-guide/tutorials/create-python-package.html).