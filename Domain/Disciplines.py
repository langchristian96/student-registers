class Discipline:
    def __init__(self,discipline):
        """
        Creates a new instance of Discipline
        """
        self.__discipline=discipline
    def getDiscipline(self):
        """
        Getter for discipline
        """
        return self.__discipline
    def setDiscipline(self,discipline):
        """
        Setter for discipline
        """
        self.__discipline=discipline
    def __eq__(self,c):
        """
        Overrides the equal function
        """
        return self.__discipline==c
        