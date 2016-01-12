'''
Created on 21 dec. 2015

@author: LenovoM
'''

class StudGrade:
    def __init__(self,name,discipline,grade,teacher):
        self.__name=name
        self.__discipline=discipline
        self.__grade=grade
        self.__teacher=teacher
        
        
    def getName(self):
        return self.__name
    def getDiscipline(self):
        return self.__discipline
    def getGrade(self):
        return self.__grade
    def getTeacher(self):
        return self.__teacher
    def __lt__(self,obj):
        return self.getName()<obj.getName()
    def __ge__(self,obj):
        return self.getName()>=obj.getName()