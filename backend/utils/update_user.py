import os
import json

def update_user(user_id, updates):
    """
    Updates a user's data in the JSON file.

    Args:
        user_id (int): The ID of the user to update.
        updates (dict): A dictionary containing the fields to update and their new values.
                       Example: {"username": "new_username", "email": "new_email@example.com"}
    """
    # Define the path to the users folder and the user file
    users_dir = f'../users'
    user_file = os.path.join(users_dir, f'user{user_id}.json')

    # Check if the user file exists
    if not os.path.exists(user_file):
        print(f"User with ID {user_id} does not exist.")
        return

    # Load the existing user data
    with open(user_file, 'r') as file:
        user_data = json.load(file)

    # Update the user data with the provided updates
    user_data.update(updates)

    # Save the updated user data back to the JSON file
    with open(user_file, 'w') as file:
        json.dump(user_data, file, indent=4)

    print(f"User with ID {user_id} updated successfully.")

def get_user_input():
    """
    Takes input from the user for updating a user's data.
    """
    # Get the user ID to update
    user_id = input("Enter the user ID to update: ")

    # Initialize an empty dictionary to store updates
    updates = {}

    # Prompt the user for fields to update
    print("Enter the fields you want to update. Leave the field blank and press Enter to finish.")
    while True:
        field = input("Enter the field name (e.g., username, email): ").strip()
        if not field:
            break
        value = input(f"Enter the new value for '{field}': ").strip()
        updates[field] = value

    return user_id, updates

# Main program
if __name__ == "__main__":
    user_id, updates = get_user_input()
    update_user(user_id, updates)