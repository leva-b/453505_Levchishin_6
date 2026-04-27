"""
Regular expressions for text analysis.
Lab 4, Task 2, Variant 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

import re

class RegexPatterns:
    """Container for compiled regex patterns (static attributes)."""
    
    SMILEY = re.compile(r'[:;]-*([\(\)\[\]])\1*')
    
    WORD = re.compile(r'\b[a-zA-Zа-яА-ЯёЁ]+\b')
    
    UPPERCASE_WITH_DIGIT = re.compile(r'\b[A-Z][A-Za-z]*\d\w*\b')
    
    HTML_COLOR = re.compile(r'^#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$')
    
    WORD_FOLLOWED_BY_DOT = re.compile(r'\b([a-zA-Zа-яА-ЯёЁ]+)\.')
    
    SENTENCE_END = re.compile(r'[.!?]+')
    
    DECLARATIVE = re.compile(r'[^.!?]*\.\s*$')
    INTERROGATIVE = re.compile(r'[^.!?]*\?\s*$')
    IMPERATIVE = re.compile(r'[^.!?]*!\s*$')
    
    @classmethod
    def is_html_color(cls, s: str) -> bool:
        """Check if string is a valid HTML hex color."""
        return bool(cls.HTML_COLOR.match(s.strip()))

    @classmethod
    def find_uppercase_with_digits(cls, text: str) -> list:
        """Return list of words starting with capital letter and containing digit."""
        return cls.UPPERCASE_WITH_DIGIT.findall(text)
    
    @classmethod
    def find_words_followed_by_dot(cls, text: str) -> list:
        """Return list of words that are immediately followed by a dot."""
        return [match for match in cls.WORD_FOLLOWED_BY_DOT.findall(text)]
    
    @classmethod
    def find_longest_word_ending_with_r(cls, text: str) -> str:
        """Return longest word ending with 'r' (case-insensitive). Return '' if none."""
        words = cls.WORD.findall(text)
        candidates = [w for w in words if w.lower().endswith('r')]
        if not candidates:
            return ''
        return max(candidates, key=len)
    
    @classmethod
    def count_smileys(cls, text: str) -> int:
        """Count all smileys matching the pattern."""
        return len(cls.SMILEY.findall(text))