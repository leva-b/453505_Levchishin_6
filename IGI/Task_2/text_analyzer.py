"""
Text analysis classes with inheritance, mixins, magic methods.
Lab 4, Task 2, Variant 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

import re
from typing import List, Dict, Tuple
from .regex_utils import RegexPatterns

class StatisticsMixin:
    """Mixin providing statistical calculations."""
    
    def avg_length(self, items: List[str]) -> float:
        """Average length of items (words or sentences)."""
        if not items:
            return 0.0
        return sum(len(item) for item in items) / len(items)
    
    def min_length_words(self, words: List[str]) -> Tuple[int, List[str]]:
        """Return (min_length, list_of_words_with_min_length)."""
        if not words:
            return 0, []
        min_len = min(len(w) for w in words)
        min_words = [w for w in words if len(w) == min_len]
        return min_len, min_words


class Text(StatisticsMixin):
    """Represents a text with analysis capabilities."""
    
    _instance_count = 0   # static attribute
    
    def __init__(self, content: str):
        self._content = content
        self._sentences = self._split_sentences()
        Text._instance_count += 1
        self._id = Text._instance_count
    
    # ---- Properties ----
    @property
    def content(self) -> str:
        return self._content
    
    @content.setter
    def content(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Content must be string")
        self._content = value
        self._sentences = self._split_sentences()
    
    @property
    def sentences(self) -> List[str]:
        return self._sentences.copy()
    
    @property
    def id(self) -> int:
        return self._id
    
    # ---- Private methods ----
    def _split_sentences(self) -> List[str]:
        """Split text into sentences using punctuation .!? as separators."""
        # Simple split: keep delimiters? We'll split and strip
        raw = re.split(r'([.!?]+)', self._content)
        sentences = []
        for i in range(0, len(raw)-1, 2):
            sent = (raw[i] + raw[i+1]).strip()
            if sent:
                sentences.append(sent)
        # If last part has no delimiter, ignore (incomplete)
        return sentences
    
    def _get_words(self, text_segment: str = None) -> List[str]:
        """Extract all word tokens (letters only) from text or segment."""
        segment = text_segment if text_segment is not None else self._content
        return RegexPatterns.WORD.findall(segment)
    
    # ---- Public analysis methods ----
    def sentence_count(self) -> int:
        return len(self._sentences)
    
    def sentence_types(self) -> Dict[str, int]:
        """Return counts of declarative (.), interrogative (?), imperative (!)."""
        counts = {'declarative': 0, 'interrogative': 0, 'imperative': 0}
        for sent in self._sentences:
            if sent.endswith('.'):
                counts['declarative'] += 1
            elif sent.endswith('?'):
                counts['interrogative'] += 1
            elif sent.endswith('!'):
                counts['imperative'] += 1
        return counts
    
    def avg_sentence_length_chars(self) -> float:
        """Average length of sentences in characters (only words, no spaces/punctuation)."""
        word_lengths = []
        for sent in self._sentences:
            words = self._get_words(sent)
            for w in words:
                word_lengths.append(len(w))
        if not word_lengths:
            return 0.0
        return sum(word_lengths) / len(self._sentences)
    
    def avg_word_length(self) -> float:
        """Average length of words in characters."""
        all_words = self._get_words()
        return self.avg_length(all_words)
    
    def count_smileys(self) -> int:
        return RegexPatterns.count_smileys(self._content)
    
    # ---- Variant-specific methods ----
    def words_uppercase_with_digits(self) -> List[str]:
        return RegexPatterns.find_uppercase_with_digits(self._content)
    
    def words_followed_by_dot(self) -> List[str]:
        return RegexPatterns.find_words_followed_by_dot(self._content)
    
    def longest_word_ending_r(self) -> str:
        return RegexPatterns.find_longest_word_ending_with_r(self._content)
    
    def min_length_words_info(self) -> Tuple[int, List[str]]:
        all_words = self._get_words()
        return self.min_length_words(all_words)
    
    
    def __str__(self) -> str:
        return f"Text(id={self.id}, sentences={self.sentence_count()}, chars={len(self._content)})"
    
    def __repr__(self) -> str:
        return f"Text('{self._content[:50]}...')"
    
    def __len__(self) -> int:
        return len(self._content)
    
    @classmethod
    def get_instance_count(cls) -> int:
        return cls._instance_count