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