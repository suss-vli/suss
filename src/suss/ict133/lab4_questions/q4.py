from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question4A(CodingProblem): 
    _var="scores"   
    _expected = """Diver	A1	A2	A3	Total
1	7.9	7.8	8.2	23.9
2	8.0	8.5	8.4	24.9
3	9.0	9.1	9.5	27.6
4	9.0	9.2	9.2	27.4
5	8.5	8.8	9.0	26.3
6	8.7	8.8	8.7	26.2\n"""
    _test_cases = [
        ([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], """Diver	A1	A2	A3	Total
1	0.0	0.0	0.0	0.0
2	0.0	0.0	0.0	0.0
3	0.0	0.0	0.0	0.0
4	0.0	0.0	0.0	0.0
5	0.0	0.0	0.0	0.0
6	0.0	0.0	0.0	0.0\n""")

    ]
        
    def test_cases(self):
        return self._test_cases

    def check(self, *args):
        source = x.get_source_code("lab4", 27)
        filtered_source = x.filter_source(source, ['#', 'q4', 'pass'])

        lines = filtered_source.split('\n')
        updated_source = '\n'.join(['    ' + line for line in lines]) 

        fn_name = "fn"
        fn_source = f"def fn():\n{updated_source}"
        # Execute the function definition
        exec(fn_source, globals())
        
        # Access the dynamically created function by its name
        fn = globals()[fn_name]
        out, actual = x.compare_printout(fn)

        x.grading_with_string_comparison(("scores of 6 divers", self._expected, out)) 
        
        for test in self._test_cases:
            # replace "scores"
            for line in lines:
                if line.startswith('scores') and '=' in line:
                    filtered_source2 = x.filter_source(filtered_source,  ['scores', '[', 'pass'])
                    updated_source_with_test = f"scores = {test[0]}\n" + filtered_source2
                    test_lines = updated_source_with_test.split('\n')
                    test_source = '\n'.join(['    ' + line for line in test_lines]) 
 
                    fn_name = "test"
                    fn_source = f"def test():\n{test_source}"
                    # Execute the function definition
                    exec(fn_source, globals())
                    
                    # Access the dynamically created function by its name
                    fn = globals()[fn_name]
                    out, actual = x.compare_printout(fn)
                    x.grading_with_string_comparison((f"{test[0]}", test[1], out)) 
                    break


class Question4B(CodingProblem):
    _var="scores"
    _expected = """\nTop three positions
Diver	Total
3	27.6
4	27.4
5	26.3\n"""
    _test_cases = [
        ([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], """\nTop three positions
Diver	Total
1	0.0
2	0.0
3	0.0\n""")

    ]
        
    def test_cases(self):
        return self._test_cases

    def check(self, *args):
        scores_source = x.get_source_code("lab4", 27)
        source = x.filter_source(scores_source, 'print') + x.get_source_code("lab4", 30)
        filtered_source = x.filter_source(source, ['#', 'q4', 'pass'])

        lines = filtered_source.split('\n')
        updated_source = '\n'.join(['    ' + line for line in lines]) 

        fn_name = "fn"
        fn_source = f"def fn():\n{updated_source}"
        # Execute the function definition
        exec(fn_source, globals())
        
        # Access the dynamically created function by its name
        fn = globals()[fn_name]
        out, actual = x.compare_printout(fn)

        x.grading_with_string_comparison(("scores of 6 divers", self._expected, out)) 
        
        for test in self._test_cases:
            # replace "scores"
            for line in lines:
                if line.startswith('scores') and '=' in line:
                    filtered_source2 = x.filter_source(filtered_source, ['scores', '[', 'pass'])
                    # filtered_source2 = x.filter_source(filtered_source2, '[')
                    updated_source_with_test = f"scores = {test[0]}\n" + filtered_source2
                    test_lines = updated_source_with_test.split('\n')
                    test_source = '\n'.join(['    ' + line for line in test_lines]) 
 
                    fn_name = "test"
                    fn_source = f"def test():\n{test_source}"
                    # Execute the function definition
                    exec(fn_source, globals())
                    
                    # Access the dynamically created function by its name
                    fn = globals()[fn_name]
                    out, actual = x.compare_printout(fn)
                    x.grading_with_string_comparison((f"{test[0]}", test[1], out)) 
                    break


class Question4C(CodingProblem):
    _var="scores"
    _expected = """Diver	A1	A2	A3	Total
1	7.9	7.8	8.2	23.9
2	8.0	8.5	8.4	24.9
3	9.0	9.1	9.5	27.6
4	9.0	9.2	9.2	27.4
5	8.5	8.8	9.0	26.3
6	9.7	9.8	9.7	29.2

Top three positions
Diver	Total
6	29.2
3	27.6
4	27.4\n"""
    _test_cases = [
        ([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], """Diver	A1	A2	A3	Total
1	0.0	0.0	0.0	0.0
2	0.0	0.0	0.0	0.0
3	0.0	0.0	0.0	0.0
4	0.0	0.0	0.0	0.0
5	0.0	0.0	0.0	0.0
6	0.0	0.0	0.0	0.0

Top three positions
Diver	Total
1	0.0
2	0.0
3	0.0\n""")

    ]
        
    def test_cases(self):
        return self._test_cases

    def check(self, *args):
        source = x.get_source_code("lab4", 33)
        filtered_source = x.filter_source(source, ['#', 'q4', 'pass'])

        lines = filtered_source.split('\n')
        updated_source = '\n'.join(['    ' + line for line in lines]) 

        fn_name = "fn"
        fn_source = f"def fn():\n{updated_source}"
        # Execute the function definition
        exec(fn_source, globals())
        
        # Access the dynamically created function by its name
        fn = globals()[fn_name]
        out, actual = x.compare_printout(fn)

        x.grading_with_string_comparison(("scores", self._expected, out)) 
        
        for test in self._test_cases:
            # replace "scores"
            for line in lines:
                if line.startswith('scores') and '=' in line:
                    filtered_source2 = x.filter_source(filtered_source, ['scores', '[', ']'])
                    updated_source_with_test = f"scores = {test[0]}\n" + filtered_source2
                    test_lines = updated_source_with_test.split('\n')
                    test_source = '\n'.join(['    ' + line for line in test_lines])
                    print(test_source) 
 
                    fn_name = "test"
                    fn_source = f"def test():\n{test_source}"
                    # Execute the function definition
                    exec(fn_source, globals())
                    
                    # Access the dynamically created function by its name
                    fn = globals()[fn_name]
                    out, actual = x.compare_printout(fn)
                    x.grading_with_string_comparison((f"{test[0]}", test[1], out)) 
                    break
 

Question4 = MultipartProblem(
    Question4A,
    Question4B,
    Question4C
)    