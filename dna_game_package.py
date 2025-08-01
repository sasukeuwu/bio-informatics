# dna_game/__init__.py

def check_gene(sequence, guess):
    return guess in sequence


def give_hint(sequence, guess):
    if guess not in sequence:
        return "Not found"

    index = sequence.find(guess)
    hint = ["_" for _ in sequence]
    for i in range(index, index + len(guess)):
        hint[i] = sequence[i]
    return "".join(hint)


# dna_game/game.py

def play_dna_game():
    print("Welcome to the DNA Gene Finder Game!")
    sequence = "ATGCGATACGTAGCTAGCTAGCTAGCTA"
    gene = "GTAGC"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        guess = input("Guess the gene sequence: ").upper()
        if guess == gene:
            print("Correct! You've found the gene.")
            return
        else:
            print("Incorrect. Hint:", give_hint(sequence, guess))
            attempts += 1

    print("Out of attempts! The gene was:", gene)


# setup.py
from setuptools import setup, find_packages

setup(
    name='dna_game',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dna-game = dna_game.game:play_dna_game',
        ],
    },
    author='Your Name',
    description='A fun DNA sequence guessing game.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


# README.md
"""
# DNA Game

A simple terminal-based game where you guess a gene sequence within a DNA strand.

## How to Play
Run the game in your terminal:

```bash
$ dna-game
```

You get 5 tries to guess the gene hidden in a DNA sequence.

## Installation

```bash
git clone https://github.com/yourusername/dna_game.git
cd dna_game
pip install .
```

## Example Output
```
Welcome to the DNA Gene Finder Game!
Guess the gene sequence: AGCTA
Incorrect. Hint: _________AGCTA_______
...
```

## License
MIT
"""
