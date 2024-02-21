import sys
import wikipedia as wiki


def add(a, b):
    return a + b


def diff(a, b):
    return abs(a - b)


def wiki_summary(name="Microsoft", lines=2):
    result = wiki.summary(name, sentences=lines)
    return result
