
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
    sorted_test_cases = dict(
            sorted(
                test_cases.items(),
                key=lambda item: (
                    0 if item[0] == "prerequisites" else int("".join(filter(str.isdigit, item[0]))) if any(char.isdigit() for char in item[0]) else float('inf')
                ),
            )
        )
    return sorted_test_cases