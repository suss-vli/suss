from learntools.core import *
from ...dev import x
import os

class Question1(FunctionProblem):
    _var="question1" 
    _expected = """Rainfall Summary
Avg rainfall 5.65mm
No of days with no rain 3 days
Highest rainfall recorded 20.6mm\n"""   
    _test_cases = [
        ("test_rainfall.dat", """Rainfall Summary
Avg rainfall 5.67mm
No of days with no rain 0 days
Highest rainfall recorded 21.2mm\n""")
    ]
    
    def test_cases(self):
        return self._test_cases
    
    def check_testbook(self, fn):
        out, actual = x.compare_printout(fn)
        x.grading_with_string_comparison(("rainfall.dat", self._expected, out))

        source = x.get_source_code("lab5", 4)
        filtered_source = x.filter_source(source, ["#", "pass", "q"])

        for test in self._test_cases:
            test_file = os.path.dirname(os.path.abspath(__file__)) + "/" + test[0]
            updated_source = x.update_x_in_code(filtered_source, "rainfall.dat", f"{test_file}")
            exec(updated_source, globals())
            
            # Access the dynamically created function by its name
            fn = globals()["question1"]
            out, actual = x.compare_printout(fn)

            x.grading_with_string_comparison(("test_rainfall.dat", test[1], out)) 
                        
    def check(self, fn):
        self.check_testbook(fn)