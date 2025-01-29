from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app, origins='*')

def get_visible_testcases(id):
    visible_testcases = []
    dir_path = f'./problems/{id}'
    testcases_dir = f'{dir_path}/testcases'
    
    visible_cases_dir = f'{testcases_dir}/visible'
    if os.path.isdir(visible_cases_dir):
        # List the directories inside the visible testcases directory
        visible_case_dirs = [
            d for d in os.listdir(visible_cases_dir) if os.path.isdir(os.path.join(visible_cases_dir, d))
        ]
        
        for case_dir in visible_case_dirs:
            explanation_file = f'{visible_cases_dir}/{case_dir}/explanation.txt'
            input_file = f'{visible_cases_dir}/{case_dir}/input.txt'
            output_file = f'{visible_cases_dir}/{case_dir}/expected_output.txt'
            
            # Check if the necessary files exist
            if os.path.exists(explanation_file) and os.path.exists(input_file) and os.path.exists(output_file):
                with open(explanation_file, 'r') as exp_file:
                    explanation_content = exp_file.read()
                with open(input_file, 'r') as in_file:
                    input_content = in_file.read()
                with open(output_file, 'r') as out_file:
                    output_content = out_file.read()
                
                visible_testcases.append({
                    "explanation": explanation_content,
                    "input": input_content,
                    "expected_output": output_content
                })
    return visible_testcases
    
def get_hidden_testcases(id):
    hidden_testcases = []
    dir_path = f'./problems/{id}'
    testcases_dir = f'{dir_path}/testcases'
    
    hidden_cases_dir = f'{testcases_dir}/hidden'
    if os.path.isdir(hidden_cases_dir):
        hidden_inputs = sorted([f for f in os.listdir(hidden_cases_dir) if f.startswith('input') and f.endswith('.txt')])
        hidden_outputs = sorted([f for f in os.listdir(hidden_cases_dir) if f.startswith('expected_output') and f.endswith('.txt')])

        # Check if the number of input and output files match
        if len(hidden_inputs) == len(hidden_outputs):
            for i in range(len(hidden_inputs)):
                hidden_input_file = os.path.join(hidden_cases_dir, hidden_inputs[i])
                hidden_output_file = os.path.join(hidden_cases_dir, hidden_outputs[i])
                
                # Read the content of the hidden input and output files
                with open(hidden_input_file, 'r') as in_file:
                    hidden_input_content = in_file.read()
                with open(hidden_output_file, 'r') as out_file:
                    hidden_output_content = out_file.read()
                
                hidden_testcases.append({
                    "input": hidden_input_content,
                    "expected_output": hidden_output_content
                })
    return hidden_testcases

def get_statement(id):
    dir_path = f'./problems/{id}'
    statement_path = f'{dir_path}/statement/statement.txt'
    
    # Check if the statement file exists
    if not os.path.exists(statement_path):
        return None  # Return None if the statement file doesn't exist
    
    # Read and return the content of the statement file
    with open(statement_path, 'r') as file:
        return file.read()

def get_problem_name(id):
    dir_path = f'./problems/{id}'
    problem_name_path = f'{dir_path}/problem_name/problem_name.txt'
    
    # Check if the statement file exists
    if not os.path.exists(problem_name_path):
        return None  # Return None if the statement file doesn't exist
    
    # Read and return the content of the statement file
    with open(problem_name_path, 'r') as file:
        return file.read()
# Route for testing
@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})

# Get problem details
@app.route('/problems/<int:id>', methods=['GET'])
def get_problem(id):
    # Fetch the problem statement
    statement = get_statement(id)
    if not statement:
        return jsonify({"message": "Statement file not found!"}), 404
    
    problem_name = get_problem_name(id)
    if not problem_name:
        return jsonify({"message": "Problem name file not found!"}), 404
    
    # Fetch visible and hidden test cases
    visible_cases = get_visible_testcases(id)
    hidden_cases = get_hidden_testcases(id)
    
    # Combine everything into a response
    testcases = {
        "visible": visible_cases,
        "hidden": hidden_cases
    }
    return jsonify({
        "name": problem_name,
        "statement": statement,
        "testcases": testcases
    })
    
