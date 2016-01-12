from Domain.Students import *
from Domain.Disciplines import *
from Domain.Grades import *
from Base.GradeBase import *
from Base.DisciplineBase import *
from Base.StudentBase import *
from Controller.DisciplineController import *
from Controller.StudentController import *
from Controller.GradeController import *
from Controller.UndoController import *
from BaseFile.FileGradeBase import *
from BaseFile.FileStudentBase import *
from UI.UI import *
import operator
import collections


    
gb=GradeBase()
db=DisciplineBase()
fgb=FileGradeBase()
fsb=FileStudentBase()
sb=StudentBase()
db.add(Discipline("FPcurs"))
db.add(Discipline("FPlab"))
db.add(Discipline("FPseminar"))
db.add(Discipline("Logica"))
db.add(Discipline("ASC"))
db.add(Discipline("Algebra"))
db.add(Discipline("Analiza"))
a=input("Press 1 for nonfile or 2 for file.")
if int(a)==2:
    undoCtrl=UndoController()
    sc=StudentController(fsb,undoCtrl)
    
    gc=GradeController(fgb,undoCtrl)
    dc=DisciplineController(db)
    sts=StatisticsController(gc,sc,dc)
    ui=UI(gc,sc,dc,undoCtrl,sts)
    ui.mainMenu()

    
   
elif int(a)==1:
    sb.add(Student(1,"Darius"))
    sb.add(Student(2,"Paul"))
    sb.add(Student(3,"Mark"))
    gb.add(Grade("FPcurs",1,"arthur",10))
    
    gb.add(Grade("FPseminar",2,"iuliana",10))
    gb.add(Grade("FPlab",3,"arthur",10))
    undoCtrl=UndoController()
    sc=StudentController(sb,undoCtrl)
    
    gc=GradeController(gb,undoCtrl)
    dc=DisciplineController(db)
    sts=StatisticsController(gc,sc,dc)
    ui=UI(gc,sc,dc,undoCtrl,sts)
    ui.mainMenu()
    