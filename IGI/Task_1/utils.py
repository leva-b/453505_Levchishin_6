"""
Helper functions: safe input, menu, data display, file handling.
Lab 4, Task 1, Variant 6.
Version: 1.0
Developer: Ivan Leuchyshyn
Date: 2026-04-23
"""

import os
from .serializers import CSVSerializer, PickleSerializer
from .models import Team, TeamTable

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CSV_PATH = os.path.join(DATA_DIR, "teams.csv")
PKL_PATH = os.path.join(DATA_DIR, "teams.pkl")


def ensure_data_dir():
    """Create data directory if it doesn't exist."""
    if not os.path.exists(DATA_DIR):      
        os.makedirs(DATA_DIR)


def safe_int_input(prompt: str, min_val: int = 0) -> int:   
    """Read integer with validation, loop until correct."""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Input cannot be empty")
            num = int(value)
            if num < min_val:
                print(f"Value must be >= {min_val}. Try again.")
                continue
            return num
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter an integer.")


def safe_string_input(prompt: str, allow_empty: bool = False) -> str:
    """Read non-empty string (unless allowed)."""
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("Input cannot be empty. Please try again.")


def display_teams(table: TeamTable):
    """Print all teams in a formatted table."""
    teams = table.get_all_teams()
    if not teams:
        print("No teams in the table.\n")
        return
    print("\n" + "=" * 40)
    print(f"{'#':<3} {'Team name':<20} {'Points':<10}")
    print("-" * 40)
    for idx, team in enumerate(teams, start=1):
        print(f"{idx:<3} {team.name:<20} {team.points:<10}")
    print("=" * 40 + "\n")


def save_data(table: TeamTable, use_csv: bool):
    """Save table to selected format."""
    ensure_data_dir()
    data = table.to_dict_list()
    if use_csv:
        CSVSerializer.save(data, CSV_PATH)
        print(f"Data saved to {CSV_PATH}")
    else:
        PickleSerializer.save(data, PKL_PATH)
        print(f"Data saved to {PKL_PATH}")


def load_data(use_csv: bool) -> TeamTable:
    """Load table from selected format. Returns empty table if file missing."""
    ensure_data_dir()
    if use_csv:
        data = CSVSerializer.load(CSV_PATH)
    else:
        data = PickleSerializer.load(PKL_PATH)

    if not data:
        print("No existing data found. Starting with empty table.")
        return TeamTable()

    return TeamTable.from_dict_list(data)


def choose_format() -> bool:
    """Ask user to choose CSV (True) or pickle (False). Return choice."""
    while True:
        ch = input("Choose storage format (1 = CSV, 2 = pickle): ").strip()
        if ch == "1":
            return True
        if ch == "2":
            return False
        print("Please enter 1 or 2.")