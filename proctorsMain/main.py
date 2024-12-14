import os
import importlib.util
import traceback

# List of allowed file names
allowedFileNames = {
    "testingFolder" : ["Angsar_Aidarbek", "Madi_Makin"],
    "SE-2437": [],
    "SE-2439": []}

# Root directory and subdirectories
root = "D:/Учеба/AITU/PHD/2trimester/introToPython/week2"
group = ["testingFolder", "SE-2437", "SE-2439"]
groupName = group[0]
student_directory = os.path.join(root, groupName)

# Test cases for the functions
def test_prerequisites(_, module):
    try:
        result = module.prerequisites()
        return result, "sorry I am not willing to do this lesson" if result == False else "I am going to finish this lesson"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task1(name, module):
    try:
        target = name.replace("_", " ")
        result = module.task1("Hello, ")
        return True if result == f"Hello, {target}" else False, f"Expected: Hello, {target}, Got: {result}" 
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

# Mapping function names to test cases
test_cases = {
    "prerequisites": test_prerequisites,
    "task1": test_task1,
    # Add more mappings for additional tasks
}

# Function to dynamically load a module from a file
def load_module_from_file(file_path, module_name):
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error loading module {module_name} from {file_path}: {traceback.format_exc()}")
        return None

# Main function to check files
def check_student_files():
    # Ensure the directory exists
    if not os.path.exists(student_directory):
        print(f"Directory not found: {student_directory}")
        return

    # Get all Python files in the student directory
    files = [f for f in os.listdir(student_directory) if f.endswith(".py")]
    messages = []

    for file in files:
        # Get the base name without extension
        student_name = os.path.splitext(file)[0]

        if student_name in allowedFileNames[groupName]:
            print(f"Checking {file}...")
            file_path = os.path.join(student_directory, file)

            # Load the module dynamically
            module = load_module_from_file(file_path, student_name)
            if not module:
                continue

            messages.append([])

            # Run test cases for each function
            for func_name, test_func in test_cases.items():
                if hasattr(module, func_name):
                    success, message = test_func(student_name, module)
                    if success:
                        messages[-1].append(f"Success/{student_name}/{func_name}")
                    else:
                        messages[-1].append(f"Failed/{student_name}/{func_name}: - {message}")
                        break
                else:
                    messages[-1].append(f"FunctionNotFound/{student_name}/{func_name}")
                    break
    return messages

def print_messages(messages):
    """
    Prints the results of the function checks in a structured format.

    Parameters:
    messages (list): A list of lists containing test result messages.
    """
    print("\nTest Results:")
    print("--------------------------------------------------")
    print(messages)
    for student_results in messages:
        if not student_results:
            continue
        print()
        for message in student_results:
            print(message)
    print("--------------------------------------------------")


# Run the checker
if __name__ == "__main__":
    messages = check_student_files()
    print_messages(messages)
