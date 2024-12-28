# 8 Queens problem solver

This is a visualiser of [8 Queens Puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) 
written in Python 3.12 and tkinter.

It presents either 12 unique solutions or all 92 solutions.

To count number of unique solution from non unique, one can use
[Burnside's lemma](https://en.wikipedia.org/wiki/Burnside%27s_lemma) and
[Dihedral group](https://en.wikipedia.org/wiki/Dihedral_group) D<sub>4</sub>

(92 + 0 + 4 + 0 + 0 + 0 + 0 + 0) / 8 = 12

## Setup

You have to install python3-tk in your system
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install poetry 
poetry install
```

## Usage
Using .venv created by poetry
```bash
python -m visualiser
```