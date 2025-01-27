from flask import Flask, jsonify, request
from flask_cors import CORS
import os

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
    
    # Fetch visible and hidden test cases
    visible_cases = get_visible_testcases(id)
    hidden_cases = get_hidden_testcases(id)
    
    # Combine everything into a response
    testcases = {
        "visible": visible_cases,
        "hidden": hidden_cases
    }
    return jsonify({
        "statement": statement,
        "testcases": testcases
    })

if __name__ == '__main__':
    app.run(debug=True)
