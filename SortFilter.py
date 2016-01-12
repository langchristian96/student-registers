

from Base.DisciplineBase import *
from Base.GradeBase import *
from Base.StudentBase import *


def gnomeSort(data):
    '''
    It is a sorting algorithm which is similar to insertion sort, 
    except that moving an element to its proper place is accomplished 
    by a series of swaps, as in bubble sort. 
    It is conceptually simple, requiring no nested loops. 
    The average, or expected, running time is O(n2), but tends towards O(n) 
    if the list is initially almost sorted.
    The algorithm always finds the first place where two adjacent elements are in the wrong order, 
    and swaps them. 
    It takes advantage of the fact that performing a swap can introduce a new out-of-order adjacent 
    pair only next to the two swapped elements. 
    It does not assume that elements forward of the current position are sorted, 
    so it only needs to check the position directly previous to the swapped elements.
    Input:list that needs to be sorted
    Output: sorted list
    '''
    pos=1
    while pos<(len(data)):
        if(data[pos]>=data[pos-1]):
            pos=pos+1
        else:
            data[pos],data[pos-1]=data[pos-1],data[pos]
            if pos>1:
                pos=pos-1


def Filter(data,criteriu):
    '''
    The function computes the corresponding element of the given list to the given criterion and appends the element
    to a new list.
    Input:data-list of elements
        criteriu- given criterion
    Output: new list with the elements corresponding to 'criteriu'
    '''
    result=[]
    for e in data:
        if e==criteriu:
            result.append(e)
    return result


def testGnomeSort():
    '''
    tester for Gnome Sort
    '''
    lista=[]
    lista.append(10)
    lista.append(3)
    lista.append(2)
    gnomeSort(lista)
    assert lista[0]==2
    
def testFilter():
    '''
    tester for Filter
    '''
    lista=[]
    gr=Grade('FPcurs',2,'qweq',10)
    gr2=Grade('FPcurs',3,'art',9)
    gr3=Grade('Algebra',4,'qweqewq',8)
    lista.append(gr)
    lista.append(gr2)
    lista.append(gr3)
    rez=[]
    rez=Filter(lista,'FPcurs')
    assert len(rez)==2
    assert rez[0].getId()==2
if __name__=='__main__':
    testGnomeSort()
    testFilter()

