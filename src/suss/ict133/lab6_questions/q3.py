from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question3(FunctionProblem): 
    _var="question3"
    _test_cases = [
        (10, ["A","B","C","", "50", "60","70","20", "30", "10", "Y", "1", "5", "22", "10", "10", "15", "N"], """{'A': [0, 0], 'B': [0, 0], 'C': [0, 0]}
10
Processing guess of A: 50 Too High
Processing guess of B: 60 Too High
Processing guess of C: 70 Too High
Processing guess of A: 20 Too High
Processing guess of B: 30 Too High
Processing guess of C: 10 correct! in 2 tries
Winner : ['C']
10
Processing guess of A: 1 Too Low
Processing guess of B: 5 Too Low
Processing guess of C: 22 Too High
Processing guess of A: 10 correct! in 2 tries
Processing guess of B: 10 correct! in 2 tries
Processing guess of C: 15 Too High
Winner : ['A', 'B']
{'A': [10, 1], 'B': [10, 1], 'C': [15, 1]}

Game  1
C 
Game  2
A B """),
        (1, ["Tom", "Alex", "", "50", "40", "10", "8", "1", "1", "N"], """{'Tom': [0, 0], 'Alex': [0, 0]}
1
Processing guess of Tom: 50 Too High
Processing guess of Alex: 40 Too High
Processing guess of Tom: 10 Too High
Processing guess of Alex: 8 Too High
Processing guess of Tom: 1 correct! in 3 tries
Processing guess of Alex: 1 correct! in 3 tries
Winner : ['Tom', 'Alex']
{'Tom': [1, 1], 'Alex': [1, 1]}

Game  1
Tom Alex """),
        (100, ["Jane", "Peter", "John", "", "50", "40", "10", "70", "80", "90", "100", "99", "100", "Y", "88", "67", "97", "99", "89", "100","N"], """{'Jane': [0, 0], 'Peter': [0, 0], 'John': [0, 0]}
100
Processing guess of Jane: 50 Too Low
Processing guess of Peter: 40 Too Low
Processing guess of John: 10 Too Low
Processing guess of Jane: 70 Too Low
Processing guess of Peter: 80 Too Low
Processing guess of John: 90 Too Low
Processing guess of Jane: 100 correct! in 3 tries
Processing guess of Peter: 99 Too Low
Processing guess of John: 100 correct! in 3 tries
Winner : ['Jane', 'John']
100
Processing guess of Jane: 88 Too Low
Processing guess of Peter: 67 Too Low
Processing guess of John: 97 Too Low
Processing guess of Jane: 99 Too Low
Processing guess of Peter: 89 Too Low
Processing guess of John: 100 correct! in 2 tries
Winner : ['John']
{'Jane': [99, 1], 'Peter': [89, 0], 'John': [100, 2]}

Game  1
Jane John 
Game  2
John """)        
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for number, test, expected in self._test_cases:
            with patch('random.randint', return_value=number):
                with patch('builtins.input', side_effect = test):
                    out, actual = x.compare_printout_from_while_loop(fn)
                    x.grading_with_assertion((out == expected), (test , expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)    