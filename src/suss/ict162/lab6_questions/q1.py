from learntools.core import *
from ...dev import x
from datetime import datetime

class Question1A(FunctionProblem):
    _var="Instructor"
    _test_cases = [
        ("John@email.com", "John", 200, """Instructor email: John@email.com   Name: John"""),
        ("Peter@email.com", "Peter", 300, """Instructor email: Peter@email.com   Name: Peter""")
        ]
    

    def check_testbook(self, fn):
        answer = dir(fn)
        for item in ['email', 'ratePerDay']:
            if item in answer: 
                x.justpass()
            else:
                x.justfail((item, fn.__name__))
            if item == "email":
                if isinstance(fn.email, property):
                    x.justpass()
                else:
                    x.justfail(item, "`email` should be a property.")
            elif item == "ratePerDay":
                if isinstance(fn.ratePerDay, property):
                    x.justpass()
                else:
                    x.justfail(item, "`ratePerDay` should be a property.")

        for test in self._test_cases:
            inst = fn(test[0], test[1], test[2])
            x.determine_the_grading_method(((test[0], test[1], test[2]), test[2], inst.ratePerDay))
            x.determine_the_grading_method(((test[0], test[1], test[2]), test[3], inst.__str__()))
                
    def check(self, fn):
        self.check_testbook(fn)

class Question1B(FunctionProblem):
    _var="CourseOffering"
    _test_cases = [
        (["Prog101", "Python Programming", 1000], ["JA214", "Javascript Fundamentals", 1500], ["John@email.com", "John", 200], [datetime(2024, 1, 4), 2], [datetime(2024, 7, 8), 5], 1400, 2500, 
"""Schedule Id: Prog101_1 	Start Date: 2024-01-04 00:00:00 	Duration: 2 days
Course Code: Prog101   Course Name: Python Programming
Instructor email: John@email.com   Name: John""", 
"""Schedule Id: JA214_2 	Start Date: 2024-07-08 00:00:00 	Duration: 5 days
Course Code: JA214   Course Name: Javascript Fundamentals
Instructor email: John@email.com   Name: John"""),
        (["DS102", "Data Science Basics", 1200], ["AI101", "AI Fundamentals", 1800], ["alice@email.com", "Alice", 300], [datetime(2024, 3, 10), 4], [datetime(2024, 8, 18), 6], 2400, 3600, 
"""Schedule Id: DS102_1 	Start Date: 2024-03-10 00:00:00 	Duration: 4 days
Course Code: DS102   Course Name: Data Science Basics
Instructor email: alice@email.com   Name: Alice""",
"""Schedule Id: AI101_2 	Start Date: 2024-08-18 00:00:00 	Duration: 6 days
Course Code: AI101   Course Name: AI Fundamentals
Instructor email: alice@email.com   Name: Alice"""),
        (["WD301", "Web Development", 1400], ["CY201", "Cybersecurity Essentials", 1600], ["bob@email.com", "Bob", 250], [datetime(2024, 5, 25), 3], [datetime(2024, 9, 30), 7], 2150, 3350, 
"""Schedule Id: WD301_1 	Start Date: 2024-05-25 00:00:00 	Duration: 3 days
Course Code: WD301   Course Name: Web Development
Instructor email: bob@email.com   Name: Bob""",
"""Schedule Id: CY201_2 	Start Date: 2024-09-30 00:00:00 	Duration: 7 days
Course Code: CY201   Course Name: Cybersecurity Essentials
Instructor email: bob@email.com   Name: Bob""")

        ]

    def check_testbook(self, fn):
        answer = dir(fn)
        for item in ['_schdId', 'changeSchId', 'courseFee', 'getCourseCode', 'getInstructorEmail', 'scheduleId', 'startDate']:
            if item in answer:
                x.justpass()
            else: 
                x.justfail((item, fn.__name__))
            if item == "_schdId":
                if fn._schdId == 1:
                    x.justpass()
                else:
                    x.justfail(item, f"`_schdId` is `{fn._schdId}`. It should be `1`.")
            elif item == "startDate":
                if isinstance(fn.startDate, property):
                    x.justpass()
                else:
                    x.justfail(item, "`startDate` should be a property.")
            elif item == "scheduleId":
                if isinstance(fn.scheduleId, property):
                    x.justpass()
                else:
                    x.justfail(item, "`scheduleId` should be a property.")

        course_code = x.get_produce_expected("lab6", "q1", "q1b")
        course = x.create_object_from_source_code(course_code, "Course")
        instructor = x.get_object_from_lab("lab6", 5, "Instructor")

        for test in self._test_cases:
            c1 = course(test[0][0], test[0][1], test[0][2])
            c2 = course(test[1][0], test[1][1], test[1][2])
            inst = instructor(test[2][0], test[2][1], test[2][2])
            cs1 = fn(c1, inst, test[3][0], test[3][1])
            cs2 = fn(c2, inst, test[4][0], test[4][1])

            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[2][0], cs1.getInstructorEmail()))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[2][0], cs2.getInstructorEmail()))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[0][0], cs1.getCourseCode()))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[1][0], cs2.getCourseCode()))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[5], cs1.courseFee()))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[6], cs2.courseFee()))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[0][0] + "_1", cs1.scheduleId))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[1][0] + "_2", cs2.scheduleId))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[7], cs1.__str__))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), test[8], cs2.__str__))

            cs1.changeSchId(2024)
            cs3 = fn(c1, inst, test[3][0], test[3][1])
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4]), cs3.scheduleId, test[0][0] + "_2024"))
            # return _schdId back to 1 for other test cases
            cs3.changeSchId(1)
     
    def check(self, fn):
        self.check_testbook(fn)

Question1 = MultipartProblem(
    Question1A,
    Question1B
)    
