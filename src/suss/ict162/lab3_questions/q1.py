from learntools.core import *
from ...dev import x


class Question1A(FunctionProblem):
    _var="JuniorAccount"    
    _test_cases = [
        (['_interestRate', 'accountId', 'accumulateInterest', 'balance', 'deposit', 'guardian', 'transfer', 'withdraw'], '002', 'John', 100, 0.04, 0.03, ['001', 100], 104, 103, """002 100.00	John""", """002 104.00	John""")
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    # to fix this https://vlisuss.atlassian.net/browse/VLI-32?focusedCommentId=10018
    def check_testbook(self, fn):
        for test in self._test_cases: 
            answer = dir(fn)

            for item in test[0]:
                if item in answer: 
                    x.justpass()
                else:
                    x.justfail((item, fn.__name__))
                if item == "_interestRate":
                    try: 
                        if fn._interestRate == 0.04 or (fn._interestRate + fn._BONUS) == 0.04:
                            x.justpass()
                        else:
                            x.justfail(item, f"""LabGuide detected that `_interestRate` is `{fn._interestRate}`. It should be `0.04`.""")
                    except AttributeError as e:
                        x.justfail(item, f"""{e}. Please define the missing attribute in `JuniorAccount` class.""")
                elif item == "guardian":
                    if isinstance(fn.guardian, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`guardian` should be a property.")
            
            ba = x.get_object_from_lab("lab3", 4, "BankAccount")
            ba1 = ba(*test[6])
            ja1 = fn(test[1], test[2], test[3])

            try:
                x.determine_the_grading_method(((test[1], test[2], test[3]), test[4], ja1._interestRate))
            except AssertionError as e:
                x.determine_the_grading_method(((test[1], test[2], test[3]), test[4], ja1._interestRate + ja1._BONUS))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[5], ba1._interestRate))

            x.determine_the_grading_method(((test[1], test[2], test[3]), test[9], ja1.__str__))

            x.determine_the_grading_method(((test[1], test[2], test[3]), False,  ja1.withdraw(51)))
            x.determine_the_grading_method(((test[1], test[2], test[3]), True, ja1.withdraw(50)))

            ja1.deposit(50)

            # 🔑 changed to handle name-mangled private attributes
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[3], ja1._BankAccount__balance))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[3], ba1._BankAccount__balance))

            ba1.accumulateInterest()
            ja1.accumulateInterest()

            x.determine_the_grading_method(((test[1], test[2], test[3]), test[7], ja1._BankAccount__balance))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[8], ba1._BankAccount__balance))

            x.determine_the_grading_method(((test[1], test[2], test[3]), test[10], ja1.__str__()))

                
    def check(self, fn):
        self.check_testbook(fn)

class Question1B(FunctionProblem):
    _var="question1b"    
    _test_cases = [
        (['234', 'Mommy', 260.00], ['_interestRate', 'accountId', 'accumulateInterest', 'balance', 'deposit', 'guardian', 'transfer', 'withdraw'], """123 250.00
234 200.00	Mommy
Deposit 100...
  234 300.00	Mommy
Withdraw 100...  False
Withdraw 50...  True
234 250.00	Mommy
123 257.50
234 260.00	Mommy\n""")
    ]
    
    
    def check_testbook(self, fn):
        for test in self._test_cases: 
            out, actual = x.compare_printout(fn)
            
            if actual is None:
                x.justfail("None", f"{self._var}() is {actual}. Please attempt the question and run the question again or return the `JuniorAccount` object.")
            else:
                for item in test[1]:
                    if item in dir(actual):
                        x.justpass()
                    else:
                        x.justfail((item, actual.__class__.__name__))

            bankaccount_code = x.get_source_code("lab3", 4, "BankAccount")
            junioraccount_code = x.get_source_code("lab3", 6, "JuniorAccount")
            
            text_source = bankaccount_code + junioraccount_code

            x.test_for_none_162(text_source, "lab3", "4,6", ["BankAccount", "JuniorAccount"])
            ja = x.create_object_from_source_code(text_source, "JuniorAccount")
            j1 = ja(*test[0])
            x.determine_the_grading_method(("question1b()", j1.__str__(), actual.__str__))
            # Test below is to assert the whole printout
            x.determine_the_grading_method(("question1b()", test[2], out))
        
    def check(self, fn):
        self.check_testbook(fn)

class Question1C(FunctionProblem):
    _var="question1c"    
    _test_cases = [
        ()
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        x.justpass()

    def check(self, fn):
        self.check_testbook(fn)

Question1 = MultipartProblem(
    Question1A,
    Question1B,
    Question1C
)    
