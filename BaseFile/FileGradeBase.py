from Base.GradeBase import GradeBase
from Domain.Grades import Grade
class FileGradeBase(GradeBase):
    _fName="grades.txt"
    def __init__(self):
        GradeBase.__init__(self)
        self.__loadFromFile()
    def add(self,stud):
        GradeBase.add(self, stud)
        self.__storeToFile()
    def update(self, id, newGrade, newTeacher, newDiscipline):
        GradeBase.update(self, id, newGrade, newTeacher, newDiscipline)
        self.__storeToFile()
    def remove(self, id, discipline):
        grade=GradeBase.remove(self, id, discipline)
        self.__storeToFile()
        return grade
    def __storeToFile(self):
        f=open(self._fName,"w")
        grades=GradeBase.getAll(self)
        for e in grades:
            cf=str(str(e.getId())+';'+str(e.getGrade())+';'+e.getTeacher()+';'+e.getDiscipline()+'\n')
            f.write(cf)
        f.close()
        
    def __loadFromFile(self):
        try:
            f=open(self._fName,'r')
        except IOError:
            return
        line=f.readline().strip()
        while line!="":
            t=line.split(';')
            gr=Grade(t[3],int(t[0]),t[2],int(t[1]))
            GradeBase.add(self, gr)
            line=f.readline().strip()
        f.close()