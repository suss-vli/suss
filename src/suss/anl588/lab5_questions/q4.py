from learntools.core import *
from ...dev import x
import os
import re
import pandas as pd
from ..lab5_questions.q2 import Question2A
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
import numpy as np
from sklearn.metrics import recall_score, make_scorer, precision_score, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier




class Question4A(EqualityCheckProblem):

    np.random.seed(0)
    def produce_expected():
        df = Question2A.produce_expected('test_credit.csv')
        produce_expected_code = x.get_produce_expected("lab5", "q4", "q4a")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        y_pred_ab_t = exec_globals['produce_expected'](df)
        return y_pred_ab_t

    _var = 'y_pred_ab_t'
    _expected = produce_expected()

    _test_cases = [
        ('X_train', "np.array([[0.1, 0.2, 0.3, 0.4, 0.5], [0.5, 0.4, 0.3, 0.2, 0.1], [0.6, 0.7, 0.8, 0.9, 1.0], [1.0, 0.9, 0.8, 0.7, 0.6], [0.3, 0.3, 0.3, 0.3, 0.3], [0.1, 0.2, 0.3, 0.4, 0.5], [0.5, 0.4, 0.3, 0.2, 0.1], [0.6, 0.7, 0.8, 0.9, 1.0], [1.0, 0.9, 0.8, 0.7, 0.6], [0.3, 0.3, 0.3, 0.3, 0.3]])", 
        'y_train', "np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])", 
        'X_test', "np.array([[0.2, 0.3, 0.4, 0.5, 0.6], [0.6, 0.5, 0.4, 0.3, 0.2]])", 
        np.array([0, 0])),
        
        ('X_train', "np.array([[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8], [8, 7, 6, 5], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]])", 
        'y_train', "np.array([0, 1, 1, 0, 1, 0, 1, 0, 1, 0])", 
        'X_test', "np.array([[2, 3, 4, 5], [5, 4, 3, 2]])", 
        np.array([0, 1])),
        
        ('X_train', "np.array([[0, 0, 1], [1, 1, 0], [0, 1, 0], [1, 0, 1], [0, 0, 0], [1, 1, 1], [0, 1, 1], [1, 0, 0], [0, 1, 1], [1, 0, 0]])", 
        'y_train', "np.array([0, 1, 1, 0, 0, 1, 1, 0, 1, 0])", 
        'X_test', "np.array([[0, 1, 1], [1, 0, 0]])", 
        np.array([1, 0]))
    ]


    def check(self, *args):

        actual_source = x.get_source_code("lab5", 56)
        filtered_actual = x.filter_source(actual_source, '#')

        if "100" and "1000" in filtered_actual:
            x.justpass()
        else:
            x.justfail("100, 1000, 100", "`(100, 1000, 100)` parameter is not found. Please use specify the correct parameter for `n_estimators`.")
        
        if "0.05" and "0.5" in filtered_actual:
            x.justpass()
        else:
            x.justfail("0.05, 0.5, 0.05", "`(0.05, 0.5, 0.05)` parameter is not found. Please use specify the correct parameter for `learning_rate`.")

        if ".fit" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".fit()", "`.fit()` is not used. Please apply the `.fit()` method on the model instance, `ab_estimator_tuned`, to train it.")

        if ".predict" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".predict()", "`.predict()` is not used. Please apply the `.predict()` method on the tuned model instance, `ab_estimator_tuned`, to compute.")
        
        previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
        filtered_previous = x.filter_source(previous, '#')

        import_source = x.get_source_code("lab5", 4)
        filtered_import_source = x.filter_source(import_source, "%")

        combined_source = filtered_import_source + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + filtered_actual
       
        variables = {}
        exec(combined_source, globals(), variables)
        
        executed_y_pred_ab_t =  variables.get('y_pred_ab_t')

        x.grading_nparray2(("y_pred_ab_t", Question4A._expected, executed_y_pred_ab_t))

        for test in self._test_cases:

            # test case for X train
            x.test_for_none_588(filtered_actual, "lab5", 56, test[0], test[1], "X_train")
            update1 = x.update_x_in_code(filtered_actual, test[0], test[1])
            # test case for y train
            x.test_for_none_588(filtered_actual, "lab5", 56, test[2], test[3], "y_train")
            update2 = x.update_x_in_code(update1, test[2], test[3])
            # test case for X test
            x.test_for_none_588(filtered_actual, "lab5", 56, test[4], test[5], "X_test")
            updated_source = x.update_x_in_code(update2, test[4], test[5])
            
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
            filtered_previous = x.filter_source(previous, '#')

            import_source = x.get_source_code("lab5", 4)
            filtered_import_source = x.filter_source(import_source, "%")

            combined_source = filtered_import_source + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + updated_source
            
            variables = {}
            exec(combined_source, globals(), variables)
            
            executed_y_pred_ab_t2 =  variables.get('y_pred_ab_t')

            x.grading_nparray2(((test[1], test[3], test[5]), "y_pred_ab_t", test[6], executed_y_pred_ab_t2), var="test")


