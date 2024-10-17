from learntools.core import *
from ...dev import x
from sklearn.linear_model import LinearRegression

class Question7(EqualityCheckProblem):

    def produce_expected():
        produce_expected_code = x.get_produce_expected("lab3", "q7", "q7")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        model = exec_globals['produce_expected']()

        return model

    _var = "model"
    _expected = produce_expected()

    def check(self, *args):
        # testing actual model
           
        source = x.get_source_code("lab3", 53)
        actual_source = x.filter_source(source, '#')    
        
        x.determine_the_grading_method(("model", f"model = {Question7._expected}", str(actual_source)))
          
