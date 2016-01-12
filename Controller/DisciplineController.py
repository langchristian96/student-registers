from Base.DisciplineBase import *

class DisciplineController:
    def __init__(self,dscBase):
        """
        Creates an instance of DisciplineController
        """
        self.__base=dscBase
    def getAll(self):
        """
        Returns the entire list of Disciplines
        """
        return self.__base.getAll()
    def add(self,dsc):
        """
        Adds a discipline to the discipline base
        """
        
        self.__base.add(dsc)
