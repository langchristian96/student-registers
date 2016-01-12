from Base.StudentBase import *
from Domain.Students import *
class FileStudentBase(StudentBase):
    _fName="students.txt"
    def __init__(self):
        StudentBase.__init__(self)
        self.__loadFromFile()
    def add(self, stud):
        StudentBase.add(self, stud)
        self.__storeToFile()
    def remove(self, id):
        st= StudentBase.remove(self, id)
        self.__loadFromFile()
        return st
    def update(self, id, newName):
        StudentBase.update(self, id, newName)
        self.__loadFromFile()
    def __storeToFile(self):
        f = open(self._fName, "w")
        students=StudentBase.getAll(self)
        for c in students:
            cf = str(c.getId()) + ";" + c.getName() + "\n"
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
            gr=Student(int(t[0]),t[1])
            StudentBase.add(self, gr)
            line=f.readline().strip()
        f.close()
