from learntools.core import *
from suss.dev import x
from datetime import datetime
from unittest.mock import patch
  
class Question6(FunctionProblem):
    _var ="question6"
    
    _test_cases = [
        (['1', 'pp1', 'SQ1', 'I', '2', '1', '1', 'pp2', 'SQ2', 'C', 'NTUC', '5', '3', '2', '4', '1', 'SQ2', '5', '6'], """1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit
Booking confirmed! ID: 1
1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit
Found! Booking id: 1
PpNo: pp1 Name: John Year Born: 1950
Flight: SQ1 Destination: LA Departure Date: 10/10/2025 10:10 
Ticket Price: $800.0
1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit
Booking confirmed! ID: 2
1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit
Airline: SIA
Booking id: 1
PpNo: pp1 Name: John Year Born: 1950
Flight: SQ1 Destination: LA Departure Date: 10/10/2025 10:10 
Ticket Price: $800.0
Company: NTUC Booking id: 2
PpNo: pp2 Name: Peter Year Born: 2000
Flight: SQ2 Destination: NY Departure Date: 11/11/2025 11:11 
Ticket Price: $500.0

1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit
Booking deleted.
1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit
Flight changed!
1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit
Airline: SIA
Booking id: 1
PpNo: pp1 Name: John Year Born: 1950
Flight: SQ2 Destination: NY Departure Date: 11/11/2025 11:11 
Ticket Price: $800.0

1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit\n"""),
        (['7', '6'], """1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit
input error
1. Add Booking
2. Search Booking
3. Delete Booking
4. Change Booking
5. Display all bookings
6. Exit\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a, expected, out))
   
    def check(self, fn):
        self.check_testbook(fn)      
                