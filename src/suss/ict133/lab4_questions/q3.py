from learntools.core import *
from unittest.mock import patch
from ...dev import x
import sys

class Question3A(FunctionProblem):
    _var="inputSwimmers"
    _test_cases = [
        ("Alice", "Bob", "Cindy", "Dan", "Eric", ['Alice', 'Bob', 'Cindy', 'Dan', 'Eric']),
        ("A", "B", "C", "D", "E", ['A', 'B', 'C', 'D', 'E'])
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for a,b,c,d,e, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e]): #NB: note the use of side_effect
                out = fn()
                x.grading(([a,b,c,d,e], expected, out))
                     
    def check(self, fn):
        self.check_testbook(fn)

class Question3B(FunctionProblem):
    _var="inputTiming"    
    _test_cases = [ # NB: should i include math ValueError: math domain error? Testcases: 10, 5, 2
        (0, 1, 2, 3, 4, [0.0, 1.0, 2.0, 3.0, 4.0]),
        (0, 0, 0, 0, 0, [0.0, 0.0, 0.0, 0.0, 0.0])
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for a,b,c,d,e, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e]): #NB: note the use of side_effect
                swimmers = ['A', 'B', 'C', 'D', 'E']
                out = fn(swimmers)
                x.grading(([a,b,c,d,e], expected, out))
                     
    def check(self, fn):
        self.check_testbook(fn)

class Question3C(FunctionProblem):
    _var="question3c"
    _test_cases = [
        ("A", "B", "C", "D", "E", 0, 0, 0, 0, 0, """A                   0.0s
B                   0.0s
C                   0.0s
D                   0.0s
E                   0.0s
Fastest is        0.0\n"""),
        ("Alice", "Bob", "Cindy", "Dan", "Eric", 0, 1, 2, 3, 4, """Alice               0.0s
Bob                 1.0s
Cindy               2.0s
Dan                 3.0s
Eric                4.0s
Fastest is        0.0\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for a,b,c,d,e,f,g,h,i,j, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e,f,g,h,i,j]): #NB: note the use of side_effect
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b,c,d,e,f,g,h,i,j], expected, out))

    def check(self, fn):
        self.check_testbook(fn)

class Question3D(FunctionProblem):
    _var="question3d"
    _test_cases = [
        ("Alice", "Bob", "Cindy", "Dan", "Eric", 3, 1, 5, 4, 2, """Bob         1.0
Eric        2.0
Alice       3.0
Dan         4.0
Cindy       5.0\n"""),
        ("A", "B", "C", "D", "E", 2, 4, 1, 5, 3, """C           1.0
A           2.0
E           3.0
B           4.0
D           5.0\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB:        
        print("Testing...")
        with patch('builtins.input', side_effect=["James", "Joseph", "Tom", "Dan", "Ian", 47.15, 46.91, 48.2, 47.4, 48.01]) as mock_input:
            # Check if the patch was successfully applied
                fn()
                if mock_input.call_count == 0:
                    out, actual = x.compare_printout(fn)

                    lines = out.strip().split("\n")
                    numbers = []
                    for line in lines:
                        parts = line.split()
                        try:
                            # Convert the second part of each line to a float (the number)
                            numbers.append(float(parts[1]))
                        except IndexError:
                            x.justfail("swimmers", "Please check your code. Attempt the question or assign the timings for the swimmers.")
                       
                            
                    # Check if the numbers are sorted in ascending order
                    if numbers == sorted(numbers):
                        x.justpass()
                    else:
                        x.justfail("printResults", "The swimmers are not sorted in order of the timing. Test your function to check your output.")

                else:
                    for a,b,c,d,e,f,g,h,i,j, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
                        with patch('builtins.input', side_effect=[a,b,c,d,e,f,g,h,i,j]): #NB: note the use of side_effect
                            out, actual = x.compare_printout(fn)
                            x.grading_with_string_comparison(([a,b,c,d,e,f,g,h,i,j], expected, out))
      
    def check(self, fn):
        self.check_testbook(fn)


Question3 = MultipartProblem(
    Question3A,
    Question3B, 
    Question3C,
    Question3D
)    