from constraint import *

if __name__ == '__main__':
    string = input()
    if string == 'BacktrackingSolver':
        problem = Problem(BacktrackingSolver())
    elif string == 'RecursiveBacktrackingSolver':
        problem = Problem(RecursiveBacktrackingSolver())
    elif string == 'MinConflictsSolver':
        problem = Problem(MinConflictsSolver())

    variables = []
    domain = []

    for i in range(0, 81):
        variables.append(i)
    for i in range(1, 10):
        domain.append(i)
    problem.addVariables(variables, domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    # KOLONA
    tmp = []
    for i in range(0, 9):
        tmp = []
        for j in range(0, 9):
            tmp.append(j + i * 9)
        problem.addConstraint(AllDifferentConstraint(), tmp)
    # REDICA
    tmp = []
    for i in range(0, 9):
        tmp = []
        for j in range(0, 9):
            tmp.append(j * 9 + i)
        problem.addConstraint(AllDifferentConstraint(), tmp)
    # BLOKOVI
    for i in range(0, 3):
        for j in range(0, 3):
            problem.addConstraint(AllDifferentConstraint(),
                                  [27 * i + 3 * j + 9 * k + c for k in range(0, 3) for c in range(0, 3)])

    # ----------------------------------------------------

    print(problem.getSolution())

    # 0 1  2  3  4  5  6  7  8
    # 9 10 11 12 13 14 15 16 17
    # 18 19 20 21 22 23 24 25 26

    # 27 28 29 30 31 32 33 34 35
    # 36 37 38 39 40 41 42 43 44
    # 45 46 47 48 49 50 51 52 53
