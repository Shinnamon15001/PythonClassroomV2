heroes = []

def display_heroes():
    if not heroes:
        print("No heroes to display.")
    else:
        print("Heroes:")
        for index, hero in enumerate(heroes, start=1):
            print(f"- {hero}")

def add_hero():
    hero_names = input("Enter the names of the heroes to add (separated by spaces): ").split()
    heroes.extend(hero_names)
    print(f"{', '.join(hero_names)} have been added to the list.")
    save_to_file()

def insert_hero():
    index = int(input("Enter the position to insert the heroes: ")) - 1
    hero_names = input("Enter the names of the heroes to insert (separated by spaces): ").split()
    heroes[index:index] = hero_names
    print(f"{', '.join(hero_names)} have been inserted at position {index + 1}.")
    save_to_file()

def remove_hero():
    if not heroes:
        print("No heroes to remove.")
    else:
        display_heroes()
        hero_to_remove = input("Enter the name of the hero to remove: ")
        if hero_to_remove in heroes:
            heroes.remove(hero_to_remove)
            print(f"{hero_to_remove} has been removed from the list.")
            save_to_file()
        else:
            print(f"{hero_to_remove} not found in the list.")

def display_sorted_heroes():
    if not heroes:
        print("No heroes to display.")
    else:
        sort_order = input("Enter 'asc' for ascending or 'desc' for descending order: ").lower()
        sorted_heroes = sorted(heroes, reverse=(sort_order == 'desc'))
        print(f"Sorted Heroes ({sort_order}ending):")
        for hero in sorted_heroes:
            print(f"- {hero}")

def save_to_file():
    with open("heroes.txt", 'w') as file:
        for hero in heroes:
            file.write(hero + '\n')
    print("Heroes have been saved to 'heroes.txt'.")

def load_from_file():
    global heroes
    try:
        with open("heroes.txt", 'r') as file:
            heroes = [line.strip() for line in file]
        print("Heroes have been loaded from 'heroes.txt'.")
    except FileNotFoundError:
        print("File 'heroes.txt' not found. Starting with an empty list of heroes.")
        heroes = []

# Load heroes from file at the beginning
load_from_file()

while True:
    print("\n1. Display Heroes\n2. Add Heroes\n3. Insert Heroes\n4. Remove Heroes\n5. Display Sorted Heroes\n6. Quit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_heroes()
    elif choice == '2':
        add_hero()
    elif choice == '3':
        insert_hero()
    elif choice == '4':
        remove_hero()
    elif choice == '5':
        display_sorted_heroes()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
