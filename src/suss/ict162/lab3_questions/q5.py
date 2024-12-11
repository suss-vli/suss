from learntools.core import *
from suss.dev import x

class Question5A(FunctionProblem):
    _var="Vehicle"
    _test_cases = [
        (['capacity', 'computeRoadTax', 'vehNo'], 'v1', 2000, 'John', 55, """Owner: John Age: 55 Road Tax: $1800.00 Vehicle No: v1 Engine Capacity: 2000cc""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            answer = dir(fn)

            for item in test[0]:
                if item == "vehNo":
                    if isinstance(fn.vehNo, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`vehNo` should be a property.")
                elif item == "computeRoadTax":
                    if fn.computeRoadTax.__isabstractmethod__:
                        x.justpass()
                    else:
                        x.justfail(item, "`function` should be an abstract method.")
                elif item == "capacity":
                    if isinstance(fn.capacity, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`capacity` should be a property.")
                elif item in answer: 
                    x.justpass()
                else:
                    x.justfail(item, f"""The attribute `{item}` is not defined in the class.""")
                    # TODO: we noted that we did not tell the student what to do next, even though we detected that the attribute is missing. ChatGPT will tell you what to do next.
            
            #testing abstract class string
            code = x.get_source_code("lab3", 38, "Vehicle")
            passenger_vehicle_code = x.get_produce_expected("lab3", "q5", "q5a")
            combined = code + "\n" + passenger_vehicle_code
            x.test_for_none_162(combined, "lab3", "38", ["Vehicle","PassengerVehicle"])
            data = x.create_many_objects_from_source_code(combined, ["Vehicle", "PassengerVehicle"])
            pv = data["PassengerVehicle"](test[1], test[2], test[3], test[4])
            x.determine_the_grading_method((('v1', 2000, 'John', 55,), test[5], pv.__str__))
                
    def check(self, fn):
        self.check_testbook(fn)      

class Question5B(FunctionProblem):
    _var="PassengerVehicle"
    _test_cases = [
        ('v1', 2000, 'John', 55, """Owner: John Age: 55 Road Tax: $1800.00 Vehicle No: v1 Engine Capacity: 2000cc"""),
        ('v2', 2000, 'Jane', 54, """Owner: Jane Age: 54 Road Tax: $2000.00 Vehicle No: v2 Engine Capacity: 2000cc""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            p1 = fn(test[0], test[1], test[2], test[3])
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[4], p1.__str__))            

    def check(self, fn):
        self.check_testbook(fn)   

class Question5C(FunctionProblem):
    _var="CommercialVehicle"
    _test_cases = [
        ('v3', 5000, 'company1', 3, """Company: company1 Max Laden Weight: 3 Road Tax: $5000.00 Vehicle No: v3 Engine Capacity: 5000cc"""),
        ('v4', 5000, 'company2', 3.1, """Company: company2 Max Laden Weight: 3.1 Road Tax: $7500.00 Vehicle No: v4 Engine Capacity: 5000cc""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            c1 = fn(test[0], test[1], test[2], test[3])        
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[4], c1.__str__))
            
    def check(self, fn):
        self.check_testbook(fn) 

class Question5D(FunctionProblem):
    _var="question5d"
    _test_cases = [
        (['_age', '_owner', '_vehNo', 'capacity', 'computeRoadTax', 'vehNo'], ['_CommercialVehicle__coyReg', '_CommercialVehicle__maxLadenWeight', 'vehNo', 'capacity', 'computeRoadTax', 'vehNo'], ['GOAT2020', 3000, 'Roger', 41], ['GOAT1990', 3000, 'Boris', 59], ['FXT2021', 3000, 'UEN20303', 3], ['FXR3333', 4500, 'UEN20303', 5], """Owner: Roger Age: 41 Road Tax: $3000.00 Vehicle No: GOAT2020 Engine Capacity: 3000cc
3000
Company: UEN20303 Max Laden Weight: 5 Road Tax: $6750.00 Vehicle No: FXR3333 Engine Capacity: 4500cc
6750.0
Owner: Boris Age: 59 Road Tax: $2700.00 Vehicle No: GOAT1990 Engine Capacity: 3000cc
2700.0
Company: UEN20303 Max Laden Weight: 3 Road Tax: $3000.00 Vehicle No: FXT2021 Engine Capacity: 3000cc
3000\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
  
            out, actual = x.compare_printout(fn)

            if actual is None:
                x.justfail("None", f"{self._var}() is {actual}. Please attempt the question and run the question again.")
            else:
                for idx, obj in enumerate(actual):
                    if idx < 2:
                        test_list = test[0] 
                    else:
                        test_list = test[1]

                for item in test_list:
                    if item in dir(obj):
                        x.justpass()
                    else:
                        x.justfail((item, obj.__class__.__name__))            


            vehicle_code = x.get_source_code("lab3", 38,"Vehicle")
            passenger_vehicle_code = x.get_source_code("lab3", 42,"PassengerVehicle") 
            commercial_vehicle_code = x.get_source_code("lab3", 46,"CommercialVehicle")

            source_code = vehicle_code + passenger_vehicle_code + commercial_vehicle_code

            x.test_for_none_162(source_code, "lab3", "38,42,46", ["Vehicle", "PassengerVehicle","CommercialVehicle"])

            data = x.create_many_objects_from_source_code(source_code, ["Vehicle", "PassengerVehicle", "CommercialVehicle"])
            
            pv = data["PassengerVehicle"]
            cv = data["CommercialVehicle"]

            pv1 = pv(*test[2])
            pv2 = pv(*test[3])
            cv1 = cv(*test[4])
            cv2 = cv(*test[5])

            # Test below is to assert p1 string
            x.determine_the_grading_method(("question5d()", pv1.__str__(), actual[0].__str__))
            
            # Test below is to assert p2 string
            x.determine_the_grading_method(("question5d()", pv2.__str__(), actual[2].__str__))

            # Test below is to assert c1 string
            x.determine_the_grading_method(("question5d()", cv1.__str__(), actual[3].__str__))
            
            # Test below is to assert c2 string
            x.determine_the_grading_method(("question5d()", cv2.__str__(), actual[1].__str__))

            # Test below is to assert the whole printout
            x.determine_the_grading_method(("question5d()", test[6], out))

    def check(self, fn):
        self.check_testbook(fn)
       
Question5 = MultipartProblem(
    Question5A,
    Question5B,
    Question5C,
    Question5D
)    
      