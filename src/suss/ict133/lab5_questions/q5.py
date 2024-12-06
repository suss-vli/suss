from learntools.core import *
from unittest.mock import patch
from ...dev import x

# TODO: check if external hints work with this 
class Question5A(EqualityCheckProblem):
    _var = 'marks'
    _expected = { 'John':[0,0], 'Jane':[0,0], 'Peter':[0,0], 'Joe':[0,0] }
    
class Question5B(FunctionProblem): #question3b only checks for the menu printed out. `choice` is not checked
    _var="menuOption"
    _test_cases = [
        (1, """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit\n"""),
        (2, """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit\n"""),
        (3, """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit\n"""),
        (4, """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit\n"""),
        (0, """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit\n"""),
        (5, """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
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

class Question5C(FunctionProblem):
    _var="addMarks"
    _test_cases = [
        ('Jane', 1, 1, 'Student already exists\n', {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}),
        ('A', 0, 0, 'A added\n',{'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0], 'A':[0,0]}),
        ('tom', 0, 0, 'Tom added\n',{'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0], 'Tom':[0,0]}),

         ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,expected, expected_marks, in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c]):
                marks = {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}
                out, actual = x.compare_printout_with_args(fn, marks)
                # x.print_comparison(out,expected)
                x.grading_with_string_comparison(([a,b,c],expected, out))
                x.grading(([a,b,c], expected_marks, marks))
                                                    
    def check(self, fn):
        self.check_testbook(fn)  

class Question5D(FunctionProblem):
    _var="updateMarks"
    _test_cases = [
        (['Jane', 'C', '2'], """Coursework/Exam: 0.0 / 0.0
Updated!!\n""", {'John':[0,0],'Jane':[2.0,0],'Peter':[0,0],'Joe':[0,0]}),
        (['A'], 'A not found\n', {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}),
        (['peter', 'e', '1'], """Coursework/Exam: 0.0 / 0.0
Updated!!\n""", {'John':[0,0],'Jane':[0,0],'Peter':[0.0,1.0],'Joe':[0,0]})
        ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected, expected_marks in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                marks = {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}
                out, actual = x.compare_printout_with_args(fn, marks)
                x.grading_with_string_comparison((a,expected, out))
                x.grading((a, expected_marks, marks))
        
    def check(self, fn):
        self.check_testbook(fn)

class Question5E(FunctionProblem):
    _var="removeStudent"
    _test_cases = [
        ('Jane', 'Student removed\n', {'John':[0,0],'Peter':[0,0],'Joe':[0,0]}),
        ('Alice', 'Alice not found\n', {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}),
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args, expected, expected_marks in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                marks = {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}
                out, actual = x.compare_printout_with_args(fn, marks)
                x.grading_with_string_comparison((args,expected, out))
                x.grading((args, expected_marks, marks))
        
    def check(self, fn):
        self.check_testbook(fn)               

class Question5F(FunctionProblem):
    _var="displayMarks"
    _test_cases = [
        ({'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}, """Name     CsWk Exam Overall Grade
John     0.0  0.0  0.0     F
Jane     0.0  0.0  0.0     F
Peter    0.0  0.0  0.0     F
Joe      0.0  0.0  0.0     F\n"""),
        ({'A':[0,0],'B':[0,0],'C':[0,0],'D':[0,0]}, """Name     CsWk Exam Overall Grade
A        0.0  0.0  0.0     F
B        0.0  0.0  0.0     F
C        0.0  0.0  0.0     F
D        0.0  0.0  0.0     F\n"""),
        ({'John':[100,100],'Jane':[100,100],'Peter':[100,100],'Joe':[100,100]}, """Name     CsWk Exam Overall Grade
John     100.0 100.0 100.0   P
Jane     100.0 100.0 100.0   P
Peter    100.0 100.0 100.0   P
Joe      100.0 100.0 100.0   P\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for marks_value, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=expected):
                marks = marks_value
                out, actual = x.compare_printout_with_args(fn, marks)
                x.grading_with_string_comparison((marks,expected, out))

    def check(self, fn):
        self.check_testbook(fn)

class Question5G(FunctionProblem):
    _var="question5g"
    _test_cases = [
        (['1', 'tom', '80', '89.9', '4', '0'], """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit
Tom added
Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit
Name     CsWk Exam Overall Grade
John     60.0 55.0 57.5    P
Jane     40.0 70.0 55.0    P
Peter    30.0 60.0 45.0    F
Joe      55.5 40.6 48.0    F
Tom      80.0 89.9 85.0    P
Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit\n"""),
        (['2', 'Jane', 'e', '51', '4', '0'], """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit
Coursework/Exam: 40.0 / 70.0
Updated!!
Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit
Name     CsWk Exam Overall Grade
John     60.0 55.0 57.5    P
Jane     40.0 51.0 45.5    F
Peter    30.0 60.0 45.0    F
Joe      55.5 40.6 48.0    F
Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit\n"""),
        (['3', 'peter', '4', '0'], """Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit
Student removed
Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit
Name     CsWk Exam Overall Grade
John     60.0 55.0 57.5    P
Jane     40.0 70.0 55.0    P
Joe      55.5 40.6 48.0    F
Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Quit\n"""),
         # TODO
        # test case for other numbers from 5 to 9 - add on after solution is confirmed, currently still displays marks
        #  (['5', '0'], """Menu
# 1. Add marks
# 2. Update marks
# 3. Remove student
# 4. Display marks
# 0. Quit
# Name     CsWk Exam Overall Grade
# John     60.0 55.0 57.5    P
# Jane     40.0 70.0 55.0    P
# Peter    30.0 60.0 45.0    F
# Joe      55.5 40.6 48.0    F
# Menu
# 1. Add marks
# 2. Update marks
# 3. Remove student
# 4. Display marks
# 0. Quit\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)

Question5 = MultipartProblem(
    Question5A,
    Question5B, 
    Question5C,
    Question5D,
    Question5E,
    Question5F,
    Question5G
)