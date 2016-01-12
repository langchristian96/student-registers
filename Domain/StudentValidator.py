from Domain.Students import *
from Domain.Exceptions import *
class StudentValidator:
    @staticmethod
    def validate(student):
        if isinstance(student,Student)==False:
            raise StudentException("Can only validate Student objects")

        if len(student.getName())==0:
            raise StudentException("Student must have a name")