from learntools.core import *
from ...dev import x
from datetime import datetime
import sys

class Question3A(FunctionProblem):
    _var="ProviderException"
    _test_cases = [()]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        test = fn.__bases__.__str__()
        if 'Exception' in test:
            x.justpass()
        else: 
            assert test == 'Exception', (f"""The parent class of {fn.__name__} should be an Exception""")

    def check(self, fn):
        self.check_testbook(fn)       

class Question3B(FunctionProblem):
    _var="Registration"
    _test_cases = [
        (["Prog101", "Python Programming", 1000], ["John@email.com", "John", 200], [datetime(2024, 12, 14), 2], ["tc@gmail.com", "TC Tan", "ThatCompany", True], ["jane.doe@example.com", "Jane Doe", "TechCorp", False], datetime(2024, 11, 15), datetime(2024, 10, 10), datetime(2024, 12, 20), datetime(2024, 12, 13), 1, 560.0,
"""Registration: Name: TC Tan	 Email: tc@gmail.com Company: ThatCompany SME: Yes+Schedule Id: Prog101_1 	Start Date: 2024-12-14 00:00:00 	Duration: 2 days
Course Code: Prog101   Course Name: Python Programming
Instructor email: John@email.com   Name: John""", 2, 700.0),
        (["JA214", "JavaScript Essentials", 1200], ["alice@email.com", "Alice", 250], [datetime(2024, 11, 20), 5], ["bob.builder@email.com", "Bob Builder", "BuildIt Inc.", True], ["jake.smith@email.com", "Jake Smith", "CodeWorks", False], datetime(2024, 9, 15), datetime(2024, 10, 10), datetime(2024, 12, 20), datetime(2024, 11, 19), 1, 980.0,
"""Registration: Name: Bob Builder	 Email: bob.builder@email.com Company: BuildIt Inc. SME: Yes+Schedule Id: JA214_2 	Start Date: 2024-11-20 00:00:00 	Duration: 5 days
Course Code: JA214   Course Name: JavaScript Essentials
Instructor email: alice@email.com   Name: Alice""", 2, 1225.0),
        (["DS301", "Data Science Bootcamp", 1500], ["johndoe@email.com", "John Doe", 300], [datetime(2024, 8, 25), 10], ["sam.student@email.com", "Sam Student", "LearnHub", True], ["eve.coder@email.com", "Eve Coder", "DevWorld", False], datetime(2024, 7, 30), datetime(2024, 6, 21), datetime(2024, 12, 20), datetime(2024, 8, 24), 1, 1800.0,
"""Registration: Name: Sam Student	 Email: sam.student@email.com Company: LearnHub SME: Yes+Schedule Id: DS301_3 	Start Date: 2024-08-25 00:00:00 	Duration: 10 days
Course Code: DS301   Course Name: Data Science Bootcamp
Instructor email: johndoe@email.com   Name: John Doe""", 2, 2250.0)
    ]

    def check_testbook(self, fn):
        answer = dir(fn)
        for item in ['_Registration__id', 'courseFee', 'courseOffering', 'customer', 'registrationId']:
            if item in answer: 
                x.justpass()
            else:
                x.justfail((item, fn.__name__))
            if item == "registrationId":
                if isinstance(fn.registrationId, property):
                    x.justpass()
                else:
                    x.justfail(item, "`registrationId` should be a property.")
            elif item == "courseOffering":
                if isinstance(fn.courseOffering, property):
                    x.justpass()
                else:
                    x.justfail(item, "`courseOffering` should be a property.")
            elif item == "customer":
                if isinstance(fn.customer, property):
                    x.justpass()
                else:
                    x.justfail(item, "`customer` should be a property.")

        course_code = x.get_produce_expected("lab6", "q1", "q1b")
        Course = x.create_object_from_source_code(course_code, "Course")
        Instructor = x.get_object_from_lab("lab6", 5, "Instructor")
        CourseOffering = x.get_object_from_lab("lab6", 9, "CourseOffering")
        Corporate = x.get_object_from_lab("lab6", 13, "Corporate")
            
        for test in self._test_cases:
            c1 = Course(test[0][0], test[0][1], test[0][2])
            inst = Instructor(test[1][0], test[1][1], test[1][2])
            cs = CourseOffering(c1, inst, test[2][0], test[2][1])
            cc1 = Corporate(test[3][0], test[3][1], test[3][2], test[3][3])
            cc2 = Corporate(test[4][0], test[4][1], test[4][2], test[4][3])
            reg = fn(cc1, cs, test[5]) 
            reg1 = fn(cc2, cs, test[6])   
            
            try:
                reg3 = fn(cc1, cs, test[7])
            except Exception as e:
                x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), "Course offering date cannot be earlier than registration date", e.__str__()))
                
            try:
                reg3 = fn(cc1, cs, test[8])
            except Exception as e:
                x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), "Can only register a course at least 2 days in advance", e.__str__()))
            
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[9], reg.registrationId))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[10], reg.courseFee()))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[11], reg.__str__()))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[12], reg1.registrationId))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[13], reg1.courseFee()))
            fn._Registration__id = 1

    def check(self, fn):
        self.check_testbook(fn)    

