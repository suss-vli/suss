from learntools.core import *
from ...dev import x
import time
import tkinter as tk
from learntools.core import *
from tkinter import ttk, Label, Button, scrolledtext

class Question4(FunctionProblem):
    try:
        Instructor = x.get_object_from_lab("lab6", 5, "Instructor")
        test_instrctor = Instructor("abc@abc.com", "abc", 100)
    except:
        instructor_code = x.get_produce_expected("lab6", "q4", "q4")
        Instructor = x.create_object_from_source_code(instructor_code, "Instructor")
        
    _var="TrainingProviderGUI"
    _test_cases = [
        ({'a@abc.com': Instructor("a@abc.com", "a", 250), 'b@abc.com': Instructor("b@abc.com", "b", 300),'c@abc.com': Instructor("c@abc.com", "c", 350)}, """Instructors:
Instructor email: a@abc.com   Name: a
Instructor email: b@abc.com   Name: b
Instructor email: c@abc.com   Name: c""", ["d@abc.com", "d", 400], """Instructors:
Instructor email: a@abc.com   Name: a
Instructor email: b@abc.com   Name: b
Instructor email: c@abc.com   Name: c
Instructor added!
Instructors:
Instructor email: a@abc.com   Name: a
Instructor email: b@abc.com   Name: b
Instructor email: c@abc.com   Name: c
Instructor email: d@abc.com   Name: d""", ["e@abc.com", "", 0], """Instructors:
Instructor email: a@abc.com   Name: a
Instructor email: b@abc.com   Name: b
Instructor email: c@abc.com   Name: c
Instructor added!
Instructors:
Instructor email: a@abc.com   Name: a
Instructor email: b@abc.com   Name: b
Instructor email: c@abc.com   Name: c
Instructor email: d@abc.com   Name: d
No instructor with this email!""", """Instructor email: d@abc.com   Name: d"""),
        # test adding same instructor
        ({'d@abc.com': Instructor("d@abc.com", "d", 400), 'e@abc.com': Instructor("e@abc.com", "e", 500)}, """Instructors:
Instructor email: d@abc.com   Name: d
Instructor email: e@abc.com   Name: e""", ["d@abc.com", "d", 400], """Instructors:
Instructor email: d@abc.com   Name: d
Instructor email: e@abc.com   Name: e
Instructor already added!
Instructors:
Instructor email: d@abc.com   Name: d
Instructor email: e@abc.com   Name: e""", ["f@abc.com", "John Doe", 350], """Instructors:
Instructor email: d@abc.com   Name: d
Instructor email: e@abc.com   Name: e
Instructor already added!
Instructors:
Instructor email: d@abc.com   Name: d
Instructor email: e@abc.com   Name: e
No instructor with this email!""", """Instructor email: d@abc.com   Name: d"""),
        # testing empty instructor dictionary
        ({},  """No instructors""", ["teach@edu.com", "Alice Smith", 100], """No instructors
Instructor added!
Instructors:
Instructor email: teach@edu.com   Name: Alice Smith""", 
    ["abc@edu.com", "abc", 100], 
     """No instructors
Instructor added!
Instructors:
Instructor email: teach@edu.com   Name: Alice Smith
No instructor with this email!""", 
    """Instructor email: teach@edu.com   Name: Alice Smith""")
    ]
 
    def insert_into_entry(self, app, values):
        values_iter = iter(values)
    
        # Find the entry widgets by name or reference
        email_widget = app._TrainingProviderGUI__tbxEmail
        name_widget = app._TrainingProviderGUI__tbxName
        rate_widget = app._TrainingProviderGUI__tbxRate
        
        widgets = [email_widget, name_widget, rate_widget]
        
        for widget in widgets:
            try:
                next_value = next(values_iter)
                widget.delete(0, tk.END)  # Clear existing text before inserting new value
                widget.insert(0, next_value)  # Insert value
            except StopIteration:
                break  # No more values to insert

                            
    def invoke_element(self,root,element):
        for child in root.winfo_children():
            for grandchild in child.winfo_children():
                if isinstance(grandchild, ttk.Button) and grandchild is element:  # if the grandchild is an Entry
                    grandchild.invoke()  # insert the value into the Entry
                    return

    def get_text_from_scrolled_text(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):  # if the child is a Frame
                print("1 - 15 may")
                print(child.winfo_children())
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, scrolledtext.ScrolledText):  # if the grandchild is an Entry
                        print("reach grandchild")
                        return grandchild.get(1.0, tk.END)

    def check_testbook(self, fn):
        for test in self._test_cases:
            root = tk.Tk()
            app = fn(root)
            app._TrainingProviderGUI__instructors = test[0]
            
            # testing "List" button.           
            self.invoke_element(root, app._TrainingProviderGUI__btnList) 
            # root.update()
            answer = app._TrainingProviderGUI__sclText.get("1.0", tk.END).strip()
            x.grading_with_string_comparison2((test[1], answer))
            
            # testing "Add" button. 
            self.insert_into_entry(app, test[2])
            self.invoke_element(root, app._TrainingProviderGUI__btnAdd)
            self.invoke_element(root, app._TrainingProviderGUI__btnList)
            answer2 = app._TrainingProviderGUI__sclText.get("1.0", tk.END).strip()
            x.grading_with_string_comparison2((test[3], answer2))
            
            # testing "Search" button.
            # test 1: only name and rate
            self.insert_into_entry(app, test[4])
            self.invoke_element(root, app._TrainingProviderGUI__btnSearch)
            answer3 = app._TrainingProviderGUI__sclText.get("1.0", tk.END).strip()
            x.grading_with_string_comparison2((test[5], answer3))
            
            # test 2: email, name and rate
            self.insert_into_entry(app, test[2])
            self.invoke_element(root, app._TrainingProviderGUI__btnSearch)
            answer4 = app._TrainingProviderGUI__sclText.get("1.0", tk.END).strip()
            x.grading_with_string_comparison2((test[6], answer4))
            
            # root.quit()

    def check(self, fn):
        self.check_testbook(fn)           