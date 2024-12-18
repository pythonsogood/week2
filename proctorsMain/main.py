import os
import traceback
import importlib.util
import testCases.loading as ltc

# List of allowed file names
allowedFileNames = {
    "testingFolder": ["Angsar_Aidarbek", "Unknown_Profile"],
    "SE-2437": [
        "Baisal_Alym",
        "Alisher_Assanov",
        "Ardak_Avissauly",
        "Aisulu_Azimkhan",
        "Bibifatima_Bisesheva",
        "Alikhan_Bizhanov",
        "Muhtarali_Duysenbay",
        "Islam_Imanbayev",
        "Medina_Klyumova",
        "Ivan_Kuznetsov",
        "Dias_Madyshev",
        "Sarah_Mukhammad",
        "Raiymbek_Mussin",
        "Ataniyaz_Mutigolla",
        "Alikhan_Nauanov",
        "Ibrahim_Nygyman",
        "Yeskendir_Salimov",
        "Muslim_Syzdikov",
        "Dias_Tursynbai",
        "Zhanibek_Yksak",
        "Shugyla_Zhaxylykova",
        "Beibarys_Zhumagali"
    ],
    "SE-2439": [
        "Sultan_Agibaev",
        "Yerassyl_Aman",
        "Alisher_Askar",
        "Gaziza_Bakir",
        "Ramazan_Bisembay",
        "Zhadyrassyn_Imangali",
        "Alikhan_Kulzhanov",
        "Elkham_Mamedov",
        "Almat_Muzdybay",
        "Miras_Omar",
        "Ilnur_Saipiyev",
        "Merkhan_Samat",
        "Aizada_Sembayeva",
        "Yernur_Syrlibayev",
        "Assel_Tynysbek",
        "Erasyl_Umirbay",
        "Sultan_Yakupov",
        "Shynbergen_Yegizbayev",
        "Aiya_Zhakupova",
        "Nurdan_Zhanabayev",
        "Nurzhiğit_Zhunis"
    ]
}

# Root directory and subdirectories
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Traverse up one level
group = ["testingFolder", "SE-2437", "SE-2439"]
groupName = group[0]
group_directory = os.path.join(root, groupName)

# Function to clean up student directories
def clean_student_directories():
    RED = "\033[91m"   # ANSI code for red text
    RESET = "\033[0m"  # ANSI code to reset text color

    # Ensure the directory exists
    if not os.path.exists(group_directory):
        print(f"{RED}Group directory not found: {group_directory}{RESET}")
        return False
    
    for student_name in allowedFileNames[groupName]:
        student_folder = os.path.join(group_directory, student_name)
        if os.path.exists(student_folder):
            for file_name in os.listdir(student_folder):
                file_path = os.path.join(student_folder, file_name)
                # Delete the file if it's not "run.py"
                if os.path.isfile(file_path) and file_name != "run.py":
                    print(f"Deleting file: {file_path}")
                    os.remove(file_path)

    return True

# Function to dynamically load a module from a file
def load_module_from_file(file_path, module_name):
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception:
        print(f"Error loading module {module_name} from {file_path}: {traceback.format_exc()}")
        return None

# Main function to check files
def check_student_files(test_cases = [[], []]):

    RED = "\033[91m"   # ANSI code for red text
    RESET = "\033[0m"  # ANSI code to reset text color

    # Ensure the directory exists
    if not os.path.exists(group_directory):
        print(f"{RED}Group directory not found: {group_directory}{RESET}")
        return

    messages = []
    for student_name in allowedFileNames[groupName]:
        student_path = os.path.join(group_directory, student_name, "run.py")
        if not os.path.exists(student_path):
            print(f"{RED}File not found: {student_path}{RESET}")
            continue

        print(f"Checking {student_name}...")
        module = load_module_from_file(student_path, student_name)
        if not module:
            continue

        messages.append([])
        # Run test cases for each function
        for func_name, test_func in test_cases.items():
            if hasattr(module, func_name):
                success, message = test_func(student_name, module)
                if success:
                    messages[-1].append(f"Success/{student_name}/{func_name}: - {message}")
                else:
                    messages[-1].append(f"Failed/{student_name}/{func_name}: - {message}")

                    if func_name != "prerequisites":
                        # Create a .txt file for failed test cases
                        failure_file_path = os.path.join(group_directory, student_name, f"{func_name}_failure.txt")
                        with open(failure_file_path, "w") as failure_file:
                            failure_file.write(f"Student: {student_name}\n")
                            failure_file.write(f"Function: {func_name}\n")
                            failure_file.write(f"Error Details: {message}\n")

                    break
            else:
                messages[-1].append(f"FunctionNotFound/{student_name}/{func_name}")
                break
    return messages

def print_messages(messages):
    RED = "\033[91m"   # ANSI code for red text
    GREEN = "\033[92m" # ANSI code for green text
    RESET = "\033[0m"  # ANSI code to reset text color

    print("\nTest Results:")
    print("--------------------------------------------------")
    for student_results in messages:
        if not student_results:
            continue
        print()
        if (0 < len(student_results)):
            print(f"{GREEN if 'Success' in student_results[0] else RED}{student_results[0]}{RESET}")
        if (2 < len(student_results)):
            print("...")
        if (1 < len(student_results)):
            print(f"{GREEN if 'Success' in student_results[-1] else RED}{student_results[-1]}{RESET}")
    print("--------------------------------------------------")


# Run the checker
if __name__ == "__main__":
    status = clean_student_directories()  # Clean up directories before running tests

    if (status):
        # Mapping function names to test cases
        test_cases = ltc.load_test_cases()
        messages = check_student_files(test_cases)
        print_messages(messages)
