from learntools.core import *
from ...dev import x

class Question6(EqualityCheckProblem):

    def check(self, *args):
  
        source = x.get_source_code("lab3", 49)
        updated_source = x.filter_source(source, '#')
        
        if "from sklearn.linear_model import LinearRegression" in updated_source:
            x.justpass()
        else:
            x.justfail("from sklearn.linear_model import LinearRegression", "`from sklearn.linear_model import LinearRegression` is not found. Please import LinearRegression from sklearn.linear_model.")
