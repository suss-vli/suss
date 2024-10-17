from learntools.core import *
from ...dev import x

class Question2A(EqualityCheckProblem):

    _var = "ex1"
    _expected = ['a', 'b', 'c', 'd']

    _test_cases = [
        ("c", "f", ['a', 'b', 'f', 'd'])
        # (4, [0, 16, 81, 256, 625, 1296, 2401, 1])
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
    
            source = x.get_source_code("lab1", 97)

            x.test_for_none_588(source, "lab1", 97, f"{test[0]}", f"{test[1]}", f"{test[0]}")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"{test[1]}")
            
            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_ex1 = local_vars.get('ex1')
            x.determine_the_grading_method((test[1], test[2], executed_ex1))

class Question2B(EqualityCheckProblem):

    _var = "ex2"
    _expected = ['b', 'c', 'd', 'b', 'c', 'd']

    _test_cases = [
        ("d", "f", ['b', 'c', 'f', 'b', 'c', 'f'])
        # (4, [0, 16, 81, 256, 625, 1296, 2401, 1])
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
                
            #getting all source code cells for q1a
            source = x.get_multiple_cell_source("lab1", [97,100])
            # print("----source----")
            # print(source)

            x.test_for_none_588(source, "lab1", 97, f"{test[0]}", f"{test[1]}", f"ex1.append({test[0]})")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"{test[1]}")  

            updated_source = x.filter_source(test_source, 'print')
            
            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_ex2 = local_vars.get('ex2')
            x.determine_the_grading_method((test[1], test[2], executed_ex2))


Question2 = MultipartProblem(
    Question2A,
    Question2B
)    