"""Singleton spacy instance for all other modules to use."""
import spacy
from spacy.lexeme import Lexeme

NLP = spacy.load('en')


def parse_docs(files):
    """Return generator of all parsed files."""
    return NLP.pipe(files)


def convert_to_string(orth):
    """Return a string given its id."""
    return NLP.vocab.strings[orth]


def is_interesting_word(word):
    """Return false for punctuation or stopword tokens."""
    return word.is_alpha and not word.is_stop
