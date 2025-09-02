import time
from ...dev import x
import tkinter as tk
from unittest.mock import patch
from learntools.core import *
from tkinter import ttk, Label, Button, scrolledtext


class Question1(FunctionProblem):
    _var="Q1GUI"
    _test_cases = [("seven is not a whole number\n\n", """seven is not a whole number
40 too low!\n\n""", """seven is not a whole number
40 too low!
90 too high!\n\n""", """seven is not a whole number
40 too low!
90 too high!
50 correct!\n\n""")]
    
    def insert_into_entry(self,root, value):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.Entry):
                        grandchild.insert(0, value)
                        root.update()
                        return
                        
    def get_text_from_scrolled_text(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, scrolledtext.ScrolledText):
                        return grandchild.get(1.0, tk.END)

                        
    def invoke_element(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.Button):
                        grandchild.event_generate('<Button-1>')
                        root.update()
                        return

    def check_testbook(self, fn):
        for test in self._test_cases:
            with patch('random.randint', return_value=50):
                try:
                    (app, root) = x.setup_gui(tk, fn)
                except Exception as e:
                    x.justfail("Q1GUI", "`Q1GUI` class is not defined properly. Please attempt the question and try again.")
                time.sleep(2)
                
                number1 = "seven"
                self.insert_into_entry(root, number1)
                self.invoke_element(root)
                str1 = self.get_text_from_scrolled_text(root)
                x.grading_with_string_comparison2((test[0], str1))
                
                number = 40
                self.insert_into_entry(root, number)
                self.invoke_element(root)
                str2 = self.get_text_from_scrolled_text(root)
                x.grading_with_string_comparison2((test[1], str2))

                number = 90
                self.insert_into_entry(root, number)
                self.invoke_element(root)
                str3 = self.get_text_from_scrolled_text(root)
                x.grading_with_string_comparison2((test[2], str3))

                number = 50
                self.insert_into_entry(root, number)
                self.invoke_element(root)
                str4 = self.get_text_from_scrolled_text(root)
                x.grading_with_string_comparison2((test[3], str4))

                x.clear_gui(app, root)

    
    def check(self, fn):
        self.check_testbook(fn)
