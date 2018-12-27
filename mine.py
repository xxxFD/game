import random


def mine_init():
    state = [[0] * 10 for i in range(10)]
    expose = [[0] * 10 for i in range(10)]
    for i in range(10):
        temp = random.randint(0, 99)
        while state[temp // 10][temp % 10] == 1:
            temp = random.randint(0, 99)
        state[temp // 10][temp % 10] = 1
    update_list = [[0] * 10 for i in range(10)]
    for i in range(10):
        for j in range(10):
            if i == 0 and j == 0:
                update_list[i][j] = state[i][j + 1] + state[i + 1][j] + state[i + 1][j + 1]
            elif i == 0 and j == 9:
                update_list[i][j] = state[i][j - 1] + state[i + 1][j] + state[i + 1][j - 1]
            elif i == 9 and j == 0:
                update_list[i][j] = state[i][j + 1] + state[i - 1][j] + state[i][j - 1]
            elif i == 9 and j == 9:
                update_list[i][j] = state[i][j - 1] + state[i - 1][j] + state[i - 1][j - 1]
            elif i == 0:
                update_list[i][j] = state[i][j - 1] + state[i][j + 1] + state[i + 1][j - 1] + state[i + 1][j] + \
                                    state[i + 1][j + 1]
            elif i == 9:
                update_list[i][j] = state[i][j - 1] + state[i][j + 1] + state[i - 1][j - 1] + state[i - 1][j] + \
                    state[i - 1][j + 1]
            elif j == 0:
                update_list[i][j] = state[i - 1][j] + state[i - 1][j + 1] + state[i][j + 1] + state[i + 1][j] + \
                                    state[i + 1][j + 1]
            elif j == 9:
                update_list[i][j] = state[i - 1][j] + state[i - 1][j - 1] + state[i][j - 1] + state[i + 1][j] + \
                    state[i + 1][j - 1]
            else:
                update_list[i][j] = state[i - 1][j - 1] + state[i - 1][j] + state[i - 1][j + 1] + \
                                    state[i][j - 1] + state[i][j + 1] + \
                                    state[i + 1][j - 1] + state[i + 1][j] + state[i + 1][j + 1]
    return state, update_list, expose