class Question3C(FunctionProblem):
    _var="TrainingProvider"
    _test_cases = [
        (["Prog101", "Python Programming", 1000], ["AI304", "AI Fundamentals", 2000], ["John@email.com", "John", 200], [datetime(2024, 12, 10), 2], ["tc@gmail.com", "TC Tan", "ThatCompany", True], (datetime(2025, 6, 10), 2), ["jane.doe@example.com", "Jane Doe", "TechCorp", False], datetime(2024, 10, 9), datetime(2024, 12, 15), [('TC Tan', 1, 'Prog101'), ('Jane Doe', 2, 'AI304')], [('TC Tan', 1, 'Prog101')], 
"""Registrations for ABC Training:
('TC Tan', 1, 'Prog101') : Registration: Name: TC Tan	 Email: tc@gmail.com Company: ThatCompany SME: Yes+Schedule Id: Prog101_1 	Start Date: 2024-12-10 00:00:00 	Duration: 2 days
Course Code: Prog101   Course Name: Python Programming
Instructor email: John@email.com   Name: John
---
('Jane Doe', 2, 'AI304') : Registration: Name: Jane Doe	 Email: jane.doe@example.com Company: TechCorp SME: No+Schedule Id: AI304_2 	Start Date: 2025-06-10 00:00:00 	Duration: 2 days
Course Code: AI304   Course Name: AI Fundamentals
Instructor email: John@email.com   Name: John
---\n"""),
        (["ABC100", "ABC Essentials", 700], ["XYZ200", "XYZ Advanced", 1200], ["rachel@abc.com", "Rachel", 80], [datetime(2024, 5, 6), 2], ["john@gmail.com", "John", "Company", True], (datetime(2025, 12, 12), 2),["peter@yahoo.com", "Peter", "MNC", False], datetime(2024, 4, 3), datetime(2024, 10, 10), [('John', 1, 'ABC100'), ('Peter', 2, 'XYZ200')], [('John', 1, 'ABC100')],
"""Registrations for ABC Training:
('John', 1, 'ABC100') : Registration: Name: John	 Email: john@gmail.com Company: Company SME: Yes+Schedule Id: ABC100_1 	Start Date: 2024-05-06 00:00:00 	Duration: 2 days
Course Code: ABC100   Course Name: ABC Essentials
Instructor email: rachel@abc.com   Name: Rachel
---
('Peter', 2, 'XYZ200') : Registration: Name: Peter	 Email: peter@yahoo.com Company: MNC SME: No+Schedule Id: XYZ200_2 	Start Date: 2025-12-12 00:00:00 	Duration: 2 days
Course Code: XYZ200   Course Name: XYZ Advanced
Instructor email: rachel@abc.com   Name: Rachel
---\n""")
    ]
    

    def check_testbook(self, fn):
        course_code = x.get_produce_expected("lab6", "q1", "q1b")
        Course = x.create_object_from_source_code(course_code, "Course")
        Instructor = x.get_object_from_lab("lab6", 5, "Instructor")
        CourseOffering = x.get_object_from_lab("lab6", 9, "CourseOffering")
        Corporate = x.get_object_from_lab("lab6", 13, "Corporate")
        registration_code = x.get_produce_expected("lab6", "q3", "q3c")
        Registration = x.create_object_from_source_code(registration_code, "Registration")
        
        for test in self._test_cases: 
            c1 = Course(test[0][0], test[0][1], test[0][2])
            c2 = Course(test[1][0], test[1][1], test[1][2])
            inst = Instructor(test[2][0], test[2][1], test[2][2])
            cs = CourseOffering(c1, inst, test[3][0], test[3][1])
            cc1 = Corporate(test[4][0], test[4][1], test[4][2], test[4][3])
            cs2 = CourseOffering(c2, inst, test[5][0], test[5][1])
            cc2 = Corporate(test[6][0], test[6][1], test[6][2], test[6][3])
            reg = Registration(cc1, cs, test[7]) 
            reg1 = Registration(cc2, cs2, test[8])   
            
            tp = fn('ABC Training')
            
            tp.addRegistration(reg)
            tp.addRegistration(reg1)
            
            x.determine_the_grading_method(((reg, reg1), test[9], list(tp._TrainingProvider__registrations.keys())))
            
            # # testing printRegistration - uncomment when instructor confirms to add printRegistration into question
            # out, actual = x.compare_printout(tp.printRegistration)
            # x.determine_the_grading_method(((reg, reg1), test[11], out))
            
            # testing providerexception 1: customer has already reigstered
            try:
                tp.addRegistration(reg)
            except Exception as e:
                x.determine_the_grading_method(((reg, reg1), "Customer has already registered for this course!", e.__str__()))
            
            # testing providerexception 2: registration id cannot be found
            try:
                tp.cancelRegistration(test[4][1], 111, test[0][0])
            except Exception as e:
                x.determine_the_grading_method(((reg, reg1), "Registration id not found!", e.__str__()))
            
            # testing providerexception 3: registration cannot be cancelled
            try:
                tp.cancelRegistration(test[4][1], 1, test[0][0])
            except Exception as e:
                x.determine_the_grading_method(((reg, reg1), "Registration cannot be cancelled!", e.__str__()))
            
            # test successfully cancelled
            tp.cancelRegistration(test[6][1], 2, test[1][0])
            x.determine_the_grading_method(((reg), test[10], list(tp._TrainingProvider__registrations.keys())))
            
            Registration._Registration__id = 1
            cs2.changeSchId(1)                             
 
    def check(self, fn):
        self.check_testbook(fn)  

