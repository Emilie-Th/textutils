# textutils

An open-source Python library providing simple utilities for common text-processing operations.

## Features

- `word_count(text)`: Count the number of words in a text.
- `character_count(text, include_spaces=True)`: Count the number of characters in a text, with the option to include or exclude spaces.
- `reverse(text)`: Reverse the characters in a text.
- `capitalize_words(text)`: Capitalize the first letter of each word in a text.
- `snake_case(text)`: Convert a text to snake case.
- `word_frequency(text, case_sensitive=False, ignore_words=None, min_length=1, top_n=None)`: Count how often each word appears in a text, ordered by frequency.


## Usage

```python
from textutils import word_count, character_count, reverse, capitalize_words, snake_case, word_frequency

print(word_count("Hello Open Source!"))
print(character_count("Hello Open Source!", include_spaces=False))
print(reverse("Hello Open Source!"))
print(capitalize_words("hello open source!"))
print(snake_case("Hello Open Source!"))
print(word_frequency("Python is great. Python is simple."))
```


## Contributing

Contributions are welcome!


## License

This project is licensed under the MIT License.