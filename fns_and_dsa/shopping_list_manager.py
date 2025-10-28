# Python script for managing a shopping list.

# Loop menu to get user input for actions.
def display_menu():
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Exit")

# Function to add an items, remove items, and diplay current list of items on shopping list.
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            shopping_list.remove(item)
        elif choice == '3':
            print("Current Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()