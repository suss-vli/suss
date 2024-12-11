from learntools.core import *
from suss.dev import x
from datetime import datetime
  
class Question6(FunctionProblem):
    _var ="question6"
    _test_cases = [
        (['J1234', 'John', 2010], ['S34567', 'Jacky', 1950], ["X12345","Betty", 1980], ['SQ1', 'LA', 2899, datetime(2024, 1, 25, 4, 15)], ['SQ911', 'NY', 3188, datetime(2024, 3, 25, 7, 35)], 'NTUC', ['name', 'ppNo', 'yearBorn'], ['departureDate', 'destination', 'fare', 'flightNo'], ['_DISCOUNT', 'bookingDate', 'bookingId', 'flight', 'passenger', 'ticketPrice'], ['_CorporateBooking__company', '_DISCOUNT', 'bookingDate', 'bookingId', 'flight', 'passenger', 'ticketPrice'], f"""Booking id: 1
PP No: J1234 	 Name: John 	 YearBorn: 2010
Flight: SQ1
Destination: LA
Fare: $2,899.00
Departure Date: 25/01/2024 04:15 
Ticket Price: $2,319.20 
 Booking id: 2
PP No: S34567 	 Name: Jacky 	 YearBorn: 1950
Flight: SQ1
Destination: LA
Fare: $2,899.00
Departure Date: 25/01/2024 04:15 
Ticket Price: $2,319.20 
 Booking id: 3
PP No: X12345 	 Name: Betty 	 YearBorn: 1980
Flight: SQ1
Destination: LA
Fare: $2,899.00
Departure Date: 25/01/2024 04:15 
Ticket Price: $2,899.00

Coporate: NTUC
Booking id: 4
PP No: S34567 	 Name: Jacky 	 YearBorn: 1950
Flight: SQ911
Destination: NY
Fare: $3,188.00
Departure Date: 25/03/2024 07:35 
Ticket Price: $1,594.00\n""")
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
                    if idx < 3:
                        test_list = test[6]
                    elif 2 < idx < 5:
                        test_list = test[7]
                    elif 4 < idx < 8:
                        test_list = test[8]
                    elif idx == 8:
                        test_list = test[9]

                    for item in test_list:
                        if item in dir(obj):
                            x.justpass()
                        else:
                            x.justfail((item, obj.__class__.__name__))

            source_code = x.get_source_code("lab3", 54,"Flight, Passenger, Booking, IndividualBooking, CorporateBooking")
            x.test_for_none_162(source_code, "lab3", "54",  ["Flight", "Passenger", "Booking", "IndividualBooking", "CorporateBooking"])
            data = x.create_many_objects_from_source_code(source_code, ["Flight", "Passenger", "Booking", "IndividualBooking", "CorporateBooking"])
            Flight = data["Flight"]
            Passenger = data["Passenger"]
            
            # creating passengers 1 and 2
            pp1 = Passenger(*test[0])
            pp2 = Passenger(*test[1])
            pp3 = Passenger(*test[2])
            # creating flights 1 and 2
            fl1 = Flight(*test[3])
            fl2 = Flight(*test[4])

            ib = data["IndividualBooking"]
            cb = data["CorporateBooking"]

            # creating bookings
            ind1 = ib(pp1, fl1)
            ind2 = ib(pp2, fl1)
            ind3 = ib(pp3, fl1)
            cor1 = cb(pp2, fl2, test[5])

            # asserting p1
            x.determine_the_grading_method(("question6()", pp1.__str__(), actual[0].__str__))
            # asserting p2
            x.determine_the_grading_method(("question6()", pp2.__str__(), actual[1].__str__))
            # asserting p3
            x.determine_the_grading_method(("question6()", pp3.__str__(), actual[2].__str__))
            # asserting f1
            x.determine_the_grading_method(("question6()", fl1.__str__(), actual[3].__str__))
            # asserting f2
            x.determine_the_grading_method(("question6()", fl2.__str__(), actual[4].__str__))
            # asserting ind1
            x.determine_the_grading_method(("question6()", ind1.__str__(), actual[5].__str__))
            # asserting ind2
            x.determine_the_grading_method(("question6()", ind2.__str__(), actual[6].__str__()))
            # asserting ind3
            x.determine_the_grading_method(("question6()", ind3.__str__(), actual[7].__str__()))
            # asserting cor1
            x.determine_the_grading_method(("question6()", cor1.__str__(), actual[8].__str__()))
            # asserting the printout
            x.determine_the_grading_method(("question6()", test[10], out))

            x.grading_check_setter("`fl1.flightNo = 'MY2'`", 'MY2', fl1, "flightNo", fl1.flightNo, "@flightNo.setter")
            x.grading_check_setter("`fl1.departureDate = datetime(2023, 5, 13, 10, 35)`", datetime(2023, 5, 13, 10, 35), fl1, "departureDate", fl1.departureDate, "@departureDate.setter")
            x.grading_check_setter("`b1.flight = Flight('MY2', 'NY', 2500, datetime(2022, 10, 21, 2, 15))`", Flight('MY2', 'NY', 2500, datetime(2022, 10, 21, 2, 15)), ind1, "flight", ind1.flight, "@flight.setter")

    def check(self, fn):
        self.check_testbook(fn)      
                