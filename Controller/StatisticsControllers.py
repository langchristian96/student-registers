import operator
from SortFilter import *
from Controller.StudentController import *
from Controller.DisciplineController import *
from Controller.GradeController import *
from Base.StudGrade import *
from Base.StudGrade import StudGrade
class StatisticsController:
    def __init__(self,GradeCtrl,StudentCtrl,DisciplineCtrl):
        """
        Creates an instance of StatisticsController
        """
        self.__GradeController=GradeCtrl
        self.__StudentController=StudentCtrl
        self.__DisciplineController=DisciplineCtrl
    def getDisciplines(self,discipline):
        """
        Searches if a discipline is available in the discipline base
        Input: discipline-string
        Output: 1 if found the given discipline
                0 otherwise
        """
        d=self.__DisciplineController.getAll()
        disciplines=[]

        for i in d:
            disciplines.append(i.getDiscipline())
        if discipline not in disciplines:
            return 0
        return 1
    
    def getListGradesAlphabetically(self,list):
        """
        Returns the list of grades sorted alphabetically
        Input: list of grades
        Output: list of grades ordered alphabetically
        """
        finlist=[]
        if list==[]:
            return 0
        else:
            
            for e in list:
                c=e.getId()
                
                q=self.__StudentController.findById(c)
                w=StudGrade(q.getName(),e.getDiscipline(),e.getGrade(),e.getTeacher())
                
                finlist.append(w)
             
            gnomeSort(finlist)
            
        return finlist
    def getAverageGrades(self):
        """
        Calculates the average grades and creates a list with both students and grades combined
        Input: -
        Output: list of top students
        """
        students=self.__StudentController.getAll()
        name=[]
        for e in students:
            c=e.getId()
            q=self.__StudentController.findById(c)
            
            t=self.__GradeController.averageGrade(c)
            w={'name':q.getName(),'average':t}
            name.append(dict(w))
        name.sort(key=operator.itemgetter('average'),reverse=True)
        return name
        