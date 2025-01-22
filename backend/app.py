from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app, origin='http://localhost:3000/')

# MySQL Database Config
db_config = {
    'user': 'root',  # Replace with your MySQL username
    'password': '',  # Replace with your MySQL password
    'host': 'localhost',
    'database': 'testcase_db',  # Replace with your database name
    'raise_on_warnings': True
}

# Function to get the MySQL connection
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# Create the test_case table if it doesn't exist
# Create the test_case table if it doesn't exist
def create_table():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_cases (
                id INT AUTO_INCREMENT PRIMARY KEY,
                input_data TEXT NOT NULL,
                expected_output TEXT NOT NULL,
                description TEXT
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error while creating table: {err}")
        # Optionally, print a more specific message for the table existence error
        if err.errno == 1050:
            print("Table 'test_cases' already exists.")


create_table()  # Ensure the table is created at startup

# Route for testing
@app.route('/')
def hello_world():
    return jsonify({"message": "Welcome to the Test Case API!"})

# Get all test cases
@app.route('/test_cases', methods=['GET'])
def get_test_cases():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM test_cases')
    test_cases = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(test_cases)

# Add a new test case
@app.route('/test_case', methods=['POST'])
def add_test_case():
    data = request.get_json()
    input_data = data.get('input_data')
    expected_output = data.get('expected_output')
    description = data.get('description')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO test_cases (input_data, expected_output, description)
        VALUES (%s, %s, %s)
    ''', (input_data, expected_output, description))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Test case added successfully!"}), 201

# Get test case by ID
@app.route('/test_case/<int:id>', methods=['GET'])
def get_test_case(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM test_cases WHERE id = %s', (id,))
    test_case = cursor.fetchone()
    cursor.close()
    conn.close()

    if test_case:
        return jsonify(test_case)
    else:
        return jsonify({"message": "Test case not found!"}), 404

# Update test case by ID
@app.route('/test_case/<int:id>', methods=['PUT'])
def update_test_case(id):
    data = request.get_json()
    input_data = data.get('input_data')
    expected_output = data.get('expected_output')
    description = data.get('description')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE test_cases
        SET input_data = %s, expected_output = %s, description = %s
        WHERE id = %s
    ''', (input_data, expected_output, description, id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Test case updated successfully!"})

# Delete test case by ID
@app.route('/test_case/<int:id>', methods=['DELETE'])
def delete_test_case(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM test_cases WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Test case deleted successfully!"})

@app.route('/testcases/<int:id>', methods=['GET'])
def getcase(id):
    dir = f'./testcases/{id}'
    n = len(os.listdir(dir)) / 2
    txt_files = []
    i = 1
    while i <= n:
        input = f'{dir}/input{i}.txt'
        expected_output = f'{dir}/expected_output{i}.txt'
        input_data = ''
        expected_output_data = ''
        with open(input, 'r') as f:
            input_data = f.read()
        with open(expected_output, 'r') as f:
            expected_output_data = f.read()
        txt_files.append({
            'input': input_data,
            'expected_output': expected_output_data
        })
        i += 1
    return jsonify({"cases" : txt_files})

if __name__ == '__main__':
    app.run(debug=True)
