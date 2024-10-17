# Load kaggle's learntools for autograding inside jupyter labs
from learntools.core import *
from .lab2_questions.q1 import Question1
from .lab2_questions.q2 import Question2
from .lab2_questions.q3 import Question3
from .lab2_questions.q4 import Question4
from .lab2_questions.q5 import Question5
from .lab2_questions.q6 import Question6
from .lab2_questions.q7 import Question7
from .lab2_questions.q8 import Question8
from .lab2_questions.q9 import Question9
from .lab2_questions.q10 import Question10
from .lab2_questions.q11 import Question11

qvars = bind_exercises(globals(), [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    Question8,
    Question9,
    Question10,
    Question11
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
