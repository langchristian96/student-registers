class AddOperation:
    def __init__(self,object):
        """
        Creates an instance of AddOperation
        """
        
        self.__object=object
    def getObject(self):
        """
        Getter for object
        """
        return self.__object
class RemoveOperation:
    def __init__(self,object):
        """
        Creates an instance of RemoveOperation
        """
        self.__object=object
    def getObject(self):
        
        """
        Getter for object
        """
        return self.__object
    
class UpdateOperation:
    def __init__(self,oldObject,updatedObject):
        """
        Creates an instance of UpdateOperation
        """
        self.__oldObject=oldObject
        self.__updatedObject=updatedObject
    def getOldObject(self):
        
        """
        Getter for OldObject
        """
        return self.__oldObject
    def getUpdatedObject(self):
        """
        Getter for UpdatedObject
        """
        return self.__updatedObject