"""
Main program for Laboratory Work No. 4.
Allows to choose which task to run.
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

def menu():
    print("=== LABORATORY WORK №4 ===\n")
    print("Select task to execute:")
    print("1. Task 1 (Competition score table, variant 6)")
    print("2. Task 2 (Text analysis with regex, variant 6)")
    print("3. Task 3 (Series, plots)")
    print("4. Task 4 (Geometric figures)")
    print("5. Task 5 (NumPy)")
    print("6. Task 6 (Pandas)")
    print("0. Exit")

    
def main():

    while(True):
        menu();
        choice = input("\nYour choice: ").strip()
        if choice == "1":
            from Task_1.task1_main import run
            run()
        elif choice == "2":
            from Task_2.task2_main import run
            run()
        elif choice == "3":
            from Task_3.task3_main import run
            run()
        elif choice == "4":
            from Task_4.task4_main import run
            run()
        elif choice == "5":
            from Task_5.task5_main import run
            run()
        elif choice == "6":
            from Task_6.task6_main import run
            run()
        elif choice == "0":
            return
        else:
            print("Invalid choice. Please run again.")

if __name__ == "__main__":
    main()