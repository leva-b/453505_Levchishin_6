"""
Main execution for Task 2 (Variant 6).
Lab 4, Task 2.
Developer: Ivan Leuchyshyn
Date: 2026-04-27
"""

import os
from .text_analyzer import Text   # Исправлено: было text_anilyzer
from .utils import (
    read_text_file, write_result_file, create_zip_archive,
    get_archive_info, safe_file_operation, ensure_dir,
    DATA_DIR, OUTPUT_DIR, DEFAULT_INPUT_FILE, RESULTS_FILE, ZIP_FILE
)

def format_results(text_obj: Text) -> list:
    """Generate list of result strings for the given Text object."""
    lines = []
    lines.append("=" * 60)
    lines.append("TEXT ANALYSIS RESULTS (Variant 6)")
    lines.append("=" * 60)
    
    lines.append(f"\n1. Number of sentences: {text_obj.sentence_count()}")
    sent_types = text_obj.sentence_types()
    lines.append(f"   - Declarative (.) : {sent_types['declarative']}")
    lines.append(f"   - Interrogative (?) : {sent_types['interrogative']}")
    lines.append(f"   - Imperative (!) : {sent_types['imperative']}")
    lines.append(f"\n2. Average sentence length (characters, words only): {text_obj.avg_sentence_length_chars():.2f}")
    lines.append(f"3. Average word length: {text_obj.avg_word_length():.2f}")
    lines.append(f"4. Number of smileys: {text_obj.count_smileys()}")
    
    lines.append("\n--- VARIANT 6 SPECIFIC ---")
    upper_words = text_obj.words_uppercase_with_digits()
    lines.append(f"5. Words starting with capital letter and containing digits ({len(upper_words)}):")
    lines.append("   " + ", ".join(upper_words) if upper_words else "   None")
    
    min_len, min_words = text_obj.min_length_words_info()
    lines.append(f"\n6. Minimum word length: {min_len}")
    lines.append(f"   Words with that length ({len(min_words)}): {', '.join(min_words) if min_words else 'none'}")
    
    dot_words = text_obj.words_followed_by_dot()
    lines.append(f"\n7. Words followed by a dot ({len(dot_words)}):")
    lines.append("   " + ", ".join(dot_words) if dot_words else "   None")
    
    longest_r = text_obj.longest_word_ending_r()
    lines.append(f"\n8. Longest word ending with 'r': '{longest_r}'" if longest_r else "   No word ending with 'r' found.")
    
    return lines

def run():
    """Entry point for Task 2."""
    print("\n=== TASK 2: TEXT ANALYSIS (Variant 6) ===\n")
    
    ensure_dir(DATA_DIR)
    ensure_dir(OUTPUT_DIR)
    
    input_path = DEFAULT_INPUT_FILE
    
    if not os.path.exists(input_path):
        print(f"Input file not found at {input_path}")
        print("Creating a sample input.txt file with test data...")
        
        sample_content = get_sample_text()
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(sample_content)
        print(f"Sample file created at {input_path}\n")
    
    content = safe_file_operation(read_text_file, input_path)
    if content is None:
        print("Exiting Task 2.")
        return
    
    print(f"Analyzing file: {input_path}\n")
    
    text = Text(content)
    
    result_lines = format_results(text)
    for line in result_lines:
        print(line)
    
    print("\n--- HTML Color Check ---")
    color_str = input("Enter a string to test if it's a valid HTML hex color (e.g., #FFFFFF): ").strip()
    from .regex_utils import RegexPatterns
    is_valid = RegexPatterns.is_html_color(color_str)
    print(f"'{color_str}' is {'a valid' if is_valid else 'NOT a valid'} HTML color code.\n")
    result_lines.append(f"\n9. HTML color check: '{color_str}' -> {'valid' if is_valid else 'invalid'}")
    
    write_result_file(RESULTS_FILE, result_lines)
    print(f"\nResults saved to: {RESULTS_FILE}")
    
    zip_path = create_zip_archive(RESULTS_FILE, ZIP_FILE)
    print(f"Results archived to: {zip_path}")
    
    archive_info = get_archive_info(zip_path)
    print("\n--- Archive information ---")
    print(archive_info)
    
    while True:
        again = input("\nDo you want to analyze another text file? (y/n): ").strip().lower()
        if again == 'y':
            custom_path = input(f"Enter file path (or press Enter to use {DEFAULT_INPUT_FILE}): ").strip()
            if custom_path:
                content = safe_file_operation(read_text_file, custom_path)
                if content is None:
                    print("Failed to read custom file. Using default.")
                else:
                    text = Text(content)
                    result_lines = format_results(text)
                    for line in result_lines:
                        print(line)
                    write_result_file(RESULTS_FILE, result_lines)
                    print(f"\nResults saved to: {RESULTS_FILE}")
                    continue
            run()
            return
        elif again == 'n':
            print("Exiting Task 2.")
            return
        else:
            print("Please answer y or n.")

def get_sample_text() -> str:
    """Return sample text for testing variant 6."""
    return """Hello World! This is a sample text for testing the text analysis program. 
Are you ready to test all features? Yes, let's begin immediately!
Check these special words: Windows10, MacOS12, Linux, Python3.9, DataScience2024.
Some words that end with letter R: car, mirror, driver, computer, processor.
Words followed by dot: Important. Example. Another one.
Smileys test: :-) ;-) :---))) ;[[[[ :)) ;]]] 
HTML colors: #FFFFFF (white), #FF0000 (red), #00FF00 (green), #0000FF (blue), #123ABC, #F50.
The minimum length word is 'a' or 'I'. The longest word ending with r is 'processor'.
What about questions? How many are here? Also exclamations! Wow! Amazing!
Make sure to test punctuation: dots, commas, exclamation marks!
"""