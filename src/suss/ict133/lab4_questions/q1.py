from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1(FunctionProblem):
    _var="question1"
    _test_cases = [
        ("Dice Occurrence\n"
         "1    0\n"
         "2    0\n"
         "3    0\n"
         "4    0\n"
         "5    100\n"
         "6    0\n"
         "Total: 100\n")
    ]

    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        try:
            with patch('__main__.randint', return_value=5):
                out, actual = x.compare_printout_from_while_loop(fn)
                x.grading_with_string_comparison(
                    ("A hundred of 5s in place of random.randint", self._test_cases[0], out)
                )
        except AttributeError:
            with patch('random.randint', return_value=5):
                out, actual = x.compare_printout_from_while_loop(fn)
                x.grading_with_string_comparison(
                    ("A hundred of 5s in place of random.randint", self._test_cases[0], out)
                )

    def check(self, fn):
        self.check_testbook(fn)
