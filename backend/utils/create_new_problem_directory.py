import os

def create_problem_directory(problem_id):
    base_dir = f".././problems/{problem_id}"
    
    
    # Paths for the subdirectories and files
    dirs_to_create = [
        f"{base_dir}/statement",
        f"{base_dir}/problem_name",
        f"{base_dir}/testcases/hidden",
        f"{base_dir}/testcases/visible/1",
        f"{base_dir}/testcases/visible/2"
    ]
    
    files_to_create = {
        f"{base_dir}/statement/statement.txt": "Problem statement goes here.",
        f"{base_dir}/problem_name/problem_name.txt": "Problem name goes here.",
        f"{base_dir}/testcases/visible/1/input.txt": "Visible input test case 1.",
        f"{base_dir}/testcases/visible/1/expected_output.txt": "Visible output test case 1.",
        f"{base_dir}/testcases/visible/1/explanation.txt": "Explanation for visible test case 1.",
        f"{base_dir}/testcases/visible/2/input.txt": "Visible input test case 2.",
        f"{base_dir}/testcases/visible/2/expected_output.txt": "Visible output test case 2.",
        f"{base_dir}/testcases/visible/2/explanation.txt": "Explanation for visible test case 2."
    }
    
    # Create directories
    for directory in dirs_to_create:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create files and add default content
    for file_path, content in files_to_create.items():
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Created file: {file_path} with content: {content}")

if __name__ == "__main__":
    problem_id = input("Enter the problem ID: ").strip()
    create_problem_directory(problem_id)
