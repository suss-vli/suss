from learntools.core import *
from ...dev import x
import time
import tkinter as tk
from learntools.core import *
from tkinter import ttk, Label, Button, scrolledtext

class Question4(FunctionProblem):
    Instructor = x.get_object_from_lab("lab6", 5, "Instructor")
    _var="TrainingProviderGUI"
    _test_cases = [
        ({'d@.com': Instructor("d@abc.com", "d", 400), 'e@abc.com': Instructor("e@abc.com", "e", 500)}, """Instructors:
Instructor email: d@abc.com   Name: d
Instructor email: e@abc.com   Name: e"""),
# TODO: come back to look at this next round. below test case is to test when the pin is incorrect. test will pass but it will throw an exception error in Tkinter for AttributeError: 'NoneType' object has no attribute 'pin'
# (1, 222, "ten", 10, 200, 20, "Please check data. Login is unsuccessful\n\n", "Please check data. Login is unsuccessful\n\n")

# TODO: we can add more test cases to test 2nd and 3rd bank account, and also when pin/account id is invalid, or only pin/id is entered and not both causing an error
    ]
       
    #TODO note that this takes in a values as a list
    # def insert_into_entry(self, root, values):
    #     values_iter = iter(values)
    #     for child in root.winfo_children():
    #         if isinstance(child, tk.Frame):
    #             for grandchild in child.winfo_children():
    #                 if isinstance(grandchild, ttk.Entry):
    #                     try:
    #                         next_value = next(values_iter)
    #                         print(f"Inserted value: {next_value} into {grandchild}")
    #                     except StopIteration:
    #                         break  # No more values to insert
    #                     grandchild.insert(0, next_value)
    #                     root.update()
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
            # print("reach invoke element")
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):  # if the child is a Frame
                print("reach child")
                print(child)
                print(len(child.winfo_children()))
                print(child.winfo_children())
            for grandchild in child.winfo_children():
                print("reach grandchild")
                print(grandchild)
                if isinstance(grandchild, ttk.Button) and grandchild is element:  # if the grandchild is an Entry
                    # print("reach grandchild")
                    # print(grandchild)
                    # element.event_generate('<Button-1>')
                    # root.call(grandchild['checkGuess']())
                    grandchild.invoke()  # insert the value into the Entry
                    # root.update()
                    # root.update_idletasks()
                # else for great_grandchild in grandchil.winfo_children():
                #     if isinstance(great_grandchild, ttk.Button):
                #         element.event_generate('<Button-1>')
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

    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        #TODO: Note that we allowed the error to surface when there is no answer or no return value for this lab. 
        # For instance, student will face AttributeError: 'Q1GUI' object has no attribute 'tk' for lab5q1
        # TODO: we need to fix this in the future. Maybe we should capture these error? 
        for test in self._test_cases:
            # source = x.get_source_code("lab5", 12, "Bank, BankAccount")
            # x.test_for_none_162(source, "lab5", "12",  ["Bank", "BankAccount"])
            # data = x.create_many_objects_from_source_code(source, ["Bank", "BankAccount"])
            # bank =  data["Bank"]('POSB')
            # # print(bank)
            # bank.addAccount(data["BankAccount"](1, 111, 100))
            # bank.addAccount(data["BankAccount"](2, 222, 200))
            # bank.addAccount(data["BankAccount"](3, 333, 300))
            # LOOK HERE 20 DEC
            root = tk.Tk()
            app = fn(root)
            print("root - printed")
            app._TrainingProviderGUI__instructors = test[0]
            
            # testing "List" button.           
            self.invoke_element(root, app._TrainingProviderGUI__btnList) 
            # root.update()
            answer = app._TrainingProviderGUI__sclText.get("1.0", tk.END).strip()
            print(f"answer is '{answer}'") 
            x.grading_with_string_comparison2((test[1], answer))
            
            # testing "Add" button. 
            self.insert_into_entry(app, ["test@abc.com", "John Doe", 350])
            self.invoke_element(root, app._TrainingProviderGUI__btnAdd)
            self.invoke_element(root, app._TrainingProviderGUI__btnList)
            answer2 = app._TrainingProviderGUI__sclText.get("1.0", tk.END).strip()
            print(f"answer2 is '{answer2}'")
            x.grading_with_string_comparison2((test[1], answer2))
            
            # testing "Search" button.
            # test 1: only name and rate
            self.insert_into_entry(app, ["", "John Doe", 350])
            self.invoke_element(root, app._TrainingProviderGUI__btnSearch)
            answer3 = app._TrainingProviderGUI__sclText.get("1.0", tk.END).strip()
            print(f"answer3 is '{answer3}'")
            x.grading_with_string_comparison2((test[1], answer3))
            
            # test 2: email, name and rate
            self.insert_into_entry(app, ["test@abc.com", "John Doe", 350])
            self.invoke_element(root, app._TrainingProviderGUI__btnSearch)
            answer4 = app._TrainingProviderGUI__sclText.get("1.0", tk.END).strip()
            print(f"answer4 is '{answer4}'")
            x.grading_with_string_comparison2((test[1], answer4))
            
            # root.update()
            # time.sleep(2)
            # app.__tk.after(300, app._TrainingProviderGUI__btnList.invoke)  # Simulate "List"
            # print(app)
            
            # print(root)
            # x.clear_gui(app, root)
            # app = fn(bank)
            # app.pack()
            # app.update()

            # app, root = x.setup_gui(tk,fn)
            # time.sleep(2)

            # print("app - printed")
            # x.scan_through_every_layers(app)
            
            # #change 1
            # print("app.win - printed")
            # x.scan_through_every_layers(app.win)

            #change 2
            # self.insert_into_entry(app.win, ["1","111"])
            # self.insert_into_entry(root, [test[0], test[1]])

            # time.sleep(2)
            #change 3
            # self.invoke_element(app.win)


            # Enable the _amount_ety widget
            # app._amount_ety.config(state=tk.NORMAL)

            # Insert the value "ten" into _amount_ety
            
            # app._amount.set(test[2])
            # self.invoke_element(root, app._deposit_btn)

            # app._amount.set(test[3])
            # self.invoke_element(root, app._deposit_btn)

            # app._amount.set(test[2])
            # self.invoke_element(root, app._withdraw_btn)

            # app._amount.set(test[4])
            # self.invoke_element(root, app._withdraw_btn)

            # app._amount.set(test[5])
            # self.invoke_element(root, app._withdraw_btn)

            # self.invoke_element(root, app._check_btn)
            
            #change 4
            # answer = self.get_text_from_scrolled_text(app.win)
            # answer = self.get_text_from_scrolled_text(app)
            # print(answer)

            # print(f"answer is '{answer}'")
            # x.grading_with_string_comparison2((test[6], answer))
            
            # self.invoke_element(root, app._logout_btn)

            # self.insert_into_entry(root, [test[0], test[1]])
            # self.invoke_element(root, app._login_btn)

            # answer2 = self.get_text_from_scrolled_text(root)
            # x.grading_with_string_comparison2((test[7], answer2))

            #change 5
            # x.clear_gui(app.win, root)
            # root.quit()

    def check(self, fn):
        self.check_testbook(fn)           