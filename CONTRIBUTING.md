## Acknowledgments

This project was created by adapting a Python package template generated with [Copier](https://copier.readthedocs.io/).

The original template provided the initial project structure, tooling (Hatch), and contributing guidelines. We modified and extended it to fit the needs of our **canadata-clean** project, which focuses on standardizing Canadian data formats.

# Contributing

Contributions of all kinds are welcome here, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## About This Project

This project focuses on cleaning and standardizing text data to follow Canadian formatting conventions. This includes:

- **Canadian Phone Numbers**: Formatting phone numbers to follow Canadian standards (e.g., +1 (XXX) XXX-XXXX)
- **Canadian Postal Codes**: Validating and formatting postal codes (e.g., A1A 1A1)
- **Canadian Date Formats**: Standardizing dates to Canadian conventions (YYYY-MM-DD)
- **Canadian Locations Formatting**: Ensuring locations follow Canada Post guidelines

**Important**: After the repository is set up, each group member should work in a GitHub flow workflow:

1. **Create a branch** for each feature or fix from the `main` branch
2. **Make your changes** in the feature branch
3. **Open a pull request** when ready for review
4. **Code review**:  At least one other teammate must review and critique the pull request before it can be merged
5. **Address feedback**:  Make any requested changes based on the review
6. **Merge**:  Once approved, the pull request can be merged into `main`

This collaborative approach ensures code quality and knowledge sharing across the team.

## Example Contributions

You can contribute in many ways, for example:

* [Report bugs](#report-bugs)
* [Fix Bugs](#fix-bugs)
* [Implement Features](#implement-features)
* [Write Documentation](#write-documentation)
* [Submit Feedback](#submit-feedback)

### Report Bugs

Report bugs at https://github.com/kessler24/canadata_clean/issues.

**If you are reporting a bug, please follow the template guidelines. The more
detailed your report, the easier and thus faster we can help you.**

### Fix Bugs

Look through the GitHub issues for bugs. Anything labelled with `bug` and
`help wanted` is open to whoever wants to implement it. When you decide to work on such
an issue, please assign yourself to it and add a comment that you'll be working on that,
too. If you see another issue without the `help wanted` label, just post a comment, the
maintainers are usually happy for any support that they can get.

### Implement Features

Look through the GitHub issues for features. Anything labelled with
`enhancement` and `help wanted` is open to whoever wants to implement it. As
for [fixing bugs](#fix-bugs), please assign yourself to the issue and add a comment that
you'll be working on that, too. If another enhancement catches your fancy, but it
doesn't have the `help wanted` label, just post a comment, the maintainers are usually
happy for any support that they can get.

### Write Documentation

canadata-clean could always use more documentation, whether as
part of the official documentation, in docstrings, or even on the web in blog
posts, articles, and such. Just
[open an issue](https://github.com/kessler24/canadata_clean/issues)
to let us know what you will be working on so that we can provide you with guidance.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/kessler24/canadata_clean/issues. If your feedback fits the format of one of
the issue templates, please use that. Remember that this is a volunteer-driven
project and everybody has limited time.

## Get Started!

Ready to contribute? Here's how to set up canadata-clean for
local development.

1. Clone the https://github.com/kessler24/canadata_clean
   repository on GitHub.

    ```shell
    git clone git@github.com:your_name_here/canadata_clean.git
    ```

2. [Install hatch](https://hatch.pypa.io/latest/install/).

3. Create a branch for local development using the default branch (typically `main`) as a starting point. Use `fix` or `clean` as a prefix for your branch name.

    ```shell
    git checkout main
    git checkout -b clean-name-of-your-func
    ```

    Now you can make your changes locally.

4. When you're done making changes, apply the quality assurance tools and check
   that your changes pass our test suite. This is all included with tox

    ```shell
    hatch run test:run
    ```

5. Commit your changes and push your branch to GitHub. Please use [semantic
   commit messages](https://www.conventionalcommits.org/).

    ```shell
    git add .
    git commit -m "fix: summarize your changes"
    git push -u origin fix-name-of-your-bugfix
    ```

6. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request.

7. At least one teammate must review your pull request before it can be merged.

### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests for Canadian formatting functionality.
2. If the pull request adds functionality, the docs should be updated. Put your new functionality into a function with a docstring that explains the Canadian formatting standards being applied.
3. Your pull request must be **reviewed and approved by at least one other team member** before merging.
4. Your pull request will automatically be checked by the full test suite. It needs to pass all of them before it can be considered for merging.
5. Ensure your code follows the project's coding standards and includes appropriate error handling for edge cases in Canadian data formatting.