from learntools.core import *
from ...dev import x
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd
from ..lab3_questions.q5 import Question5
from ..lab3_questions.q9 import Question9A

class Question10A(EqualityCheckProblem):


    def check(self, *args):
  
        source = x.get_source_code("lab3", 68)
        updated_source = x.filter_source(source, '#')
        
        if "sklearn.metrics" in updated_source:
            x.justpass()
        else:
            x.justfail("sklearn.metrics", "`sklearn.metrics` is not found. Please import from sklearn.metrics.")
        
        if "mean_absolute_error" in updated_source:
            x.justpass()
        else:
            x.justfail("mean_absolute_error", "`mean_absolute_error` is not found. Please import `mean_absolute_error` from sklearn.metrics.")
        
        if "mean_squared_error" in updated_source:
            x.justpass()
        else:
            x.justfail("mean_squared_error", "`mean_squared_error` is not found. Please import `mean_squared_error` from sklearn.metrics.")
        
        if "r2_score" in updated_source:
            x.justpass()
        else:
            x.justfail("r2_score", "`r2_score` is not found. Please import `r2_score` from sklearn.metrics.")

class Question10B(EqualityCheckProblem):


    def produce_expected():
        produce_expected_code = x.get_produce_expected("lab3", "q10", "q10b")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        MAE, RMSE, R2 = exec_globals['produce_expected'](Question5._expected, Question9A._expected)
        return MAE, RMSE, R2

    _vars = ['MAE', 'RMSE', 'R2']
    _expected = produce_expected()

    _test_cases = [ 
        ('test_pred', 'y_test', 0.0, 0.0, 1.0)
    ]

    def check(self, *args):
        # testing actual MAE, RMSE, R2
        x.grading_equal((f"MAE", Question10B._expected[0], args[0]))
        x.grading_equal((f"RMSE", Question10B._expected[1], args[1]))
        x.grading_equal((f"R2", Question10B._expected[2], args[2]))

        for test in self._test_cases:
            actual_source = x.get_source_code("lab3", 71)
            filtered_actual = x.filter_source(actual_source, '#')

            x.test_for_none_588(filtered_actual, "lab3", 71, test[0], test[1], "MAE, RMSE, R2")
            test_source = x.update_x_in_code(filtered_actual, test[0], test[1])

            previous = x.get_multiple_cell_source("lab3", [10, 31, 34, 39, 43, 44, 49, 53, 57, 61, 68])
            combined_source = "import pandas as pd\n" + previous + "\n" + test_source
            updated_source = x.filter_source(combined_source, '#')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}

            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
            
            executed_MAE = local_vars.get('MAE')
            executed_RMSE = local_vars.get('RMSE')
            executed_R2 = local_vars.get('R2')

            x.grading_equal((f"{test_source}", "MAE", test[2], executed_MAE), var="test")
            x.grading_equal((f"{test_source}", "RMSE", test[3], executed_RMSE), var="test")
            x.grading_equal((f"{test_source}", "R2", test[4], executed_R2), var="test")

class Question10C(EqualityCheckProblem):
    MAE, RMSE, R2 = Question10B._expected
    def produce_expected():
        produce_expected_code = x.get_produce_expected("lab3", "q10", "q10c")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        df_scores = exec_globals['produce_expected'](Question10B._expected)
        
        return df_scores

    _var = 'df_scores'
    _expected = produce_expected()

    _test_cases = [ 
        ('MAE', '0', pd.DataFrame([0,RMSE,R2], index = ['0','RMSE','R2'], columns = ['metrics']).transpose()),
        ('RMSE', '0', pd.DataFrame([MAE,0,R2], index = ['MAE','0','R2'], columns = ['metrics']).transpose()),
        ('R2', '0', pd.DataFrame([MAE,RMSE,0], index = ['MAE','RMSE','0'], columns = ['metrics']).transpose()),
        ('metrics', 'None', pd.DataFrame([MAE,RMSE,R2], index = ['MAE','RMSE','R2'], columns = ['None']).transpose())
    ]

    def check(self, *args):
        # testing actual df_scores
        x.grading_df_series(("df_scores", Question10C._expected, args[0]))

        for test in self._test_cases:

            actual_source = x.get_source_code("lab3", 74)
            filtered_actual = x.filter_source(actual_source, '#')

            x.test_for_none_588(filtered_actual, "lab3", 74, test[0], test[1], "df_scores")
            test_source = x.update_x_in_code(filtered_actual, test[0], test[1])

 
            previous = x.get_multiple_cell_source("lab3", [10, 31, 34, 39, 43, 44, 49, 53, 57, 61, 68, 71])
            combined_source = "import pandas as pd\n" + previous + "\n" + test_source
            updated_source = x.filter_source(combined_source, '#')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}

            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
            
            executed_df_scores = local_vars.get('df_scores')
            x.grading_df_series((f"{test_source}", "df_scores", test[2], executed_df_scores), var="test")

Question10 = MultipartProblem(
    Question10A,
    Question10B,
    Question10C
)    