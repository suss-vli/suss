from learntools.core import *
from ...dev import x
import os

class Question2(FunctionProblem):
    _var="question2" 
    _expected = """Reading from file
Name            Weight   Height   BMI     
John            50.00    1.40     25.51
Peter           60.00    1.70     20.76
Amy             40.00    1.30     23.67
Nathan          70.00    1.70     24.22
Joe             45.00    1.45     21.40\n"""
    _test_cases = [
            ("test_customer.dat", """Reading from file
Name            Weight   Height   BMI     
John            50.00    1.40     25.51
Peter           60.00    1.70     20.76
Amy             40.00    1.30     23.67
Nathan          70.00    1.70     24.22
Joe             45.00    1.45     21.40\n""")
        ]
        
    def test_cases(self):
        return self._test_cases
        
    def check_testbook(self, fn):            
        out, actual = x.compare_printout(fn)
        x.grading_with_string_comparison(("customer.dat", self._expected, out))
        source = x.get_source_code("lab5", 7)
        filtered_source = x.filter_source(source, ["#", "pass", "q"])

        for test in self._test_cases:
            test_file = os.path.dirname(os.path.abspath(__file__)) + "/" + test[0]
            updated_source = x.update_x_in_code(filtered_source, "customer.dat", f"{test_file}")
            exec(updated_source, globals())
            
            # Access the dynamically created function by its name
            fn = globals()["question2"]
            out, actual = x.compare_printout(fn)

            x.grading_with_string_comparison(("test_customer.dat", test[1], out)) 
                        
    def check(self, fn):
        self.check_testbook(fn)    