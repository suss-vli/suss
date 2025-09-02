import time
from ...dev import x
import tkinter as tk
from learntools.core import *
from tkinter import ttk, Label, Button, scrolledtext

class Question3(FunctionProblem):
    _var="ATMGui"
    _test_cases = [
        (1, 111, "ten", 10, 200, 20, """1 100 retrieved
ten is not a whole number
Balance before deposit $100.00
Balance after depositing 10 is $110.00
ten is not a whole number
Insufficient balance $110.00 to withdraw $200
Balance before withdrawing $110.00
Balance after withdrawing 20 is $90.00
checking balance activated.
Balance is $90.00\n\n""", "1 90 retrieved\n\n"),
        (2, 222, "ten", 20, 300, 30, """2 200 retrieved
ten is not a whole number
Balance before deposit $200.00
Balance after depositing 20 is $220.00
ten is not a whole number
Insufficient balance $220.00 to withdraw $300
Balance before withdrawing $220.00
Balance after withdrawing 30 is $190.00
checking balance activated.
Balance is $190.00\n\n""", "2 190 retrieved\n\n"),
        (3, 333, "ten", 30, 400, 40, """3 300 retrieved
ten is not a whole number
Balance before deposit $300.00
Balance after depositing 30 is $330.00
ten is not a whole number
Insufficient balance $330.00 to withdraw $400
Balance before withdrawing $330.00
Balance after withdrawing 40 is $290.00
checking balance activated.
Balance is $290.00\n\n""", "3 290 retrieved\n\n"),
    ]

    def insert_into_entry(self, root, values):
        values_iter = iter(values)
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.Entry):
                        try:
                            next_value = next(values_iter)
                        except StopIteration:
                            break
                        grandchild.insert(0, next_value)
                        root.update()
                            
    def invoke_element(self,root,element):
        for child in root.winfo_children():
            for grandchild in child.winfo_children():
                if isinstance(grandchild, ttk.Button) and grandchild is element:
                    element.event_generate('<Button-1>')
                    root.update()
                    return
                
    def get_text_from_scrolled_text(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, scrolledtext.ScrolledText):
                        return grandchild.get(1.0, tk.END)

    def check_testbook(self, fn):
        for test in self._test_cases:
            source = x.get_source_code("lab5", 12, "Bank, BankAccount")
            x.test_for_none_162(source, "lab5", "12",  ["Bank", "BankAccount"])
            data = x.create_many_objects_from_source_code(source, ["Bank", "BankAccount"])
            bank =  data["Bank"]('POSB')
            bank.addAccount(data["BankAccount"](1, 111, 100))
            bank.addAccount(data["BankAccount"](2, 222, 200))
            bank.addAccount(data["BankAccount"](3, 333, 300))
            root = tk.Tk()
            app = fn(bank, root)
            app.update()
            
            # Insert account id and pin
            self.insert_into_entry(root, [test[0], test[1]])
            
            # Login using mangled name
            self.invoke_element(root, app._ATMGui__login_btn)
            
            # Deposit / Withdraw using mangled names
            app._ATMGui__amount.set(test[2])
            self.invoke_element(root, app._ATMGui__deposit_btn)
            
            app._ATMGui__amount.set(test[3])
            self.invoke_element(root, app._ATMGui__deposit_btn)
            
            app._ATMGui__amount.set(test[2])
            self.invoke_element(root, app._ATMGui__withdraw_btn)
            
            app._ATMGui__amount.set(test[4])
            self.invoke_element(root, app._ATMGui__withdraw_btn)
            
            app._ATMGui__amount.set(test[5])
            self.invoke_element(root, app._ATMGui__withdraw_btn)
            
            # Check balance
            self.invoke_element(root, app._ATMGui__check_btn)
            
            # Get text from scrolled text
            answer = self.get_text_from_scrolled_text(root)
            x.grading_with_string_comparison2((test[6], answer))
            
            # Logout using mangled name
            self.invoke_element(root, app._ATMGui__logout_btn)
            
            # Login again to test second part of test case
            self.insert_into_entry(root, [test[0], test[1]])
            self.invoke_element(root, app._ATMGui__login_btn)
            
            answer2 = self.get_text_from_scrolled_text(root)
            x.grading_with_string_comparison2((test[7], answer2))
            
            # Clear GUI
            x.clear_gui(app, root)

    def check(self, fn):
        self.check_testbook(fn)

