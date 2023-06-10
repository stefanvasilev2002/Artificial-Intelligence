from searching_framework import *


class Explorer2(Problem):

    def successor(self, state):
        successors = dict()

        man_x = state[0]
        man_y = state[1]

        obstacle1 = [state[2], state[3], state[4]]
        obstacle2 = [state[5], state[6], state[7]]

        # OBS 1
        if obstacle1[2] == 1:
            if obstacle1[1] < 5:
                obstacle1[1] += 1
            else:
                obstacle1[2] = -1
                obstacle1[1] -= 1
        else:
            if obstacle1[1] > 0:
                obstacle1[1] -= 1
            else:
                obstacle1[2] = 1
                obstacle1[1] += 1

        if obstacle2[2] == 1:
            if obstacle2[1] < 5:
                obstacle2[1] += 1
            else:
                obstacle2[2] = -1
                obstacle2[1] -= 1
        else:
            if obstacle2[1] > 0:
                obstacle2[1] -= 1
            else:
                obstacle2[2] = 1
                obstacle2[1] += 1
        obs1 = [obstacle1[0], obstacle1[1]]
        obs2 = [obstacle2[0], obstacle2[1]]

        # RIGHT
        if man_x < 7 and [man_x + 1, man_y] != obs1 and [man_x + 1, man_y] != obs2:
            successors['RIGHT'] = (man_x + 1, man_y,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if man_x > 0 and [man_x - 1, man_y] != obs1 and [man_x - 1, man_y] != obs2:
            successors['LEFT'] = (man_x - 1, man_y,
                                  obstacle1[0], obstacle1[1], obstacle1[2],
                                  obstacle2[0], obstacle2[1], obstacle2[2])

        if man_y < 5 and [man_x, man_y + 1] != obs1 and [man_x, man_y + 1] != obs2:
            successors['UP'] = (man_x, man_y + 1,
                                obstacle1[0], obstacle1[1], obstacle1[2],
                                obstacle2[0], obstacle2[1], obstacle2[2])

        if man_y > 0 and [man_x, man_y - 1] != obs1 and [man_x, man_y - 1] != obs2:
            successors['DOWN'] = (man_x, man_y - 1,
                                  obstacle1[0], obstacle1[1], obstacle1[2],
                                  obstacle2[0], obstacle2[1], obstacle2[2])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return (state[0], state[1]) == self.goal

    def h(self, node):
        return abs(self.goal[0] - node.state[0]) + abs(self.goal[1] - node.state[1])


if __name__ == '__main__':
    goal = (7, 4)
    initial = (0, 2)
    o1 = (5, 0, 1)
    o2 = (2, 5, -1)

    explorer = Explorer2((initial[0], initial[1],
                          o1[0], o1[1], o1[2],
                          o2[0], o2[1], o2[2]), goal)

    print(astar_search(explorer).solution())
