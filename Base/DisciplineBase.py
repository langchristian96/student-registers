from Domain.Disciplines import Discipline
class DisciplineBase:
    def __init__(self):
        """
        Creates an instance of the DisciplineBase
        """
        self.__data=[]
    def getAll(self):
        """
        Returns all the DisciplineBase
        """
        return self.__data

        
    def add(self,dsc):
        """
        Adds a discipline to the DisciplineBase
        """
        self.__data.append(dsc)
