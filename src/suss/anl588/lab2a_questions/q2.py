from learntools.core import *
from ...dev import x
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import collections as mc # NEW

class Question2(EqualityCheckProblem):

    def produce_expected(dataset):
        produce_expected_code = x.get_produce_expected("lab2a", "q2", "q2")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        fig1, ax1 = exec_globals['produce_expected'](dataset)

        return fig1, ax1

    _test_cases = [
        ('HouseAge'),
        ('AveRooms')]

    def check(self, *args):
        # actual testing
        plt.ioff()

        source = x.get_source_code("lab2a", 31) + "\n" + x.get_source_code("lab2a", 59) + "\n" + "fig1 = plt.gcf()" + "\n" + "ax1 = plt.gca()"

        # assert seaborn used
        if "sns.kdeplot" in source:
            x.justpass()
        else:
            x.justfail("sns.kdeplot", "`sns.kdeplot` is not used. Please use `sns.kdeplot` to construct a kernel density plot.")

        variables = {}
        exec(source, globals(), variables)
        
        # Check actual fill color
        actual_ax = variables.get('ax1')
        plt.figure()
        expected_fig, expected_ax = Question2.produce_expected("Population")
        x.grading_anl588_seaborn_kdeplot((actual_ax, expected_ax))
            
            # testing test cases
        for test in self._test_cases:

            x.test_for_none_588(source, "lab2a", 31, "Population", test, "Population")
            updated_source = x.update_x_in_code(source, "Population", test)
            variables = {}
            exec(updated_source, globals(), variables)
            actual_ax = variables.get('ax1')
            plt.figure()
            expected_fig, expected_ax = Question2.produce_expected(test)
            x.grading_anl588_seaborn_kdeplot((actual_ax, expected_ax))

        


