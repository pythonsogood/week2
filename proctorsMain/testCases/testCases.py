import traceback

# Test cases for the functions
def test_prerequisites(_, module):
    try:
        result = module.prerequisites()
        return result, "sorry I am not willing to do this lesson" if not result else "I am going to finish this lesson"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task1(name, module):
    try:
        target = name.replace("_", " ")
        result = module.task1("Hello, ")
        answer = result == f"Hello, {target}"
        return answer, f"Expected: Hello, {target}, Got: {result}" if not answer else "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task2(_, module):
    try:
        inputs = [0, -3, 15, 100]
        expected = ["20", "8", "80", "420"]
        for i, inp in enumerate(inputs):
            result = module.task2(inp)
            if result != expected[i]:
                return False, f"Input: {inp}, Expected: {expected[i]}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task3(_, module):
    try:
        inputs = [0, 15, 18, 20, 21]
        expected = ["False", "False", "True", "True", "True"]
        for i, inp in enumerate(inputs):
            result = module.task3(inp)
            if result != expected[i]:
                return False, f"Input: {inp}, Expected: {expected[i]}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task4(_, module):
    try:
        inputs = [2, 7, 10, -1]
        expected = ["Even", "Odd", "Even", "Odd"]
        for inp, exp in zip(inputs, expected):
            result = module.task4(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

# task is to reverse the string
def test_task5(_, module):
    try:
        inputs = ["hello", "world", "python", "programming"]
        expected = ["olleh5", "dlrow5", "nohtyp6", "gnimmargorp11"]
        for inp, exp in zip(inputs, expected):
            result = module.task5(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
# task is to find the sum of the first n natural numbers
def test_task6(_, module):
    try:
        inputs = [5, 10, 0, 15]
        expected = ["15", "55", "0", "120"]
        for inp, exp in zip(inputs, expected):
            result = module.task6(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task7(_, module):
    try:
        inputs = [12234, 13235, 9923, 11114, 122352455231234]
        expected = ["one1two2three1four1", "one1two1three2five1", "two1three1nine2", "one4four1", "one2two5three3four2five3"]
        for inp, exp in zip(inputs, expected):
            result = module.task7(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task8(_, module):
    try:
        inputs = ["abc123", "password1", "pass1234", "somereallylongpassowrd"]
        expected = ["False", "True", "True", "False"]
        for inp, exp in zip(inputs, expected):
            result = module.task8(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task9(_, module):
    try:
        inputs = [2, 9, 17, 22, 25, 13]
        expected = ["True", "False", "True", "False", "False", "True"]
        for inp, exp in zip(inputs, expected):
            result = module.task9(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
# check if number is palindrome
def test_task10(_, module):
    try:
        inputs = [121, 123, 12321, 12345, 123454321]
        expected = ["True", "False", "True", "False", "True"]
        for inp, exp in zip(inputs, expected):
            result = module.task10(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
#Count how many numbers between start (inclusive) and end (inclusive) are divisible by 5.
def test_task11(_, module):
    try:
        inputs = [(1, 10), (15, 30), (10, 20), (1, 5), (1, 100), (1, 2), (-50, -2)]
        expected = ["2", "4", "3", "1", "20", "0", "10"]
        for inp, exp in zip(inputs, expected):
            result = module.task11(*inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
# Check if two numbers satisfy the condition: their sum is greater than 50.
def test_task12(_, module):
    try:
        inputs = [(25, 30), (20, 10), (30, 20), (25, 25), (50.00000000001, 0)]
        expected = ["True", "False", "False", "False", "True"]
        for inp, exp in zip(inputs, expected):
            result = module.task12(*inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

# Find the maximum of three numbers.
def test_task13(_, module):
    try:
        inputs = [(5, 10, 15), (1, 2, 3), (-3, -2, -1), (11.11111111, 3, 11.11111112)]
        expected = ["15", "3", "-1", "11.11111112"]
        for inp, exp in zip(inputs, expected):
            result = module.task13(*inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task14(_, module):
    try:
        inputs = [5, -1, 0, -0.0000000001]
        expected = ["Positive", "Negative", "Zero", "Negative"]
        for inp, exp in zip(inputs, expected):
            result = module.task14(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task15(_, module):
    try:
        inputs = [(10, 5), (10, 3), (0, 5), (3, 1), (27, 2)]
        expected = ["True", "False", "True", "True", "False"]
        for inp, exp in zip(inputs, expected):
            result = module.task15(*inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
# Check if the numbers form a Pythagorean triplet.
def test_task16(_, module):
    try:
        inputs = [(3, 4, 5), (1, 2, 3), (5, 12, 13), (8, 15, 17), (7, 21, 25), (9, 10, 41)]
        expected = ["True", "False", "True", "True", "False", "False"]
        for inp, exp in zip(inputs, expected):
            result = module.task16(*inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
# find factorial of a number
def test_task17(_, module):
    try:
        inputs = [5, 0, 1, 6]
        expected = ["120", "1", "1", "720"]
        for inp, exp in zip(inputs, expected):
            result = module.task17(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task18(_, module):
    try:
        result = module.task18()
        expected = "7"  # The answer to the riddle
        correct = result == expected
        return correct, f"Expected: {expected}, Got: {result}" if not correct else "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
# Find the sum of all even numbers from 1 to n.
def test_task19(_, module):
    try:
        inputs = [10, 6, 3, -5]
        expected = ["30", "12", "2", "0"]
        for inp, exp in zip(inputs, expected):
            result = module.task19(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task20(_, module):
    try:
        inputs = [(50, 40), (50, 60), (50, 50)]
        expected = ["Too Low", "Too High", "Correct!"]
        for inp, exp in zip(inputs, expected):
            result = module.task20(*inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"