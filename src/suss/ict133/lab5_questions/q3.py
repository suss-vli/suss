from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question3A(FunctionProblem):
    _var="printGroupSummary" 
    _test_cases = [
        ({'T01':28, 'T02':15, 'T03':28, 'T04':25, 'T05':29, 'T06':22 }, """TG   Size
T01   28 
T02   15 
T03   28 
T04   25 
T05   29 
T06   22 
Total number of students 147\n"""),
        ({'T01': 20, 'T02': 20, 'T03': 20, 'T04': 20}, """TG   Size
T01   20 
T02   20 
T03   20 
T04   20 
Total number of students 80\n"""),
        ({'T01': 35}, """TG   Size
T01   35 
Total number of students 35\n"""),
        ({'T01': 12, 'T02': 25, 'T03': 30, 'T04': 18}, """TG   Size
T01   12 
T02   25 
T03   30 
T04   18 
Total number of students 85\n"""),
        ({'T01': 100, 'T02': 150, 'T03': 200}, """TG   Size
T01  100 
T02  150 
T03  200 
Total number of students 450\n"""),
        ({}, """TG   Size
Total number of students 0\n""")
        ]
        
    def test_cases(self):
        return self._test_cases
        
    def check_testbook(self, fn):            
        for test in self._test_cases:
            tutGp = test[0]
            out, actual = x.compare_printout_with_args(fn, tutGp)
            x.grading_with_string_comparison((f"tutGp = {test[0]}", test[1], out))
                        
    def check(self, fn):
        self.check_testbook(fn)    

class Question3B(FunctionProblem):
    _var="addUpdateGroup" 
    _test_cases = [
        ('T01', '1', """Tutorial group exists. Class size is 28
Class size for T01 adjusted to 29\n"""),
        ('T05', '2', """Tutorial group exists. Class size is 29
Class size must not go below 20 and more than 30
Class size for T05 adjusted to 29\n"""),
        ('t06', '-3', """Tutorial group exists. Class size is 22
Class size must not go below 20 and more than 30
Class size for T06 adjusted to 22\n"""),
        ('T02', '0', """Tutorial group exists. Class size is 15
No amendment needed
Class size for T02 adjusted to 15\n"""),
        ('T07', '10', """New Tutorial Group.
Class size must not go below 20 and more than 30
Tutorial Group T07 added with class size 0\n"""),
        ('T07', '20', """New Tutorial Group.
Tutorial Group T07 added with class size 20\n""")
        ]
        
    def test_cases(self):
        return self._test_cases
        
    def check_testbook(self, fn):            
        for test in self._test_cases:
            with patch('builtins.input', side_effect=[test[0], test[1]]):
                tutGp = {'T01':28, 'T02':15, 'T03':28, 'T04':25, 'T05':29, 'T06':22 }
                out, actual = x.compare_printout_with_args(fn, tutGp)
                x.grading_with_string_comparison((f"{test[0]}, {test[1]}", test[2], out))
                        
    def check(self, fn):
        self.check_testbook(fn) 

class Question3C(FunctionProblem):
    _var="updateAllGroup" 
    _test_cases = [
        ({'T01':28, 'T02':15, 'T03':28, 'T04':25, 'T05':29, 'T06':22 }, """T01 adjusted to max 30
T02 adjusted to 18
T03 adjusted to max 30
T04 adjusted to 28
T05 adjusted to max 30
T06 adjusted to 25\n"""),
        ({'T01': 0, 'T02': 0, 'T03': 0}, """T01 adjusted to 3
T02 adjusted to 3
T03 adjusted to 3\n"""),
        ({'T01': 30, 'T02': 35, 'T03': 32, 'T04': 40}, """T01 adjusted to max 30
T02 adjusted to max 30
T03 adjusted to max 30
T04 adjusted to max 30\n"""),
        ({'T01': 18, 'T02': 5, 'T03': 30, 'T04': 15, 'T05': 20, 'T06': 24, 'T07': 35}, """T01 adjusted to 21
T02 adjusted to 8
T03 adjusted to max 30
T04 adjusted to 18
T05 adjusted to 23
T06 adjusted to 27
T07 adjusted to max 30\n"""),
        ({'T01': 25}, """T01 adjusted to 28\n"""),
        ({}, "")
        ]
        
    def test_cases(self):
        return self._test_cases
        
    def check_testbook(self, fn):            
        for test in self._test_cases:
            tutGp = test[0].copy()
            out, actual = x.compare_printout_with_args(fn, tutGp)
            x.grading_with_string_comparison((f"tutGp = {test[0]}", test[1], out))
                        
    def check(self, fn):
        self.check_testbook(fn) 

Question3 = MultipartProblem(
    Question3A,
    Question3B,
    Question3C
)    