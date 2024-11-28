from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question2(FunctionProblem):
    _var="question2"
    _test_cases = [
        ("S7928964G", """Valid NRIC\n"""),
        ("S7928964g", """Valid NRIC\n"""),
        ("S1234567A", """Ref Char is not correct\n"""),
        ("T1234567J", """Valid NRIC\n"""),
        ("F76A4321I", """Must consist of 7 digits\n"""),
        ("G2345678M", """Ref Char is not correct\n"""),
        ("X7654321I", """The first letter must be S, T, F or G\n"""),
        ("S7654321*", """Reference letter must be A to Z or a to z\n"""),
        ("S123456789", """Length must be exactly 9\n""")        
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((args, expected, out))
                     
    def check(self, fn):
        self.check_testbook(fn)