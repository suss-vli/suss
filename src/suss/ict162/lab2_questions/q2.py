from learntools.core import *
from ...dev import x
from datetime import datetime

class Question2(FunctionProblem):
    _var="question2"     
    _test_cases = [
        (['SQ1', 'LA', datetime(2022, 12, 26, 16, 30)], ['SQ52', 'KL', datetime(2022, 4, 3, 12, 35)], ['PP1', 'John'], ['PP2', 'Jane'], ['flightNo', 'destination', 'departureDate'], ['ppNo', 'name'], ['bookingId', 'flight', 'getNextBookingId', 'passenger'], """Booking id: 1
Passport No: PP1 Name: John
Flight: SQ1
Destination: LA
Departure Date: 25/12/2022 04:15
Booking id: 2
Passport No: PP2 Name: Jane
Flight: SQ52
Destination: KL
Departure Date: 03/04/2022 12:35
Booking id: 1
Passport No: PP1 Name: John
Flight: SQ1
Destination: LA
Departure Date: 25/12/2022 04:15
Booking id: 2
Passport No: PP2 Name: Jane
Flight: SQ1
Destination: LA
Departure Date: 25/12/2022 04:15
3
Booking id: 1
Passport No: PP1 Name: John
Flight: SQ1
Destination: LA
Departure Date: 26/12/2022 16:30
Booking id: 2
Passport No: PP2 Name: Jane
Flight: SQ1
Destination: LA
Departure Date: 26/12/2022 16:30
Passport No: PP2 Name: Jane\n""")
    ]
    
    def check_testbook(self, fn):
        for test in self._test_cases:
            out, actual = x.compare_printout(fn)

            Flight = x.get_object_from_lab("lab2", 16, "Flight")
            Passenger = x.get_object_from_lab("lab2", 16, "Passenger")
            Booking = x.get_object_from_lab("lab2", 16, "Booking")

            f1 = Flight(*test[0])
            f2 = Flight(*test[1])
            pp1 = Passenger(*test[2])
            pp2 = Passenger(*test[3])
            b1 = Booking(pp1, f1)
            b2 = Booking(pp2, f2)
            
            b2.flight = f1

            if actual is None:
                x.justfail("None", f"{self._var}() is {actual}. Please attempt the question and run the question again.")
            else:
                for idx, obj in enumerate(actual):
                    if idx < 2:
                        test_list = test[4]
                    elif 1 < idx < 4 :
                        test_list = test[5]
                    else:
                        test_list = test[6]

                for item in test_list:
                    if item in dir(obj):
                        x.justpass()
                    else:
                        x.justfail((item, obj.__class__.__name__))

            x.determine_the_grading_method(("question2()", f1.__str__(), actual[0].__str__))
            x.determine_the_grading_method(("question2()", f2.__str__(), actual[1].__str__))
            x.determine_the_grading_method(("question2()", pp1.__str__(), actual[2].__str__))
            x.determine_the_grading_method(("question2()", pp2.__str__(), actual[3].__str__))
            x.determine_the_grading_method(("question2()", b1.__str__(), actual[4].__str__))
            x.determine_the_grading_method(("question2()", b2.__str__(), actual[5].__str__))

            x.determine_the_grading_method(("question2()", test[7], out))

            x.grading_check_setter("`f1.flightNo = 'SQ2'`", 'SQ2', f1, "flightNo", f1._Flight__flightNo, "@flightNo.setter")
            x.grading_check_setter("`f1.departureDate = datetime(2023, 5, 13, 10, 35)`", datetime(2023, 5, 13, 10, 35), f1, "departureDate", f1._Flight__departureDate, "@departureDate.setter")
            x.grading_check_setter(
                "`b1.flight = Flight('MY2', 'NY', datetime(2022, 10, 21, 2, 15))`",
                Flight('MY2', 'NY', datetime(2022, 10, 21, 2, 15)),
                b1,
                "flight",
                b1._Booking__flight,
                "@flight.setter"
            )

    def check(self, fn):
        self.check_testbook(fn)   
