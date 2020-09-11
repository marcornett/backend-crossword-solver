#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
"""Crossword Solver Program"""

__author__ = "marcornett"

# YOUR HELPER FUNCTION GOES HERE


def search(reg_str, words):
    pattern = re.compile(f'{reg_str}')
    matches = []
    for word in words:
        match = pattern.findall(word)
        if match:
            matches.extend(match)
    return ', '.join(matches)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()
    test_word = input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
    reg_str = test_word.replace(' ', "\w")
    matches = search(reg_str, words)
    print(matches)


if __name__ == '__main__':
    main()
