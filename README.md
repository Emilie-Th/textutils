# textutils

An open-source Python library providing simple utilities for common text-processing operations.

## Features

- `word_count(text)`: Count the number of words in a text.
- `character_count(text, include_spaces=True)`: Count the number of characters in a text, with the option to include or exclude spaces.
- `reverse(text)`: Reverse the characters in a text.
- `capitalize_words(text)`: Capitalize the first letter of each word in a text.


## Usage

```python
from textutils import word_count, character_count, reverse, capitalize_words

print(word_count("Hello Open Source!"))
print(character_count("Hello Open Source!", include_spaces=False))
print(reverse("Hello Open Source!"))
print(capitalize_words("hello open source!"))
```


## Contributing

Contributions are welcome!


## License

This project is licensed under the MIT License.