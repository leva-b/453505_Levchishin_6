# modules/advanced_text_module.py
"""
Module: advanced_text_module.py
Description: Task 4 - Advanced text analysis with predefined string
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""

from typing import List, Dict, Any
import math


# Predefined text for Task 4
PREDEFINED_TEXT = (
    "So she was considering in her own mind, as well as she could, for the "
    "hot day made her feel very sleepy and stupid, whether the pleasure of "
    "making a daisy-chain would be worth the trouble of getting up and "
    "picking the daisies, when suddenly a White Rabbit with pink eyes ran "
    "close by her."
)


def get_words(text: str) -> List[str]:
    """
    Split text into words (remove punctuation).
    
    Args:
        text: Input string
    
    Returns:
        List of words in lowercase
    """
    # Replace punctuation with spaces
    for punct in ",.!?;:":
        text = text.replace(punct, ' ')
    # Split and filter out empty strings
    return [word for word in text.lower().split() if word]


def is_vowel(char: str) -> bool:
    """
    Check if a character is a vowel (English vowels).
    
    Args:
        char: Single character
    
    Returns:
        True if character is a vowel, False otherwise
    """
    vowels = 'aeiouy'
    return char.lower() in vowels


def count_words_ending_with_vowel(words: List[str]) -> int:
    """
    Count words that end with a vowel.
    
    Args:
        words: List of words
    
    Returns:
        Number of words ending with a vowel
    """
    count = 0
    vowel_words = []
    
    for word in words:
        if word and is_vowel(word[-1]):
            count += 1
            vowel_words.append(word)
    
    return count, vowel_words


def get_average_word_length(words: List[str]) -> float:
    """
    Calculate average word length.
    
    Args:
        words: List of words
    
    Returns:
        Average length of words
    """
    if not words:
        return 0.0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def find_words_with_length(words: List[str], target_length: int) -> List[str]:
    """
    Find all words with specific length.
    
    Args:
        words: List of words
        target_length: Desired word length
    
    Returns:
        List of words with target length
    """
    return [word for word in words if len(word) == target_length]


def get_every_nth_word(words: List[str], n: int) -> List[str]:
    """
    Get every n-th word (1-indexed).
    
    Args:
        words: List of words
        n: Step (e.g., 5 for every 5th word)
    
    Returns:
        List of every n-th word
    """
    # n-th word means indices n-1, 2n-1, 3n-1, ...
    return [words[i] for i in range(n - 1, len(words), n)]


def analyze_advanced_text() -> Dict[str, Any]:
    """
    Analyze predefined text according to variant.
    
    Args:
        variant: Task variant number
    
    Returns:
        Dictionary with analysis results
    """
    words = get_words(PREDEFINED_TEXT)
    
    # a) Count words ending with vowel
    vowel_count, vowel_words = count_words_ending_with_vowel(words)
    
    # b) Calculate average word length and round to integer
    avg_length = get_average_word_length(words)
    rounded_avg = round(avg_length)
    
    # Find words with average length
    words_with_avg_length = find_words_with_length(words, rounded_avg)
    
    # c) Get every 5th word
    every_fifth_word = get_every_nth_word(words, 5)
    
    # Build result description
    description = f"\n--- RESULTS (Variant 6) ---\n"
    description += f"\na) Words ending with a vowel:\n"
    description += f"   Count: {vowel_count} out of {len(words)} words\n"
    if vowel_words:
        description += f"   Words: {', '.join(vowel_words[:20])}"
        if len(vowel_words) > 20:
            description += f" ... and {len(vowel_words) - 20} more"
        description += "\n"
    
    description += f"\nb) Average word length:\n"
    description += f"   Average: {avg_length:.2f}\n"
    description += f"   Rounded to integer: {rounded_avg}\n"
    
    if words_with_avg_length:
        description += f"   Words with length {rounded_avg} ({len(words_with_avg_length)} words):\n"
        description += f"   {', '.join(words_with_avg_length)}\n"
    else:
        description += f"   Слов длиной {rounded_avg} символов в строке нет\n"
    
    description += f"\nc) Every 5th word ({len(every_fifth_word)} words):\n"
    if every_fifth_word:
        for i, word in enumerate(every_fifth_word, 1):
            position = i * 5
            description += f"   {position}. {word}\n"
    
    return {
        'word_count': len(words),
        'vowel_ending_count': vowel_count,
        'vowel_words': vowel_words,
        'average_length': avg_length,
        'rounded_average': rounded_avg,
        'words_with_avg_length': words_with_avg_length,
        'every_fifth_word': every_fifth_word,
        'description': description
    }
    