class Question4B(EqualityCheckProblem):

    def produce_expected():
        df = Question2A.produce_expected('test_credit.csv')
        produce_expected_code = x.get_produce_expected("lab5", "q4", "q4b")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        y_pred_gb_t = exec_globals['produce_expected'](df)
        return y_pred_gb_t

    _var = 'y_pred_gb_t'
    _expected = produce_expected()

    _test_cases = [
        ('X_train', "np.array([[0.1, 0.2, 0.3, 0.4], [0.5, 0.4, 0.3, 0.2], [0.6, 0.5, 0.4, 0.3], [0.9, 0.8, 0.7, 0.6], [0.2, 0.3, 0.4, 0.5], [0.7, 0.6, 0.5, 0.4], [0.4, 0.5, 0.6, 0.7], [0.3, 0.2, 0.1, 0.0], [0.8, 0.7, 0.6, 0.5], [0.9, 0.8, 0.7, 0.6]])",
        'y_train', "np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])",  # 5 samples per class
        'X_test', "np.array([[0.4, 0.5, 0.6, 0.7], [0.5, 0.6, 0.7, 0.8]])", 
        np.array([1, 1])),

        # Second test case: Three classes, each with at least 5 samples for 5-fold CV
        ('X_train', "np.array([[0.2, 0.3, 0.4, 0.5], [0.7, 0.6, 0.5, 0.4], [0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 0.8, 0.7, 0.6], [0.4, 0.3, 0.2, 0.1], [0.3, 0.4, 0.5, 0.6], [0.6, 0.5, 0.4, 0.3], [0.2, 0.3, 0.4, 0.5], [0.9, 0.8, 0.7, 0.6], [0.5, 0.6, 0.7, 0.8], [0.4, 0.3, 0.2, 0.1], [0.3, 0.2, 0.1, 0.0], [0.6, 0.5, 0.4, 0.3], [0.8, 0.7, 0.6, 0.5]])",
        'y_train', "np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])",  # 5 samples per class
        'X_test', "np.array([[0.4, 0.5, 0.6, 0.7], [0.5, 0.6, 0.7, 0.8]])", 
        np.array([1, 0])),

        # Third test case: Two classes, each with exactly 5 samples for 5-fold CV
        ('X_train', "np.array([[0.3, 0.4, 0.5], [0.6, 0.7, 0.8], [0.1, 0.2, 0.3], [0.9, 0.8, 0.7], [0.5, 0.4, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9], [0.2, 0.1, 0.0], [0.8, 0.7, 0.6], [0.3, 0.2, 0.1]])",
        'y_train', "np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])",  # Two balanced classes with 5 samples each
        'X_test', "np.array([[0.5, 0.6, 0.7], [0.2, 0.3, 0.4]])", 
        np.array([0, 0]))
    ]

    def check(self, *args):

        actual_source = x.get_source_code("lab5", 65)
        filtered_actual = x.filter_source(actual_source, '#')
        
        if "max_depth" in filtered_actual:
            x.justpass()
        else:
            x.justfail("max_depth", "`max_depth` is not found. Please use specify the correct parameter for `max_depth`.")
        
        if "1,5" or "1, 5" or "1 , 5" or "1 ,5" in filtered_actual:
            x.justpass()
        else:
            x.justfail("1, 5", "`np.arange(1, 5)` is not found. Please use specify the correct parameter for `max_depth`.")
        
        if "100" and "1000" in filtered_actual:
            x.justpass()
        else:
            x.justfail("100, 1000, 100", "`(100, 1000, 100)` parameter is not found. Please use specify the correct parameter for `n_estimators`.")
        
        if "0.05" and "0.5" in filtered_actual:
            x.justpass()
        else:
            x.justfail("0.05, 0.5, 0.05", "`(0.05, 0.5, 0.05)` parameter is not found. Please use specify the correct parameter for `learning_rate`.")

        if ".fit" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".fit()", "`.fit()` is not used. Please apply the `.fit()` method on the model instance, `ab_estimator_tuned`, to train it.")

        if ".predict" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".predict()", "`.predict()` is not used. Please apply the `.predict()` method on the tuned model instance, `ab_estimator_tuned`, to compute.")
        
        previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
        filtered_previous = x.filter_source(previous, '#')

        import_source = x.get_source_code("lab5", 4)
        filtered_import_source = x.filter_source(import_source, "%")

        combined_source = filtered_import_source + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + filtered_actual
       
        variables = {}
        exec(combined_source, globals(), variables)
        
        executed_y_pred_gb_t =  variables.get('y_pred_gb_t')

        x.grading_nparray2(("y_pred_gb_t", Question4B._expected, executed_y_pred_gb_t))

        for test in self._test_cases:

            # test case for X train
            x.test_for_none_588(filtered_actual, "lab5", 65, test[0], test[1], "X_train")
            update1 = x.update_x_in_code(filtered_actual, test[0], test[1])
            # test case for y train
            x.test_for_none_588(filtered_actual, "lab5", 65, test[2], test[3], "y_train")
            update2 = x.update_x_in_code(update1, test[2], test[3])
            # test case for X test
            x.test_for_none_588(filtered_actual, "lab5", 65, test[4], test[5], "X_test")
            updated_source = x.update_x_in_code(update2, test[4], test[5])
            
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
            filtered_previous = x.filter_source(previous, '#')

            import_source = x.get_source_code("lab5", 4)
            filtered_import_source = x.filter_source(import_source, "%")

            combined_source = filtered_import_source + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + updated_source
            
            variables = {}
            exec(combined_source, globals(), variables)
            
            executed_y_pred_gb_t2 =  variables.get('y_pred_gb_t')

            x.grading_nparray2(((test[1], test[3], test[5]), "y_pred_gb_t", test[6], executed_y_pred_gb_t2), var="test")


Question4 = MultipartProblem(
    Question4A,
    Question4B,

)
