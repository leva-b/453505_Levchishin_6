"""
File and archive utilities for Task 2.
Lab 4, Task 2, Variant 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

import os
import zipfile
from datetime import datetime
from typing import List

TASK2_ROOT = os.path.dirname(__file__)
DATA_DIR = os.path.join(TASK2_ROOT, "data")
OUTPUT_DIR = os.path.join(DATA_DIR, "output")
DEFAULT_INPUT_FILE = os.path.join(DATA_DIR, "input.txt")
RESULTS_FILE = os.path.join(OUTPUT_DIR, "analysis_results.txt")
ZIP_FILE = os.path.join(OUTPUT_DIR, "results_archive.zip")

def ensure_dir(path: str):
    """Create directory if not exists."""
    if not os.path.exists(path):
        os.makedirs(path)

def read_text_file(filepath: str) -> str:
    """Read text from file (UTF-8). Raises FileNotFoundError."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_result_file(filepath: str, results: List[str]) -> None:
    """Write list of result strings to a file."""
    ensure_dir(os.path.dirname(filepath))
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(results))

def create_zip_archive(source_file: str, archive_name: str) -> str:
    """Create zip archive containing source_file. Returns archive path."""
    ensure_dir(os.path.dirname(archive_name))
    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(source_file, arcname=os.path.basename(source_file))
    return archive_name

def get_archive_info(zip_path: str) -> str:
    """Return formatted info about zip file: name, size, modification time."""
    if not os.path.exists(zip_path):
        return "Archive not found."
    with zipfile.ZipFile(zip_path, 'r') as zf:
        info = zf.infolist()[0]  # only one file expected
        return (f"Archive: {os.path.basename(zip_path)}\n"
                f"File inside: {info.filename}\n"
                f"Compressed size: {info.compress_size} bytes\n"
                f"Original size: {info.file_size} bytes\n"
                f"Compression ratio: {info.compress_size/info.file_size:.2%}\n"
                f"Modified: {datetime(*info.date_time)}")

def safe_file_operation(func, *args, **kwargs):
    """Generic safe file operation with exception handling."""
    try:
        return func(*args, **kwargs)
    except FileNotFoundError as e:
        print(f"File error: {e}. Please check input file.")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None