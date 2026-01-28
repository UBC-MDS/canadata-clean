# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Implementing Code Coverage functionality for test coverage visualization
- Implementing test for successful quarto documentation build using Netlify
- Adding tutorial (vignette) to demonstrate package functionality and usage
- Initiating a package review and making improvements based on feedback received

## [0.0.1] - (2026-01-08)

- Created empty shells for 4 data cleaning functions
- Adapted contributing and code of conduct from Copier template
- Created readme with summary, list of functions, and where our package fits in the python ecosystem

## [1.0.0] - (2026-01-16)

- Implemented clean_postalcode, clean_location, clean_date and clean_phonenumber functions
- Implemented test_clean_postalcode, test_clean_location, test_clean_date test_clean_phonenumber tests
- Implemented exception handling for tests
- Consulted with LLMs to improve functionality and test cases

## [2.0.1] - (2026-01-23)

- Created quarto documentation site for package documentation and published to GitHub pages
- Created build-deploy workflow with build action that runs pytest tests and  deploy action that deploys package to TestPyPI