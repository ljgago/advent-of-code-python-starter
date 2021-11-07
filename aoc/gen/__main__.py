import sys, os, errno
import re
from pathlib import Path
from string import Template
from datetime import date

from colorama import Fore, Style
from dotenv import load_dotenv
import requests

# return a substring with the relative path
def relative_path(filename):
    path = Path(__file__).parent.resolve()
    project_path = Path(path / "../../../").parent.resolve()
    full_path = Path(path / filename).resolve()
    r_path = str(full_path).split(str(project_path))
    return r_path[1]

# print a status of the generated files
def info(filename, status):
    r_path = relative_path(filename)
    if status:
        print("{}* creating{} {}".format(Fore.GREEN, Style.RESET_ALL, r_path))
    else:
        print("{}* ignoring{} {} already exists".format(Fore.YELLOW, Style.RESET_ALL, r_path))

# open the file in read mode
def read_file(filename):
    path = Path(__file__).parent.resolve()
    with open(path / filename, 'r') as f:
        return f.read()

# create and write the files
def write_file(filename, content):
    path = Path(__file__).parent.resolve()
    if not Path(path / filename).parent.exists():
        try:
            Path(path / filename).parent.mkdir(parents=True)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    if not Path(path / filename).exists():
        with open(path / filename, 'w') as f:
            f.write(content)

        info(filename, True)
    else:
        info(filename, False)
        return

# get de default year
def default_year():
    today = date.today()
    if today.day == 12:
        return today.year
    else:
        return today.year - 1

# get the environment variables
def get_env():
    year = os.getenv("AOC_YEAR")
    if year is None:
        year = default_year()

    session = os.getenv("AOC_SESSION")
    return year, session

# generate the input from the url
def gen_input(path, year, day, session):
    if session is not None:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        headers = {"cookie": f"session={session}"}
        r = requests.get(url, headers=headers)
        content = r.text
        write_file(path, content)
    else:
        write_file(path, "")

# generate the base code from templates
def gen_template(templates, paths, substitute):
    for i in list(zip(templates, paths)):
        data = read_file(i[0])
        t = Template(data)
        content = t.substitute(substitute)
        path = i[1].format(substitute["module_name"])
        write_file(path, content)

def main():
    load_dotenv()
    if len(sys.argv) is not 2:
        print("--- aoc.gen needs one only argument ---")
        return

    module_name = sys.argv[1]
    m = re.search(r'(?<=day)\d+(?!\w)', module_name)
    if m is None:
        print("--- The argument must be `day + NUM` (e.g. day01) ---")
        return
    day = int(m.group(0))

    templates = [
        "./templates/__main__.tpl",
        "./templates/part1.tpl",
        "./templates/part2.tpl",
        "./templates/readme.tpl",
        "./templates/test_day.tpl",
    ]

    paths = [
        "../{}/__main__.py",
        "../{}/part1.py",
        "../{}/part2.py",
        "../{}/README.md",
        "../../tests/test_{}.py"
    ]

    year, session = get_env()
    input_path = "../{}/resources/input.txt".format(module_name)
    gen_input(input_path, year, day, session)
    gen_template(templates, paths, {"module_name": module_name, "day": day})

if __name__ == "__main__":
    main()
