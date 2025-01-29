import os
import random

import string
def generate_random_string():
    length = random.randint(1, 50)  # Random length between 1 and 50
    letters = string.ascii_letters + string.digits  # Letters and digits
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_hidden_testcases(problem_id, hidden_count):
    # Go back to the parent directory to access the 'problems' folder
    base_dir = os.path.join(os.path.dirname(__file__), "../problems", str(problem_id), "testcases")

    # Generating hidden test cases
    hidden_dir = os.path.join(base_dir, "hidden")
    os.makedirs(hidden_dir, exist_ok=True)

    for i in range(1, hidden_count + 1):
        input_file = os.path.join(hidden_dir, f"input{i}.txt")
        output_file = os.path.join(hidden_dir, f"expected_output{i}.txt")

        # Generate random test case input
        # n = random.randint(1, 100)  # Random number between 1 and 100
        # y = random.randint(1, 100)  # Random number between 1 and 100
        x = generate_random_string()  # Random string
        # arr = []
        # for i in range(n):
        #     arr.append(random.randint(1, 100))
        with open(input_file, "w") as infile:
            infile.write(f"{x}\n")
        # with open(input_file, "a") as infile:
        #     infile.write(f"{arr}\n")
        # a = 'abc'
        # Compute expected output (for example, x * x)
        with open(output_file, "w") as outfile:
            outfile.write(f"{x[::-1]}\n")

        print(f"Generated hidden test case {i}: {input_file} and {output_file}")

if __name__ == "__main__":
    problem_id = input("Enter Problem ID: ").strip()
    hidden_count = int(input("Enter number of hidden test cases: ").strip())

    generate_hidden_testcases(problem_id, hidden_count)
