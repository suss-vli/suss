from learntools.core import *
from ...dev import x
import matplotlib.pyplot as plt

class Question1A(CodingProblem):

    def produce_expected():
        produce_expected_code = x.get_produce_expected("lab2a", "q1", "q1a")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        df1 = exec_globals['produce_expected']()
        return df1

    _var = "df1"
    _expected = produce_expected()

    _test_cases = [
        ("a", "d", ['d', 'b', 'c', 0, 1, 2, 3]),
        (2, 4, ['a', 'b', 'c', 0, 1, 4, 3])
    ]

    def check(self, *args):

        #checking for the correct library imported/used
        source = x.get_source_code("lab2a", 31)
        
        if "sklearn.datasets" and "fetch_california_housing" in source:
            x.justpass()
        elif "sklearn.datasets" not in source:
            x.justfail("sklearn.datasets", "Please use the correct library: `sklearn.datasets`.")
        elif "fetch_california_housing" not in source:
            x.justfail("fetch_california_housing", "Please use the correct library: `fetch_california_housing`.")

        lines = source.split('\n')
        filtered_lines = [line for line in lines if not line.lstrip().endswith('info()')]
        filtered_lines = [line for line in filtered_lines if not line.lstrip().startswith('print')]
        updated_source = '\n'.join(filtered_lines)       
        
        variables = {}
        exec(updated_source, globals(), variables)
        
        df_actual =  variables.get('df1')      
        expected_df = Question1A._expected

        x.grading_df_series(("df1", expected_df, df_actual))
        x.determine_the_grading_method(("df1.info()", expected_df.info(), df_actual.info()))

class Question1B(EqualityCheckProblem):

    def produce_expected():
        produce_expected_code = x.get_produce_expected("lab2a", "q1", "q1b")
        exec_globals = {}
        exec(produce_expected_code, exec_globals)
        expected_fig = exec_globals['produce_expected'](Question1A._expected)
        
        return expected_fig

    _vars = ['fig', 'ax1']
    # _expected = ['<Figure size 640x480 with 1 Axes>', '<Axes: ylabel='Medium Income in California'>']
    _test_cases = [
        ('HouseAge'),
        ('AveRooms')]

    def check(self, *args):

        for test in self._test_cases:

            plt.ioff()
            
            source = x.get_source_code("lab2a", 31) + "\n" + "plt.ioff()" + "\n" + x.get_source_code("lab2a", 34)

            variables = {}
            exec(source, globals(), variables)            

            actual_fig = variables.get('fig')
            expected_fig = Question1B.produce_expected()

            # Access the patches of the actual figure
            actual_patches = actual_fig.axes[0].patches

            # Access the patches of the expected figure
            expected_patches = expected_fig.axes[0].patches

            # Ensure the number of patches is the same for both figures
            assert len(actual_patches) == len(expected_patches), ("""
The number of bars is incorrect. Expected the number of bars to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(len(expected_patches)), str(len(actual_patches)), x.get_edits_string(str(len(expected_patches)), str(len(actual_patches))))
            
            
            # Compare attributes for each patch/bar
            for i, (actual_patch, expected_patch) in enumerate(zip(actual_patches, expected_patches)):
                # Access the height (count) of the bar
                assert actual_patch.get_height() == expected_patch.get_height(), ("""
The data is incorrect. Expected the data of `Bar {}` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(i), str(expected_patch.get_height()), str(actual_patch.get_height()), x.get_edits_string(str(expected_patch.get_height()), str(actual_patch.get_height())))

                # Access color, edge color, and label of the patch
                assert actual_patch.get_facecolor() == expected_patch.get_facecolor(), ("""
Expected the face color of `Bar {}` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(i), str(expected_patch.get_facecolor()), str(actual_patch.get_facecolor()), x.get_edits_string(str(expected_patch.get_facecolor()), str(actual_patch.get_facecolor())))

                assert actual_patch.get_edgecolor() == expected_patch.get_edgecolor(), ("""
Expected the edge color of `Bar {}` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(i), str(expected_patch.get_edgecolor()), str(actual_patch.get_edgecolor()), x.get_edits_string(str(expected_patch.get_edgecolor()), str(actual_patch.get_edgecolor())))

                assert actual_patch.get_label() == expected_patch.get_label(), ("""
Expected the label of `Bar {}` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(i), str(expected_patch.get_label()), str(actual_patch.get_label()), x.get_edits_string(str(expected_patch.get_label()), str(actual_patch.get_label())))

            
             # check y label - this is checked in grading_plt_figure < but this function is specific to scatterplot
            actual_ylabel = actual_fig.axes[0].get_ylabel()
            expected_ylabel = expected_fig.axes[0].get_ylabel()

            assert actual_ylabel == expected_ylabel, ("""
The y-axis title is incorrect. Expected the y-axis title to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_ylabel), str(actual_ylabel), x.get_edits_string(str(expected_ylabel), str(actual_ylabel)))

                
            plt.close('all')      


Question1 = MultipartProblem(
    Question1A,
    Question1B
)    