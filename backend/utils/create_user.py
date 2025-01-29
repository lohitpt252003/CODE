import os
import json

def get_next_user_id(users_dir):
    """Find the smallest missing user ID using binary search."""
    user_files = sorted([int(f[4:-5]) for f in os.listdir(users_dir) if f.startswith("user") and f.endswith(".json")])

    # Edge case: No users exist
    if not user_files:
        return 1

    # Binary search to find the missing ID
    low, high = 0, len(user_files) - 1
    while low <= high:
        mid = (low + high) // 2
        if user_files[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1

    return low + 1  # First missing user ID

def create_user():
    users_dir = '../users'
    if not os.path.exists(users_dir):
        os.makedirs(users_dir)

    user_id = get_next_user_id(users_dir)
    user_file = os.path.join(users_dir, f'user{user_id}.json')

    user_data = {
        "id": user_id,
        "username": f"user{user_id}",
        "email": f"user{user_id}@example.com",
        "solved_problems": [],
        "contests_joined": []
    }

    with open(user_file, 'w') as file:
        json.dump(user_data, file, indent=4)

    print(f"User with ID {user_id} created successfully.")

if __name__ == '__main__':
    create_user()
