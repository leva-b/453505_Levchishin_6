"""
Main logic for Task 1 (variant 6).
Called from the global main.py.
Lab 4, Task 1, Variant 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-23
"""

from .utils import (
    safe_int_input, safe_string_input, display_teams,
    save_data, load_data, choose_format
)
from .models import Team, TeamTable


def add_team_interactive(table: TeamTable):
    print("\n--- Add new team ---")
    name = safe_string_input("Team name: ")
    if table.find_team(name):
        print(f"Team '{name}' already exists.")
        return
    points = safe_int_input("Points (0 or more): ", min_val=0)
    team = Team(name, points)
    table.add_team(team)
    print(f"Team '{name}' added with {points} points.")

def edit_team_interactive(table: TeamTable):
    print("\n--- Edit team points ---")
    name = safe_string_input("Enter team name to edit: ")
    team = table.find_team(name)
    if not team:
        print(f"Team '{name}' not found.")
        return
    print(f"Current points: {team.points}")
    new_points = safe_int_input("New points: ", min_val=0)
    team.points = new_points
    print("Points updated.")

def remove_team_interactive(table: TeamTable):
    print("\n--- Remove team ---")
    name = safe_string_input("Enter team name to remove: ")
    if table.remove_team(name):
        print(f"Team '{name}' removed.")
    else:
        print(f"Team '{name}' not found.")

def show_first_place(table: TeamTable):
    first = table.get_first_place()
    if not first:
        print("No teams.")
        return
    if len(first) == 1:
        print(f"\n🏆 First place: {first[0].name} with {first[0].points} pts.")
    else:
        names = ", ".join(t.name for t in first)
        print(f"\n🏆 Tie: {names} ({first[0].points} pts each).")

def show_sorted_table(table: TeamTable):
    sorted_teams = table.get_sorted_by_rank()
    if not sorted_teams:
        print("No teams.")
        return
    print("\n===== SORTED BY RANK =====")
    for rank, team in enumerate(sorted_teams, start=1):
        print(f"{rank}. {team.name} — {team.points} pts")
    print()

def search_team(table: TeamTable):
    name = safe_string_input("Enter team name to search: ")
    team = table.find_team(name)
    if team:
        print(f"\n✅ Found: {team}")
    else:
        print(f"❌ Team '{name}' not found.")

def run():
    """Entry point for Task 1."""
    print("\n=== TASK 1: COMPETITION SCORE TABLE (Variant 6) ===\n")
    use_csv = choose_format()
    table = load_data(use_csv)

    while True:
        print("\n" + "-" * 50)
        print("MENU:")
        print("1. Show all teams")
        print("2. Add team")
        print("3. Edit team points")
        print("4. Remove team")
        print("5. Show first place team(s)")
        print("6. Show sorted table by rank")
        print("7. Search team by name")
        print("8. Save and exit")
        print("9. Exit without saving")
        print("-" * 50)

        choice = safe_string_input("Your choice (1-9): ", allow_empty=False)

        if choice == "1":
            display_teams(table)
        elif choice == "2":
            add_team_interactive(table)
        elif choice == "3":
            edit_team_interactive(table)
        elif choice == "4":
            remove_team_interactive(table)
        elif choice == "5":
            show_first_place(table)
        elif choice == "6":
            show_sorted_table(table)
        elif choice == "7":
            search_team(table)
        elif choice == "8":
            save_data(table, use_csv)
            print("Data saved. Exiting Task 1.")
            return
        elif choice == "9":
            print("Exiting without saving.")
            return
        else:
            print("Invalid choice.")