from Domain.Exceptions import StudentException

class Student:
    def __init__(self,id,name):
        """
         Creates a new instance of Student.
        """
        if id<0:
            raise StudentException("ID must be positive")
        self.__id=id
        self.__name=name
        self.__average=0
    def getName(self):
        '''
        Getter for name. This is a read-only property
        '''
        return self.__name
    def getId(self):
        '''
        Getter for id. This is a read-only property
        '''
        return self.__id
    def setId(self,value):
        '''
        Setter for id
        '''
        if value<0:
            raise StudentException("ID Must be positive")
        self.__id=value
    def setName(self,value):
        '''
        Setter for name
        '''
        self.__name=value
    def __str__(self):
        return str(self.__id)+'\t name '+str(self.__name)
    
def testStudent():
    stud=Student(1,"Ariesan Darius")
    assert stud.getId()==1
    assert stud.getName()=="Ariesan Darius"
    stud.setName("Darius")
    assert stud.getName()=="Darius"
    stud.setId(2)
    assert stud.getId()==2
    try: 
        stud.setId(-1)
        assert False
    except StudentException:
        assert True
    try:
        stud1=Student(-2,"nume")
        assert False
    except StudentException:
        assert True
if __name__ == '__main__':
    testStudent()
        
        
    