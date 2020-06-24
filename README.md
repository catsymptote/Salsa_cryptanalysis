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
> python -m pytest --durations=n

Where n is an integer of how many of the slowest tests you want to show.

### Exclude integration and slow tests
> python -m pytest --without-integration --without-slow-integration

Uses (pytest-integration)[https://pypi.org/project/pytest-integration/] to exclude integration and slow tests.