from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question5A(FunctionProblem):
    _var="displayGameScore"   
    _test_cases = [
        ([['A','B'],[21,11],[19,21],[20,21]], """Player A vs B
Game 1 21-11
Game 2 19-21
Game 3 20-21
Overall 1-2
Winner is player B\n"""),
    ([['A', 'B'], [21, 19], [21, 15], [22, 20]], """Player A vs B
Game 1 21-19
Game 2 21-15
Game 3 22-20
Overall 3-0
Winner is player A\n"""),
    ([['P', 'Q'], [0, 0]], """Player P vs Q
Game 1 0-0
Overall 0-0
Winner is player None, Game is Draw\n"""),
    ([['X', 'Y'], [15, 21], [21, 15], [15, 21], [21, 15]], """Player X vs Y
Game 1 15-21
Game 2 21-15
Game 3 15-21
Game 4 21-15
Overall 2-2
Winner is player None, Game is Draw\n""")
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=test):
                out, actual = x.compare_printout_with_args(fn, test)
                x.grading_with_string_comparison((test,expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)    

class Question5B(FunctionProblem):
    _var="getPlayerNames"    
    _test_cases = [
        ("A", "B", [['A', 'B']]),
        ("alice", "bob", [['Alice', 'Bob']]),
        ("Player1", "Player2", [['Player1', 'Player2']])
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                out = fn()
                x.grading(([a,b],expected, out))   
        # test print out
        with patch('builtins.input', side_effect=["A", "a", "A", "B"]):
            out, actual = x.compare_printout(fn)
            x.grading_with_string_comparison((["A", "a", "A","B"], "Player names cannot be the same. Try again.\n", out))


    def check(self, fn):
        self.check_testbook(fn)    

class Question5C(FunctionProblem):
    _var="inputGameScores"    
    _test_cases = [
        ([['A', 'B']], "0-0", "0-0", "", "", [['A', 'B'], [0, 0], [0, 0]]),
        ([['Alice', 'Bob']], "1-2", "3-4", "5-6", "", [['Alice', 'Bob'], [1, 2], [3, 4], [5, 6]]),
        ([['Player1', 'Player2']], "10-15", "", "", "", [['Player1', 'Player2'], [10, 15]]),
        ([['cindy', 'dan']], "", "", "", "", [['cindy', 'dan']])
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test,a,b,c,d,expected in self._test_cases:
            scoreList = test
            with patch('builtins.input', side_effect=[a,b,c,d]):
                out = fn(scoreList)
                x.grading(([test, a,b,c,d],expected, scoreList))
                                
    def check(self, fn):
        self.check_testbook(fn)    

class Question5D(FunctionProblem):
    _var="question5d"    
    _test_cases = [
        ("A", "B", '1-2', '2-3', '', """Player A vs B
Game 1 1-2
Game 2 2-3
Overall 0-2
Winner is player B\n"""),
        ("A", "B", '3-2', '4-1', '', """Player A vs B
Game 1 3-2
Game 2 4-1
Overall 2-0
Winner is player A\n"""),
        ("Alice", "Bob", '1-1', '', '', """Player Alice vs Bob
Game 1 1-1
Overall 0-0
Winner is player None, Game is Draw\n""")
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,d,e, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e]):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b,c,d,e],expected, out))

    def check(self, fn):
        self.check_testbook(fn)    
        
Question5 = MultipartProblem(
    Question5A,
    Question5B,
    Question5C,
    Question5D
)    