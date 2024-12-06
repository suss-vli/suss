from learntools.core import *
from unittest.mock import patch
from ...dev import x

# Question4 - step by step multiple part functional problem
class Question4A(EqualityCheckProblem):
    _var = 'currs'
    _expected = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
    
class Question4B(FunctionProblem): #question3b only checks for the menu printed out. `choice` is not checked
    _var="menuOption"
    _test_cases = [
        (1, """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n"""),
        (2, """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n"""),
        (3, """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n"""),
        (4, """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n"""),
        (0, """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n"""),
        (5, """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=test):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((test,expected, out))
                x.determine_the_grading_method((test, test, actual))

    def check(self, fn):
        self.check_testbook(fn)       

class Question4C(FunctionProblem):
    _var="addCurrency"
    _test_cases = [
        ('MYR',3, """MYR with rate 3.0 has been added successfully\n""", {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73, 'MYR': 3.0}),
        ('hkd',4, """Currency already exists\n""", {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73})
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,expected, expected_currs in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
                out, actual = x.compare_printout_with_args(fn, currs)
                # x.print_comparison(out,expected)
                x.grading_with_string_comparison(([a,b],expected, out))
                x.grading(([a,b], expected_currs, currs))
                                                    
    def check(self, fn):
        self.check_testbook(fn)  

class Question4D(FunctionProblem):
    _var="adjustCurrency"
    _test_cases = [
        ('sgd', '', 'Currency not found!\n', {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}),
        ('usd', '1', """Rate is 0.73\n""", {'USD': 1.0, 'RMB': 5.01, 'HKD': 5.73}),
        ('rmb', '5.01', """Rate is 5.01
No change was made\n""", {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73})

    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,expected, expected_currs in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
                out, actual = x.compare_printout_with_args(fn, currs)
                x.grading_with_string_comparison(([a,b],expected, out))
                x.grading(([a,b], expected_currs, currs))
        
    def check(self, fn):
        self.check_testbook(fn)

class Question4E(FunctionProblem):
    _var="removeCurrency"
    _test_cases = [
        ('hkd', 'HKD has been removed successfully\n', {'USD': 0.73, 'RMB': 5.01}),
        ('myr', 'No such currency.\n', {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73})
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args,expected, expected_currs in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
                out, actual = x.compare_printout_with_args(fn, currs)
                x.grading_with_string_comparison((args,expected, out))
                x.grading((args, expected_currs, currs))
        
    def check(self, fn):
        self.check_testbook(fn)               

class Question4F(FunctionProblem):
    _var="displayCurrencyRates"  
    _test_cases = [
        ({'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}, """Currency   Rate
USD        0.73
RMB        5.01
HKD        5.73\n"""),
        ({'USD': 0.73, 'RMB': 5.01}, """Currency   Rate
USD        0.73
RMB        5.01\n"""),
        ({'SGD': 1.0, 'MYR': 3.0}, """Currency   Rate
SGD        1.00
MYR        3.00\n"""),
        ({}, """Currency   Rate\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for currs_value,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=expected): # TODO: remove this? 
                currs = currs_value
                out, actual = x.compare_printout_with_args(fn, currs)
                x.grading_with_string_comparison((currs,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)

class Question4G(FunctionProblem):
    _var="question4g"
    _test_cases = [
        (['1', 'sgd', '1', '4', '0'], """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit
SGD with rate 1.0 has been added successfully
Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit
Currency   Rate
USD        0.73
RMB        5.01
HKD        5.73
SGD        1.00
Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n"""),
        (['2', 'usd', '0.5', '4', '0'], """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit
Rate is 0.73
Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit
Currency   Rate
USD        0.50
RMB        5.01
HKD        5.73
Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n"""),
        (['3', 'rmb', '4', '0'], """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit
RMB has been removed successfully
Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit
Currency   Rate
USD        0.73
HKD        5.73
Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n"""),
        # TODO
        # test case for other numbers from 5 to 9 - add on after solution is confirmed, currently still displays currency
        #  (['5', '0'], """Menu
# 1. Add Currency
# 2. Adjust Currency
# 3. Remove Currency
# 4. Display Currency rates
# 0. Quit
# Currency   Rate
# USD        0.73
# RMB        5.01
# HKD        5.73
# Menu
# 1. Add Currency
# 2. Adjust Currency
# 3. Remove Currency
# 4. Display Currency rates
# 0. Quit\n""")
        
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a): #TODO remove this?
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)

Question4 = MultipartProblem(
    Question4A,
    Question4B, 
    Question4C,
    Question4D,
    Question4E,
    Question4F,
    Question4G
)