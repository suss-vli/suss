from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question2A(FunctionProblem):
    _var="isArmstrongNumber"
    _test_cases = [
        (1, True), 
        (11, False),
        (12, False),
        (153, True),
        (370, True)
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
                actual = fn(test)
                x.grading((test, expected, actual))

    def check(self, fn):
        self.check_testbook(fn)    

class Question2B(FunctionProblem):
    _var="rollDice"        
    _test_cases = [
        ([1, 2, 0, 2, 1, 5], "[2, 4, 1, 6, 5]\n"),
        ([5, 4, 0], "[6]\n")
    ]

    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test, expected in self._test_cases:
            try:
                with patch('__main__.randint', side_effect=test):
                    out, actual = x.compare_printout(fn)
                    x.grading_with_string_comparison((test, expected, out))
            except AttributeError:
                with patch('random.randint', side_effect=test):
                    out, actual = x.compare_printout(fn)
                    x.grading_with_string_comparison((test, expected, out))


    def check(self, fn):
        self.check_testbook(fn)    

Question2 = MultipartProblem(
    Question2A,
    Question2B
)    