from Domain.Exceptions import StudentException
from Domain.Grades import Grade

class GradeBase:

    def __init__(self):
        '''
         Creates an instance of the GradeBase.
         '''

        self.__data=[]
    def __find(self,id):
        '''
         Returns the index grade having the given id.
         Input: id - integer, the id of the student that is being searched
        for
         Output: index - if the grade was found, -1 - otherwise
         '''

        for i in range(len(self.__data)):
            if self.__data[i].getId()==id:
                return i
        return -1
    def __findUpdate(self,id,discipline):
        """
        Return the grade's id for a given id and discipline
        Input: id - integer - id of the student
                discipline - string
        """
        for i in range(len(self.__data)):
            if self.__data[i].getId()==id and self.__data[i].getDiscipline()==discipline:
                return i
        return -1
    
    def findByDisciplineAndID(self,id,discipline):
        
        """
        Returns the grade at the given discipline with the given student id
        Input: id - integer
                discipline - string
        """
        for i in range(len(self.__data)):
            if self.__data[i].getId()==id and self.__data[i].getDiscipline()==discipline:
                return self.__data[i]
        return None
        
    def findById(self,id):
        '''
         Returns the grade having the given id.
         Input: id - integer, the id of the grade that is being searched
        for
         Output: the grade, if found or None otherwise
         '''
        idx=self.__find(id)
        if idx==-1:
            return None
        else:
            return self.__data[idx]
    def add(self,stud):
        '''
         Adds a grade to the base.
         Input: stud - object of type Grade
         Output: the given Grade is added to the base, if no other
        grade with the same id exists
         Exceptions: raises StudentException if another grade with the
        same id already exists
         '''
        c=self.findById(stud.getId())
        if self.findById(stud.getId())!=None and c.getDiscipline()==stud.getDiscipline():
            raise StudentException("ID already exists at the same discipline")
        self.__data.append(stud)
    def remove(self,id,discipline):
        '''
         Removes a grade from the base, using its id
         Input: id - integer, the id of the grade that must be removed
         Output: if such a grade exists, it is removed and returned
         Exceptions: raises StudentException if a grade with the given id
        does not exist
         '''
        idx=self.__findUpdate(id,discipline)
        if idx==-1:
            raise StudentException("There is no student with the given ID")
        return self.__data.pop(idx)
    def __len__(self):
        '''
         Returns the size of the list of grades
         (Overriding the len() built-in function)
         '''

        return len(self.__data)
    
    def getAll(self):
        '''
         Returns the list of grades
         '''
        return self.__data
    
    def update(self,id,newGrade,newTeacher,newDiscipline):
        '''
        Updates the grade with the given id with the new grade, new teacher, new discipline.
        Input: id- integer positive number
               newGrade-integer between 0 and 10
               newTeacher-string
               newDiscipline-string
        Raises StudentException if there is no student with the given id.
        '''
        idx=self.__findUpdate(id, newDiscipline)
        if idx==-1:
            raise StudentException("There is no student with the given ID or the student does not have a grade at the given discipline")
        
        self.__data[idx].setTeacher(newTeacher)
        self.__data[idx].setGrade(newGrade)
        self.__data[idx].setDiscipline(newDiscipline)
def testGradeBase():
    base=GradeBase()
    s1=Grade("FP",1,"Irina",10)
    s2=Grade("FP",1,"Arthur",10)
    assert len(base)==0
    base.add(s1)
    assert len(base)==1
    assert base.findById(1)==s1
    try:
        base.add(s1)
        assert False
    except StudentException:
        assert True
    try:
        base.add(s2)
        assert False
    except StudentException:
        assert True
    s2=Grade("FP",2,"Arthur",10)
    base.add(s2)
    assert len(base)==2
    assert base.findById(1)==s1
    assert base.findById(2)==s2
    base.remove(1)
    assert len(base)==1
    assert base.findById(2)==s2
    try:
        base.remove(1)
        assert False
    except StudentException:
        assert True
    assert base.remove(2)==s2
    assert len(base)==0
if __name__ == '__main__':
    testGradeBase()

    
    
    
    
    