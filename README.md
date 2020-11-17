# Cryptanalysis of Salsa20.
Author: Paul Knutson

## Included:
* Implementation of Salsa20.
* Partial implementation of ChaCha20.
* Cryptanalysis tools like:
    * Pearson correlation tool.
    * Hamming weight and distance tool.
* Multiple test for Salsa and its quarter-round function.


## Testing

### Simple and full test
> python -m pytest

### Show test durations
> python -m pytest --durations=5

Where n is an integer of how many of the slowest tests you want to show.

### Exclude integration and slow tests
> python -m pytest --without-integration --without-slow-integration

### Exclude slow tests, include durations and clear before
> clear ; python -m pytest --without-integration --without-slow-integration --durations=5

### In case of slow tests
If pytest is not collecting the tests, then add `tests` after `python -m pytest`. This is due to pytest searching through a large amount of folders.

Uses [pytest-integration](https://pypi.org/project/pytest-integration/) to exclude integration and slow tests.
