# textutils

An open-source Python library providing simple utilities for common text-processing operations.

## Features

- `word_count(text)`: Count the number of words in a text.
- `character_count(text, include_spaces=True)`: Count the number of characters in a text, with the option to include or exclude spaces.
- `reverse(text)`: Reverse the characters in a text.
- `capitalize_words(text)`: Capitalize the first letter of each word in a text.
- `snake_case(text)`: Convert a text to snake case.
- `word_frequency(text, case_sensitive=False, ignore_words=None, min_length=1, top_n=None)`: Count how often each word appears in a text, ordered by frequency.

## Requirements

- Python 3.12 or later.

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/Emilie-Th/textutils.git
cd textutils
python -m pip install .
```

To install the package with the development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Usage

```python
from textutils import (
    word_count,
    character_count,
    reverse,
    capitalize_words,
    snake_case,
    word_frequency,
)

print(word_count("Hello Open Source!"))
print(character_count("Hello Open Source!", include_spaces=False))
print(reverse("Hello Open Source!"))
print(capitalize_words("hello open source!"))
print(snake_case("Hello Open Source!"))
print(word_frequency("Python is great. Python is simple."))
```

## Testing

The project uses **pytest** for automated testing and **pytest-cov** to measure test coverage.

Run the complete test suite:

```bash
python -m pytest -q
```

Run the tests with a coverage report:

```bash
python -m pytest -q --cov=textutils --cov-report=term-missing
```

## Code Quality

The project uses **Black** for consistent code formatting and **Ruff** for linting and static code analysis.

Check formatting with Black:

```bash
python -m black --check .
```

Format the code automatically:

```bash
python -m black .
```

Check code quality with Ruff:

```bash
python -m ruff check .
```

These checks should pass before submitting a pull request.

## Contributing

Contributions are welcome!

Before submitting a pull request, please:

1. Add or update tests for any changes.
2. Ensure all tests pass.
3. Check the code with Black and Ruff.
4. Follow the existing package structure and document public functions using NumPy-style docstrings.

## License

This project is licensed under the MIT License.