from learntools.core import *
from .lab4_questions.q1 import Question1
from .lab4_questions.q2 import Question2
from .lab4_questions.q3 import Question3

qvars = bind_exercises(globals(), [
    Question1,
    Question2,
    Question3
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
