# Create a dictionary with at least 3 categories and values
favorites = {
    "color": "blue",
    "food": "pizza",
    "movie": "Interstellar"
}

# Display the available categories to the user
print("Your favorite categories are:", ", ".join(favorites.keys()))

# Ask the user for a category
category = input("Which category would you like to see? ")

# Check if the category exists and display the favorite, or notify if it's not available
if category in favorites:
    print(f"My favorite {category} is {favorites[category]}!")
else:
    print(f"Sorry, the category '{category}' is not available.")

# Ask if the user wants to add a new favorite category
add_new = input("Would you like to add a new favorite category? (yes/no) ").lower()

if add_new == "yes":
    new_category = input("Enter new category: ")
    new_favorite = input(f"Enter your favorite for {new_category}: ")
    
    # Add the new category and favorite to the dictionary
    favorites[new_category] = new_favorite

# Print the entire updated dictionary
print("\nHere are all your favorites:")
for category, favorite in favorites.items():
    print(f"{category}: {favorite}")
