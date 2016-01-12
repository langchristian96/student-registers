from Domain.Exceptions import StudentException
class Grade:
    def __init__(self,discipline,id,teacher,grade):
        """
         Creates a new instance of Grade.
        """
        self.__discipline=discipline
        if id<0:
            raise StudentException("ID cannot be negative")
        if grade<0 or grade>10:
            raise StudentException("The grade must between 0 and 10")
        
        self.__id=id
        self.__discipline=discipline
        self.__teacher=teacher
        self.__grade=grade
    def getId(self):
        """
         Return the id. This is a read-only property as we do
    not have a setter
        """
        return self.__id
    def getDiscipline(self):
        '''
        Getter for discipline. This is a read-only property.
        '''
        return self.__discipline
    def getTeacher(self):
        '''
        Getter for teacher. This is a read-only property
        '''
        return self.__teacher
    def getGrade(self):
        '''
        Getter for grade. This is a read-only property
        '''
        return self.__grade
    def setId(self,value):
        '''
        Setter for id
        '''
        if value<0:
            raise StudentException("Id must be positive")
        self.__id=value
    def setDiscipline(self,value):
        '''
        Setter for discipline
        '''
        self.__discipline=value
    def setTeacher(self,value):
        '''
        Setter for teacher
        '''
        self.__teacher=value
    def setGrade(self,value):
        '''
        Setter for grade
        '''
        if value<0 or value>10:
            raise StudentException("Grade must be between 0 and 10")
        self.__grade=value
        
    def __eq__(self,crit):
        return self.getDiscipline()==str(crit)
            
    def __str__(self):
        return str(self.__discipline)+"\t Student ID: "+str(self.__id)+"\t Teacher "+str(self.__teacher)+"\t Grade: "+str(self.__grade)
    
    
def testGrade():
    grd=Grade("FP",1,"Arthur",10)
    assert grd.getID()==1
    assert grd.getDiscipline()=="FP"
    assert grd.getGrade()==10
    assert grd.getTeacher()=="Arthur"
    grd.setTeacher("Irina")
    assert grd.getTeacher()=="Irina"
    grd.setId(2)
    assert grd.getId()==2
    grd.setGrade(9)
    assert grd.getGrade()==9
    grd.setDiscipline("LabFP")
    assert grd.getDiscipline()=="LabFP"
    
    try:
        grd.setGrade(11)
        assert False
    except StudentException:
        assert True
    try:
        grd1=Grade("LC",-2,"Nume",9)
        assert False
    except StudentException:
        assert True
    try:
        grd2=Grade("LC",2,"Nume",90)
        assert False
    except StudentException:
        assert True
    
    