# Advent of Code Python Starter

A tamplate for [Advent of Code](https://adventofcode.com) write in Python.

## Usage

The project use [poetry](https://python-poetry.org) for project manager.
Clone this repository and run `poetry install` for install dependencies:

    $ git clone https://github.com/ljgago/advent-of-code-python-starter aoc-python
    $ cd aoc-python

    # install dependencies
    $ poetry install

    # run tests from day01
    $ poetry run pytest tests/test_day01.py

    # run the day01
    # poetry run python -m aoc.day01

## Generate

You can generate all necesary files for use in the event with a simple
command:

    $ poetry run python -m aoc.gen day01

This command generate these files:

    * creating /aoc/day01/resources/input.txt
    * creating /aoc/day01/__main__.py
    * creating /aoc/day01/part1.py
    * creating /aoc/day01/part2.py
    * creating /aoc/day01/README.md
    * creating /tests/test_day01.py

- `/aoc/day01/resources/input.txt`: you can insert here the input data.
- `/aoc/day01/__main__.py`: is the main module.
- `/aoc/day01/part1.py`: solution for part 1.
- `/aoc/day01/part2.py`: solution for part 2.
- `/aoc/day01/README.md`: you can write the challenge statement.
- `/tests/test_day01.py`: is the module where you write the tests.

## Config

You can configure the automatic input download from the Advent of Code
session token.

For dowload the inputs from web, you needs to set the environment var
`AOC_SESSION`. You can to get the session token from the cookie web browser.

Also can you set the `AOC_YEAR` to select a certain year.
(It is not mandatory use the `AOC_YEAR`, aoc.gen can get the year automatically)

You can set an `.env` file with these variables.

> Note:
> You can avoid the generation of the folder `__pycache__` set this environment
> variable `export PYTHONDONTWRITEBYTECODE=1` o pass the `-B` flag
> after python command.

Folder structure:

    ├── aoc
    │   └── day01
    │       ├── __main__.py
    │       ├── part1.py
    │       ├── part2.py
    │       ├── README.md
    │       └── resources
    │           └── input.txt
    └── tests
        ├── conftest.py
        └── test_day01.py

Happy coding!

[MIT License](LICENSE)
