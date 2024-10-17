from ...dev import x
from learntools.core import *
import os
import pandas as pd

class Question1(CodingProblem):

    def produce_expected(employment_rate_file, labour_rate_file):
        expected_file1 = os.path.dirname(os.path.abspath(__file__)) + "/" + employment_rate_file 
        expected_file2 = os.path.dirname(os.path.abspath(__file__)) + "/" + labour_rate_file
        produce_expected_code = x.get_produce_expected("lab4", "q1", "q1")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        expected_employment_rate_percent, expected_labour_force_participation_percent, expected_r = exec_globals['produce_expected_combined_data'](expected_file1, expected_file2)
        expected_r_new = exec_globals['produce_expected_sorted'](expected_file1, expected_file2)

        return expected_employment_rate_percent, expected_labour_force_participation_percent, expected_r, expected_r_new
    

    _vars=["aged_15plus_employment_rate_percent", "aged_15plus_labour_force_participation_rate_percent", "r", "r_new"] # need to specify these variables in the question

    _test_cases = [
        ('employment_rate_test.csv', 'labour_force_participation_test.csv', 'test_females_aged_15plus_employment_rate_percent.csv', 'test_females_aged_15plus_labour_force_participation_rate_percent1.csv')
    ]

    def check(self, *args):
        for test in self._test_cases:
            # testing student's actual code and data file
            actual_employment_rate_percent = args[0]
            actual_labour_force_participation_percent = args[1]
            actual_r = args[2]
            actual_r_new = args[3]

            expected_employment_rate_percent, expected_labour_force_participation_percent, expected_r, expected_r_new = Question1.produce_expected(test[0], test[1])
            x.determine_the_grading_method(("aged_15plus_employment_rate_percent", expected_employment_rate_percent, actual_employment_rate_percent))
            x.determine_the_grading_method(("aged_15plus_labour_force_participation_rate_percent",expected_labour_force_participation_percent, actual_labour_force_participation_percent))
            x.determine_the_grading_method(("r", expected_r, actual_r))
            x.determine_the_grading_method(("r_new", expected_r_new, actual_r_new))
            
            # for test cases:
            
            #getting all source code cells
            cell_numbers = [4,5,6,7,8,9,10,11,13,14,15,16]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab4", item)
                previous = previous + "\n" + current
            
            # update employment rate csv
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[2]
            updated_employment_rate_source = x.update_csv_in_code(previous, new_csv, "aged_15plus_employment_rate_percent")
            
            
            # # update labour rate csv
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[3]
            updated_source = x.update_csv_in_code(updated_employment_rate_source, new_csv, "aged_15plus_labour_force_participation_rate_percent")
            
            variables = {}
            exec(updated_source, globals(), variables)

            actual_test_employment_rate_percent = variables.get('aged_15plus_employment_rate_percent') 
            actual_test_labour_force_participation_percent = variables.get('aged_15plus_labour_force_participation_rate_percent') 
            actual_test_r =  variables.get('r')
            
            # expected for test case
            expected_test_employment_rate_percent, expected_test_labour_force_participation_percent, expected_test_r, expected_test_r_new = Question1.produce_expected(test[2], test[3])
            x.determine_the_grading_method(("aged_15plus_employment_rate_percent", expected_test_employment_rate_percent, actual_test_employment_rate_percent))
            x.determine_the_grading_method(("aged_15plus_labour_force_participation_rate_percent",expected_test_labour_force_participation_percent, actual_test_labour_force_participation_percent))
            x.determine_the_grading_method(("r", expected_test_r, actual_test_r))
                        
            actual_test_r_new =  variables.get('r_new')
            x.determine_the_grading_method(("r_new", expected_test_r_new, actual_test_r_new))