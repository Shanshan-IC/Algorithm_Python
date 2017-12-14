def linear_search(list, val):
    for index, x in enumerate(list):
        if (val == x):
            return index
    return -1

if __name__ == '__main__':
    print linear_search([1, 2, 3, 5, 6, 7, 101010, 1928394, 10299283, 28282829338474], 1928394)