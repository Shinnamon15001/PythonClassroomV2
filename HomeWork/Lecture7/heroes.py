import pickle

heroes = []

def display_heroes():
    if not heroes:
        print("No heroes to display.")
    else:
        print("Heroes:")
        for hero in heroes:
            print(hero)

def add_hero():
    hero_name = input("Enter the name of the hero to add: ")
    heroes.append(hero_name)
    print(f"{hero_name} has been added to the list.")
    save_to_file()

def insert_hero():
    index = int(input("Enter the position to insert the hero: "))
    hero_name = input("Enter the name of the hero to insert: ")
    heroes.insert(index, hero_name)
    print(f"{hero_name} has been inserted at position {index}.")
    save_to_file()

def remove_hero():
    if not heroes:
        print("No heroes to remove.")
    else:
        hero_name = input("Enter the name of the hero to remove: ")
        if hero_name in heroes:
            heroes.remove(hero_name)
            print(f"{hero_name} has been removed from the list.")
            save_to_file()
        else:
            print(f"{hero_name} not found in the list.")

def display_sorted_heroes():
    if not heroes:
        print("No heroes to display.")
    else:
        sort_order = input("Enter 'asc' for ascending or 'desc' for descending order: ").lower()
        sorted_heroes = sorted(heroes, reverse=(sort_order == 'desc'))
        print(f"Sorted Heroes ({sort_order}ending):")
        for hero in sorted_heroes:
            print(hero)

def save_to_file():
    with open("heroes.pkl", 'wb') as file:
        pickle.dump(heroes, file)
    print("Heroes have been saved to 'heroes.pkl'.")

def load_from_file():
    global heroes
    try:
        with open("heroes.pkl", 'rb') as file:
            heroes = pickle.load(file)
        print("Heroes have been loaded from 'heroes.pkl'.")
    except FileNotFoundError:
        print("File 'heroes.pkl' not found. Starting with an empty list of heroes.")
        heroes = []

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
