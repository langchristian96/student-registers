from Domain.Grades import *
from Domain.Exceptions import *
class gradeValidator:
    @staticmethod
    def validate(grade):
        if isinstance(grade,Grade)==False:
            raise StudentException("Can only validate grade objects")
        er=""
        if len(grade.getTeacher())==0:
            er+="Grade must have a teacher \n"
        if len(er)>0:
            raise StudentException(er)
        
            