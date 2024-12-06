from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question4A(FunctionProblem):
    _var = 'initializeSoups'    
    _test_cases = [
        ({'C': ['Clam Chowder', 50], 'M': ['Mushroom', 45], 'T': ['Tomato', 40], 'P': ['Pumpkin', 50], 'O': ['Oxtail', 10]})
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): 
        for expected in self._test_cases: 
            out = fn()
            x.grading(("soups.txt", expected, out))

    def check(self, fn):
        self.check_testbook(fn)
class Question4B(FunctionProblem):
    _var="question4b"
    _test_cases = [
        (['3', '0'], """Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
ID   Name            Qty 
C    Clam Chowder    50  
M    Mushroom        45  
T    Tomato          40  
P    Pumpkin         50  
O    Oxtail          10  
Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
End of program\n"""),
        (['1', 'M', '24', '3', '0'], """Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
ID   Name            Qty 
C    Clam Chowder    50  
M    Mushroom        45  
T    Tomato          40  
P    Pumpkin         50  
O    Oxtail          10  
Thank you for your purchase!
Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
ID   Name            Qty 
C    Clam Chowder    50  
M    Mushroom        21  
T    Tomato          40  
P    Pumpkin         50  
O    Oxtail          10  
Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
End of program\n"""),
(['2', 'C', '10', '2', 'T', '10', '3', '0'], """Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
ID   Name            Qty 
Cannot replenish more than 50!
Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
ID   Name            Qty 
Replenish successful!
Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
ID   Name            Qty 
C    Clam Chowder    50  
M    Mushroom        21  
T    Tomato          50  
P    Pumpkin         50  
O    Oxtail          10  
Menu
1. Purchase Soup
2. Replenish Soup
3. Display all soups
0. Quit 
End of program\n""" )
]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        with open('soups.txt', 'w') as file:
            file.write("""Clam Chowder,50
Mushroom,45
Tomato,40
Pumpkin,50
Oxtail,10""")
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a, expected, out))

    def check(self, fn):
        self.check_testbook(fn)            

Question4 = MultipartProblem(
    Question4A,
    Question4B
)