class Question3D(FunctionProblem):
    _var="main"
    _test_cases = [
        ("""in try block: 
Registrations for SUSS:
('TC Tan', 1, 'Prog101') : Registration: Name: TC Tan	 Email: tc@gmail.com Company: ThatCompany SME: Yes+Schedule Id: Prog101_1 	Start Date: 2025-10-01 00:00:00 	Duration: 2 days
Course Code: Prog101   Course Name: Python Programming
Instructor email: John@email.com   Name: John
---
in else block
Registrations for SUSS:
in finally block
Registrations for SUSS:\n"""),
#         # the following is the test case for if `Individual` `dd` and `reg1` is added to TrainingProvider
#         ("""in try block: 
# Registrations for SUSS:
# ('TC Tan', 1, 'Prog101') : Registration: Name: TC Tan	 Email: tc@gmail.com Company: ThatCompany SME: Yes+Schedule Id: Prog101_1 	Start Date: 2025-10-01 00:00:00 	Duration: 2 days
# Course Code: Prog101   Course Name: Python Programming
# Instructor email: John@email.com   Name: John
# ---
# ('Tan Tan', 2, 'Prog101') : Registration: Name: Tan Tan	 Email: TanTan@gmail.com Skill Upgrade: No+Schedule Id: Prog101_1 	Start Date: 2025-10-01 00:00:00 	Duration: 2 days
# Course Code: Prog101   Course Name: Python Programming
# Instructor email: John@email.com   Name: John
# ---
# in else block
# Registrations for SUSS:
# ('Tan Tan', 2, 'Prog101') : Registration: Name: Tan Tan	 Email: TanTan@gmail.com Skill Upgrade: No+Schedule Id: Prog101_1 	Start Date: 2025-10-01 00:00:00 	Duration: 2 days
# Course Code: Prog101   Course Name: Python Programming
# Instructor email: John@email.com   Name: John
# ---
# in finally block
# Registrations for SUSS:
# ('Tan Tan', 2, 'Prog101') : Registration: Name: Tan Tan	 Email: TanTan@gmail.com Skill Upgrade: No+Schedule Id: Prog101_1 	Start Date: 2025-10-01 00:00:00 	Duration: 2 days
# Course Code: Prog101   Course Name: Python Programming
# Instructor email: John@email.com   Name: John
# ---\n""")
    ]
    

    def check_testbook(self, fn):
        out, actual = x.compare_printout(fn)
        
        x.determine_the_grading_method(("", self._test_cases[0], out))    
 
    def check(self, fn):
        self.check_testbook(fn)  

Question3 = MultipartProblem(
    Question3A,
    Question3B,
    Question3C,
    Question3D
)