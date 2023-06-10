from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def right(obstacles, h1_x, h1_y, h2_x, h2_y, o_x, o_y):
    while h1_x < 8 and [h1_x + 1, h1_y] not in obstacles \
            and [h1_x + 1, h1_y] != [h2_x, h2_y] \
            and [h1_x + 1, h1_y] != [o_x, o_y]:
        h1_x += 1
    return h1_x


def left(obstacles, h1_x, h1_y, h2_x, h2_y, o_x, o_y):
    while h1_x > 0 and [h1_x - 1, h1_y] not in obstacles \
            and [h1_x - 1, h1_y] != [h2_x, h2_y] \
            and [h1_x - 1, h1_y] != [o_x, o_y]:
        h1_x -= 1
    return h1_x


def up(obstacles, h1_x, h1_y, h2_x, h2_y, o_x, o_y):
    while h1_y < 6 and [h1_x, h1_y + 1] not in obstacles \
            and [h1_x, h1_y + 1] != [h2_x, h2_y] \
            and [h1_x, h1_y + 1] != [o_x, o_y]:
        h1_y += 1
    return h1_y


def down(obstacles, h1_x, h1_y, h2_x, h2_y, o_x, o_y):
    while h1_y > 0 and [h1_x, h1_y - 1] not in obstacles \
            and [h1_x, h1_y - 1] != [h2_x, h2_y] \
            and [h1_x, h1_y - 1] != [o_x, o_y]:
        h1_y -= 1
    return h1_y


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [7, 9]
        self.obstacles = obstacles

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.
        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        successors = dict()

        h1_x, h1_y = [state[0], state[1]]
        h2_x, h2_y = [state[2], state[3]]
        o_x, o_y = [state[4], state[5]]

        # H1
        x_new = right(self.obstacles, h1_x, h1_y, h2_x, h2_y, o_x, o_y)
        if x_new != h1_x:
            successors['H1: Right'] = (x_new, h1_y, h2_x, h2_y, o_x, o_y)
        x_new = left(self.obstacles, h1_x, h1_y, h2_x, h2_y, o_x, o_y)
        if x_new != h1_x:
            successors['H1: Left'] = (x_new, h1_y, h2_x, h2_y, o_x, o_y)
        y_new = up(self.obstacles, h1_x, h1_y, h2_x, h2_y, o_x, o_y)
        if y_new != h1_y:
            successors['H1: Up'] = (h1_x, y_new, h2_x, h2_y, o_x, o_y)
        y_new = down(self.obstacles, h1_x, h1_y, h2_x, h2_y, o_x, o_y)
        if y_new != h1_y:
            successors['H1: Down'] = (h1_x, y_new, h2_x, h2_y, o_x, o_y)

        # H2
        x_new = right(self.obstacles, h2_x, h2_y, h1_x, h1_y, o_x, o_y)
        if x_new != h2_x:
            successors['H2: Right'] = (h1_x, h1_y, x_new, h2_y, o_x, o_y)
        x_new = left(self.obstacles, h2_x, h2_y, h1_x, h1_y, o_x, o_y)
        if x_new != h2_x:
            successors['H2: Left'] = (h1_x, h1_y, x_new, h2_y, o_x, o_y)
        y_new = up(self.obstacles, h2_x, h2_y, h1_x, h1_y, o_x, o_y)
        if y_new != h2_y:
            successors['H2: Up'] = (h1_x, h1_y, h2_x, y_new, o_x, o_y)
        y_new = down(self.obstacles, h2_x, h2_y, h1_x, h1_y, o_x, o_y)
        if y_new != h2_y:
            successors['H2: Down'] = (h1_x, h1_y, h2_x, y_new, o_x, o_y)

        # O
        x_new = right(self.obstacles, o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        if x_new != o_x:
            successors['O: Right'] = (h1_x, h1_y, h2_x, h2_y, x_new, o_y)
        x_new = left(self.obstacles, o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        if x_new != o_x:
            successors['O: Left'] = (h1_x, h1_y, h2_x, h2_y, x_new, o_y)
        y_new = up(self.obstacles, o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        if y_new != o_y:
            successors['O: Up'] = (h1_x, h1_y, h2_x, h2_y, o_x, y_new)
        y_new = down(self.obstacles, o_x, o_y, h1_x, h1_y, h2_x, h2_y)
        if y_new != o_y:
            successors['O: Down'] = (h1_x, h1_y, h2_x, h2_y, o_x, y_new)

        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба
        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата
        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.
        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return state[1] == state[3] == state[5] \
            and state[0] + 1 == state[4] \
            and state[2] - 1 == state[4]


if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = Molecule(obstacles_list, (h1_pos[0], h1_pos[1],
                                         h2_pos[0], h2_pos[1],
                                         o_pos[0], o_pos[1]))

    print(breadth_first_graph_search(molecule).solution())
