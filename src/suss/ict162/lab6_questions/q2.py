from learntools.core import *
from ...dev import x

class Question2(FunctionProblem):
    _var="Corporate"
    _test_cases = [
        (["tc@gmail.com", "TC Tan", "ThatCompany", True], 0.6, "Name: TC Tan	 Email: tc@gmail.com Company: ThatCompany SME: Yes", ["ahtan@gmail.com ", "Ah Tan Tan", False], 0, """Name: Ah Tan Tan	 Email: ahtan@gmail.com  Skill Upgrade: No"""),
        (["jane.doe@example.com", "Jane Doe", "TechCorp", False], 0.5, "Name: Jane Doe	 Email: jane.doe@example.com Company: TechCorp SME: No", ["ahyong@gmail.com ", "Ah Yong Yong", True], 0.9, """Name: Ah Yong Yong	 Email: ahyong@gmail.com  Skill Upgrade: Yes"""),
        (["bob.builder@email.com", "Bob Builder", "BuildIt Inc.", True], 0.6, "Name: Bob Builder	 Email: bob.builder@email.com Company: BuildIt Inc. SME: Yes", ["ali@gmail.com", "Ali", True], 0.9, """Name: Ali	 Email: ali@gmail.com  Skill Upgrade: Yes""")

    ]
    def check_testbook(self, fn):
        if fn.__base__.__name__ == "Customer":
            x.justpass()
        else:
            x.justfail(fn.__base__, "`Corporate` class should inherit from `Customer` class.")
        
        if fn.__base__.getDiscount.__isabstractmethod__ == True:
            x.justpass()
        else:
            x.justfail(fn.__base__.getDiscount, "`getDiscount` method should be an abstract method in `Customer` class.")
        
        #  # testing for `Individual`
        # actual_individual = x.get_object_from_lab("lab6", 13, "Individual")
        
        # if actual_individual.__base__.__name__ == "Customer":
        #     x.justpass()
        # else:
        #     x.justfail(actual_individual.__base__, "`Individual` class should inherit from `Customer` class.")
        
        # if actual_individual.__base__.getDiscount.__isabstractmethod__ == True:
        #     x.justpass()
        # else:
        #     x.justfail(actual_individual.__base__.getDiscount, "`getDiscount` method should be an abstract method in `Customer` class.")
                
        for test in self._test_cases:
            cc = fn(test[0][0], test[0][1], test[0][2], test[0][3])

            x.determine_the_grading_method(((test[0][0], test[0][1], test[0][2], test[0][3]), test[1], cc.getDiscount()))
            x.determine_the_grading_method(((test[0][0], test[0][1], test[0][2], test[0][3]), test[0][0], cc.email))
            x.determine_the_grading_method(((test[0][0], test[0][1], test[0][2], test[0][3]), test[0][1], cc.name))
            x.determine_the_grading_method(((test[0][0], test[0][1], test[0][2], test[0][3]), test[2], cc.__str__()))
            
            # # testing for `Individual`
            # dd = actual_individual(test[3][0], test[3][1], test[3][2])
            # x.determine_the_grading_method(((test[3][0], test[3][1], test[3][2]), test[4], dd.getDiscount()))
            # x.determine_the_grading_method(((test[3][0], test[3][1], test[3][2]), test[3][0], dd.email))
            # x.determine_the_grading_method(((test[3][0], test[3][1], test[3][2]), test[3][1], dd.name))
            # x.determine_the_grading_method(((test[3][0], test[3][1], test[3][2]), test[5], dd.__str__()))
       

    def check(self, fn):
        self.check_testbook(fn)       
