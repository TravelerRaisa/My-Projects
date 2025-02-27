print("Welcome Glossary List Manager")
grocery_list = []
while True:
         print("\nGrocery List Manager Menu: ")
         print("1. Add an item to the grocery list")
         print("2. Remove an item from the grocery  list")
         print("3. View the grocery  list")
         print("4. Check if an item is already in the grocery  list")
         print("5. Exit")
         choice = input("Enter your choice (1-5): ")
         if choice == "1":
            item = input("Enter the item to add: ")
            grocery_list.append(item)
            print(f"{item}, it's in the grocery list.")
         elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in grocery_list:
               grocery_list.remove(item)
               print(f"{item} has been removed from the grocery list.")
            else:
                print(f"{item} is not in the grocery list.")
         elif choice == "3":
            if grocery_list:
                print("Your grocery list:")
            for i, item in enumerate(grocery_list, start=1):
                print(f"{i}. {item}")
            else:
                print("Your grocery list is empty.")
         elif choice == "4":
            item = input("Enter the item to check: ")
            if item in grocery_list:
                 print(f"{item} is already in the grocery list.")
            else:
                 print(f"{item} is not in the grocery list.")
         elif choice=="5":
            print("Goodbye! Have a great day.")