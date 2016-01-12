from Domain.Exceptions import StudentException
from Domain.Students import Student

class StudentBase:
    def __init__(self):
        '''
         Creates an instance of the StudentBase.
         '''

        self.__data=[]
    def __find(self,id):
        '''
         Returns the index student having the given id.
         Input: id - integer, the id of the student that is being searched
        for
         Output: index - if the student was found, -1 - otherwise
         '''

        for i in range(len(self.__data)):
            if self.__data[i].getId()==id:
                return i
        return -1
    def findById(self,id):
        '''
         Returns the student having the given id.
         Input: id - integer, the id of the student that is being searched
        for
         Output: the student, if found or None otherwise
         '''
        idx=self.__find(id)
        if idx==-1:
            return None
        else:
            return self.__data[idx]
    def add(self,stud):
        '''
         Adds a student to the base.
         Input: stud - object of type Grade
         Output: the given student is added to the base, if no other
        student with the same id exists
         Exceptions: raises StudentException if another student with the
        same id already exists
         '''
        if self.findById(stud.getId())!=None:
            raise StudentException("ID already exists")
        self.__data.append(stud)
    def remove(self,id):
        '''
         Removes a student from the base, using its id
         Input: id - integer, the id of the student that must be removed
         Output: if such a student exists, it is removed and returned
         Exceptions: raises StudentException if a student with the given id
        does not exist
         '''
        idx=self.__find(id)
        if idx==-1:
            raise StudentException("There is no student with the given ID")
        return self.__data.pop(idx)
    def __len__(self):
        '''
         Returns the size of the list of grades
         (Overriding the len() built-in function)
         '''
        return len(self.__data)
    
    def __lt__(self,obj):
        return self.getName()<obj.getName()
    def getAll(self):
        '''
         Returns the list of students
         '''

        return self.__data
    
    def update(self,id,newName):
        '''
        Updates the student with the given id with the new name.
        Input:id-integer positive number
              newName-string
        Raises StudentException if there is no student with the given id.
        '''
        idx=self.__find(id)
        if idx==-1:
            raise StudentException("There is no student with the given ID")
        self.__data[idx].setName(newName)

def testStudentBase():
    base=StudentBase()
    s1=Student(1,"Darius")
    s2=Student(1,"Alex")
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
    s2=Student(2,"Nume")
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
    testStudentBase()

    
    
    
    
    