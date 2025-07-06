import os

# Step 1: Load favorites from file if it exists, otherwise use a default dictionary
filename = "favorites.txt"

def load_favorites():
    favorites = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                # Skip empty lines and strip extra whitespace
                line = line.strip()
                if line:
                    # Split by the first colon and save key-value pair
                    category, favorite = line.split(":", 1)
                    favorites[category.strip()] = favorite.strip()
    else:
        # Default favorites if no file exists
        favorites = {
            "color": "blue",
            "food": "pizza",
            "movie": "Interstellar"
        }
    return favorites

def save_favorites(favorites):
    with open(filename, "w") as f:
        for category, favorite in favorites.items():
            f.write(f"{category}: {favorite}\n")

# Step 2: Load the favorites dictionary from file
favorites = load_favorites()

# Step 3: Main loop for continuous interaction
while True:
    # Step 3.1: Display available categories
    print("\nYour favorite categories are:", ", ".join(favorites.keys()))

    # Step 3.2: Ask the user what action they want to perform
    action = input("\nChoose an action: (1) View, (2) Update, (3) Add, (4) Delete, (5) Quit: ")

    if action == "1":
        # View a category
        category = input("Which category would you like to see? ")
        if category in favorites:
            print(f"My favorite {category} is {favorites[category]}!")
        else:
            print(f"Sorry, the category '{category}' is not available.")
    
    elif action == "2":
        # Update an existing category
        category = input("Which category would you like to update? ")
        if category in favorites:
            new_favorite = input(f"Enter your new favorite for {category}: ")
            favorites[category] = new_favorite
            print(f"{category} updated to {new_favorite}!")
        else:
            print(f"Sorry, the category '{category}' does not exist.")
    
    elif action == "3":
        # Add a new category
        new_category = input("Enter new category: ")
        new_favorite = input(f"Enter your favorite for {new_category}: ")
        favorites[new_category] = new_favorite
        print(f"{new_category} added with favorite {new_favorite}!")

    elif action == "4":
        # Delete an existing category
        category = input("Which category would you like to delete? ")
        if category in favorites:
            del favorites[category]
            print(f"{category} has been deleted.")
        else:
            print(f"Sorry, the category '{category}' does not exist.")
    
    elif action == "5":
        # Quit the program
        save_favorites(favorites)  # Save changes to file before quitting
        print("All changes saved. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid action.")

    # Save the dictionary to the file after every operation
    save_favorites(favorites)

    # Ask if the user wants to perform another action
    continue_action = input("\nWould you like to perform another action? (yes/no): ").lower()
    if continue_action != "yes":
        save_favorites(favorites)  # Save before quitting the loop
        print("Goodbye!")
        break
