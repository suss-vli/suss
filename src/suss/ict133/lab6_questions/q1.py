from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1A(FunctionProblem):
    _var="question1a"
    _test_cases = [
        (['100','1', ''], "1.1\n"), 
        (['-1','1', ''], """Weight must be more than 0\n"""),
        (['4','4', '1', '1',''], """Zone must be 1, 2 or 3
0.5\n"""),
        (['2001', '2', ''], "50.45\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a, expected, out))

    def check(self, fn):
        self.check_testbook(fn)    

class Question1B(FunctionProblem):
    _var="question1b"        
    _test_cases = [
        (['100','1', '200', '2', ''], """1.1
5.2\n"""), 
        (['1', '1', '2', '2', '3', '3', ''], """0.5
0.7
1.3\n"""),
        (['-1','1', '4', '4', '1', '10', '2', ''], """Weight must be more than 0
Zone must be 1, 2 or 3
Zone must be 1, 2 or 3
0.5
0.7\n"""),
        (['2001', '5', '2', '10', '1', '30', '3', ''], """Zone must be 1, 2 or 3
50.45
0.5
1.65\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a, expected, out))

    def check(self, fn):
        self.check_testbook(fn)    

Question1 = MultipartProblem(
    Question1A,
    Question1B
)    