import sys
import io
import subprocess
import tempfile

# Function to execute Python code and capture output
def run_python_code(code, input_data=None):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    if input_data:
        sys.stdin = io.StringIO(input_data)  # Simulate user input
    try:
        exec(code)
    except Exception as e:
        captured_output.write(f"Error: {str(e)}")
    result = captured_output.getvalue()
    sys.stdout = sys.__stdout__
    return result

# Function to execute C code
def run_c_code(code, input_data=None):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.c') as tmp_file:
        tmp_file.write(code.encode())
        tmp_file_path = tmp_file.name

    compile_command = f"gcc {tmp_file_path} -o {tmp_file_path}.out"
    run_command = f"{tmp_file_path}.out"
    try:
        subprocess.run(compile_command, check=True, shell=True)
        result = subprocess.run(run_command, input=input_data, capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr}"
    
    return output

# Function to execute C++ code
def run_cpp_code(code, input_data=None):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.cpp') as tmp_file:
        tmp_file.write(code.encode())
        tmp_file_path = tmp_file.name

    compile_command = f"g++ {tmp_file_path} -o {tmp_file_path}.out"
    run_command = f"{tmp_file_path}.out"
    try:
        subprocess.run(compile_command, check=True, shell=True)
        result = subprocess.run(run_command, input=input_data, capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr}"
    
    return output

# Function to execute Java code
def run_java_code(code, input_data=None):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.java') as tmp_file:
        tmp_file.write(code.encode())
        tmp_file_path = tmp_file.name

    compile_command = f"javac {tmp_file_path}"
    run_command = f"java -cp {tmp_file_path.rsplit('/', 1)[0]} {tmp_file_path.split('/')[-1].split('.')[0]}"
    try:
        subprocess.run(compile_command, check=True, shell=True)
        result = subprocess.run(run_command, input=input_data, capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr}"
    
    return output

# Function to execute JavaScript code (Node.js required)
def run_js_code(code, input_data=None):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.js') as tmp_file:
        tmp_file.write(code.encode())
        tmp_file_path = tmp_file.name

    try:
        result = subprocess.run(f"node {tmp_file_path}", input=input_data, capture_output=True, text=True, check=True, shell=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr}"
    
    return output

# Unified function to run code based on language
def run_code(lang, code, input_data=None):
    if lang == "python":
        return run_python_code(code, input_data) 
    elif lang == "c":
        return run_c_code(code, input_data) 
    elif lang == "cpp":
        return run_cpp_code(code, input_data) 
    elif lang == "java":
        return run_java_code(code, input_data) 
    elif lang == "javascript":
        return run_js_code(code, input_data) 
    else:
        return "Unsupported language."
