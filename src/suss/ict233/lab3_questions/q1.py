import re
import requests
from ...dev import x
from learntools.core import *
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


class Question1(EqualityCheckProblem):

    def produce_expected(file):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + file
        produce_expected_code = x.get_produce_expected("lab3", "q1", "q1")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        expected_df = exec_globals['produce_expected'](expected_file)[0]
        expected_fig = exec_globals['produce_expected'](expected_file)[1]
        return expected_df, expected_fig

    _vars=["df", "fig"]
    # _expected = [produce_expected_df(), produce_expected_fig()]

    _test_cases = [
        ('test_dataset_2013.txt'),
        ('test_case_dataset_2009.txt')]

    def check(self, *args):
        for test in self._test_cases:

            plt.ioff()
            
            #getting all source code cells for q1a
            cell_numbers = [4,5,9]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab3", item)
                previous = previous + "\n" + current
            
            # adding in plt cell
            previous = previous + "\n" + "plt.ioff()" + "\n" + x.get_source_code("lab3", 9)
            
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test
            update_df = x.update_csv_in_code(previous, new_csv, "df") # need to specify df in the question

            lines = update_df.split('\n')
            filtered_lines = [line for line in lines if not line.lstrip().startswith('%')]
            filtered_lines = [line for line in filtered_lines if not line.lstrip().startswith('print')]
            updated_source = '\n'.join(filtered_lines)        
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            df_actual =  variables.get('df')      
            expected_df = Question1.produce_expected(test)[0]
        
            x.determine_the_grading_method(("df", expected_df, df_actual))

            x.determine_the_grading_method(("df.head()", expected_df.head(), df_actual.head()))

            actual_fig = variables.get('fig')
            expected_fig = Question1.produce_expected(test)[1]
        
            # gettting the x and y data from the actual and expected figure
            actual_x_data, actual_y_data = x.get_x_y_data_from_plt(actual_fig)
            expected_x_data, expected_y_data = x.get_x_y_data_from_plt(expected_fig)
            
            # Compare x data
            assert all(a == b for a, b in zip(actual_x_data, expected_x_data)), "The X data is incorrect."

            # Compare y data
            assert all(a == b for a, b in zip(actual_y_data, expected_y_data)), "The Y data is incorrect."

            # grading the figure - axes, title, xlabel, ylabel
            x.grading_plt_figure(actual_fig, expected_fig) 

            plt.close('all')      