
from . import testCases as tc

# from inspect import getmembers, isfunction
# print(getmembers(tc, isfunction))
# print(tc.must_test_prerequisites)
# print(dir(tc))

# Function to dynamically load test cases from testCases module
def load_test_cases():
    test_cases = {}
    for attr_name in dir(tc):
        if attr_name.startswith("test_") and callable(getattr(tc, attr_name)):
            func_name = attr_name[len("test_"):]  # Remove the 'must_' prefix
            test_cases[func_name] = getattr(tc, attr_name)
    return test_cases