@app.route('/problems', methods=['GET'])
def get_problems():
    dir_path = './problems'
    problem_names = []
    # pth = './problems/1/problem_name/problem_name.txt'
    
    # Loop through all problem directories in './problems'
    for problem in os.listdir(dir_path):
        problem_dir = f'{dir_path}/{problem}'
        # Check if it's a directory
        if os.path.isdir(problem_dir):
            problem_name_file = f'{problem_dir}/problem_name/problem_name.txt'
            # print(problem_name_file)
            with open(problem_name_file, 'r') as file:
                problem_name = file.read().strip()  # Read and remove any extra whitespace or newlines
                # print(problem_name)
                problem_names.append(problem_name)

            # Read the problem name from 'problems_name.txt' if the file exists
            # if os.path.exists(problem_name_file):
            #     print(1)
            #     with open(problem_name_file, 'r') as file:
            #         problem_name = file.read().strip()  # Read and remove any extra whitespace or newlines
            #         print(problem_name)
            #         problem_names.append(problem_name)
    
    # Return the list of problem names
    return jsonify(problem_names)


from run_code.run_code import run_code 
@app.route('/submit/<id>', methods=['POST'])  # Use POST for form submissions
def submit_code(id):
    # Get form data
    lang = request.form.get('lang')
    code = request.form.get('code')
    
    # return lang.strip()
    # return code.strip()

    # Validate language field
    if not lang or lang.strip() == '':
        # print('language is empty')
        return jsonify({"message": "Language cannot be empty!"})

    # Validate code field
    if not code or code.strip() == '':
        return jsonify({"message": "Code cannot be empty!"})

    # Process and print the submitted data
    visible_cases = get_visible_testcases(id)
    for case in visible_cases:
        input = case['input'].strip()
        expected_output = case['expected_output'].strip()
        output = run_code(lang, code, input)
        # print(input, expected_output, output)
        
        if output.endswith("\n"):
            output = output.rstrip("\n")
        if expected_output.endswith("\n"):
            expected_output = expected_output.rstrip("\n")
        if expected_output != output:
            return jsonify({
                "status": "failure",
                "input": input,
                "expected_output": expected_output,
                "output": output,
                "message": "Visible Test case failed!"
            })
    
    # hidden_cases = get_hidden_testcases(id)
    # for case in hidden_cases:
    #     input = case['input'].strip()
    #     expected_output = case['expected_output'].strip()
    #     output = run_code(lang, code, input)
    #     if output.endswith("\n"):
    #         output = output.rstrip("\n")
    #     if expected_output.endswith("\n"):
    #         expected_output = expected_output.rstrip("\n")
    #     if expected_output != output:
    #         return jsonify({
    #             "status": "failure",
    #             "input": input,
    #             "expected_output": expected_output,
    #             "output": output,
    #             "message": "Hidden test case failed!"
    #         })
    
    # Return success response
    return jsonify({
        "status": "success",
        "message": "Congratulations!\nAll cases passed!\nCode ACCEPTED"
        }), 200

@app.route('/contests/<id>', methods=['GET'])
def get_contest_problems(id):
    path_dir = f'./contests/{id}'
    problems = []
    if os.path.isdir(path_dir):
        problems_file = f'{path_dir}/problems.txt'
        if os.path.exists(problems_file):
            with open(problems_file, 'r') as file:
                problems = file.read().split(' ')
    
    return jsonify(problems)


@app.route('/contests', methods=['GET'])
def get_contests():
    path_dir = './contests'
    contests = []
    for contest in os.listdir(path_dir):
        contest_dir = f'{path_dir}/{contest}'
        if os.path.isdir(contest_dir):
            problems_file = f'{contest_dir}/problems.txt'
            if os.path.exists(problems_file):
                with open(problems_file, 'r') as file:
                    problems = file.read().split(',')
                    contests.append({
                        "id": contest,
                        "problems": problems
                    })
    
    return jsonify(contests)


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user_dir = f'./users/user{id}.json'

    # Check if file exists
    if not os.path.exists(user_dir):
        return jsonify({"error": "User not found"}), 404  # Return 404 if not found

    # Read JSON data safely
    with open(user_dir, 'r') as file:
        user_data = json.load(file)

    return jsonify(user_data)

@app.route('/users', methods=['GET'])
def get_users():
    users_dir = './users'
    users = []

    # Ensure the directory exists
    if not os.path.exists(users_dir):
        return jsonify({"error": "Users directory not found"}), 404

    # Iterate over files in the directory
    for filename in os.listdir(users_dir):
        file_path = os.path.join(users_dir, filename)

        # Ensure it's a JSON file
        if filename.endswith('.json') and os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                try:
                    current_user = json.load(file)  # Load JSON data
                    users.append(current_user)      # Append user data
                except json.JSONDecodeError:
                    return jsonify({"error": f"Invalid JSON in {filename}"}), 400

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
