# Salsa20 + cryptanalysis tools
Author: Paul Knutson


## Included:
* Implementation of Salsa20.
* Partial implementation of ChaCha20.
* Cryptanalysis tools like:
    * Pearson correlation tool.
    * Hamming weight and distance tool.
* Multiple test for Salsa and its quarter-round function.
* Export and import tools for encryption of files and plaintexts.
* Context Aggregation Network (CAN) in Matlab, used as a cryptanalysis tool against ciphertexts and cipherimages from Salsa20.


## Setup
This project uses [pipenv](https://pypi.org/project/pipenv/): A [pip](https://pypi.org/project/pip/) based package management system. Assuming pip [is already installed](https://pip.pypa.io/en/stable/installing/), you can install pip by running the following command:

`pip install pipenv`

Once pipenv is installed, go to the project workspace (in the terminal/CLI), and run the following command to launch the pipenv environment:

`pipenv shell`

Sync the environment to make sure the packages are up to date. The `-d` is added so the development packages will also sync:

`pipenv sync -d`


## Testing
Run the 100+ unit tests on the Python programs, by using the command:

`python -m pytest tests`

I suggest adding `tests` to the regular `python -m pytest`, as it will only look in the "tests" folder. Otherwise, it will take a while.
Add `--durations=5` to also get a list of the 5 slowest tests. This is useful when attempting to implement efficient unit tests.
Add `--without-integration` and/or `--without-slow-integration` to skip the tests marked integration or slow-integration tests (these are slower than other tests).

Simple copy/paste test command:

`clear ; python -m pytest tests --without-integration --without-slow-integration --durations=5`

The project uses [pytest-integration](https://pypi.org/project/pytest-integration/) to allow developers to exclude integration and slow tests.
