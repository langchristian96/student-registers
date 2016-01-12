class UndoController:
    def __init__(self):
        """
        Creates an instance of UndoController
        """
        self.__controllers=[]
        self.__index=-1
        
    def recordUpdatedController(self,modifController):
        
        self.__controllers.append(modifController)
        self.__controllers = self.__controllers[0:self.__index + 2]
        
        self.__index=len(self.__controllers)-1
    def undo(self):
        if self.__index<0:
            return False

        for i in self.__controllers[self.__index]:
            i.undo()
        self.__index-=1
        
        
        return True
    def redo(self):
        if self.__index>=len(self.__controllers)-1:
            return False
        
        for e in self.__controllers[self.__index]:
            e.redo()
        
        self.__index+=1
        return True
    