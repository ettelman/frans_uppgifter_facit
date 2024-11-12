"""
Inköpslista
Skapa ett program som hanterar en inköpslista. Programmet ska kunna:

Lägga till, ta bort och visa alla varor till inköpslistan.
Spara inköpslistan till en textfil (användaren får välja filnamn).

Krav:

Programmet ska ha en meny där användaren kan välja att visa listan, lägga till varor, ta bort varor, spara listan eller avsluta.
Använd funktioner för att hantera menyval.
"""

def add_item(shopping_list):
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"{item} was added to shopping list")

def display_list(shopping_list):
    if shopping_list:
        print("Shopping list:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Shopping list is empty")

def remove_item(shopping_list):
    display_list(shopping_list)
    if shopping_list:
        item_number = input("Enter the number to remove: ")
        if item_number.isdigit() and 1 <= int(item_number) <= len(shopping_list):
            removed_item = shopping_list.pop(int(item_number) - 1)
            print(f"{removed_item} has been removed")
        else:
            print("Invalid item number")

def save_list(shopping_list):
    if shopping_list:
        filename = input("Enter filename: ")
        with open(filename, "w") as file:
            for item in shopping_list:
                file.write(item + "\n")
        print(f"Shopping list has been saved to: {filename}")
    else:
        print("List is empty!")

def main():
    shopping_list = []

    while True:
        print("\nMenu:")
        print("1. Add an item")
        print("2. Display shopping list")
        print("3. Remove item")
        print("4. Save as file")
        print("5. Exit")
        choice = input("Chose an option: ")

        if choice == "1":
            add_item(shopping_list)
        if choice == "2":
            display_list(shopping_list)
        if choice == "3":
            remove_item(shopping_list)
        if choice == "4":
            save_list(shopping_list)
        if choice == "5":
            break

main()