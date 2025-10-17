# 0_docstring.py : demonstration of function & class docstring



def f(m:int=10,n:int=10) -> list[list[int]]:
    '''
    google docstring\n
    given \<int m> \<int n>, return mxn timetable \<list[list[int]]>

    Input:
        m (int): number of rows
        n (int): number of cols
    
    Output:
        r (list[list[int]]): mxn timetable
    '''
    return [[i*j for j in range(n)] for i in range(m)]

def g(m:int=10,n:int=10) -> list[list[int]]:
    '''
    numpy docstring\n
    given \<int m> \<int n>, return mxn timetable \<list[list[int]]>

    Input
    ----
    m : int
        number of rows
    n : int
        number of cols
    
    Output
    ----
    list[list[int]]
    mxn timetable
    '''
    return [[i*j for j in range(n)] for i in range(m)]



# 1 class docstring

class Creature:
    '''
    class representing creature

    A:
        name (str): name of creature
        type (str): type of creature
    '''
    def __init__(s:object,name:str,type:str) -> None:
        s.name = name
        s.type = type
    def __str__(s:object) -> str:
        return f'{s.name} is a {s.type}'
    def __repr__(s:object) -> str:
        return f'Creature(\'{s.name}\',\'{s.type}\')'

if __name__ == '__main__':
    print(f(10,10))
    print(g(10,10))
    bob = Creature('bob','beetle')
    print(str(bob))
    print(repr(bob))