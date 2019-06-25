from collections import defaultdict


def initialize_dept_dict(dept_list_path):
    d = defaultdict()
    for line in open(dept_list_path, "r"):
        d[line.strip()] = {}

    return d


if __name__ == "__main__":

    dept_list_path = "data\dept_list.txt"
    dept_dict = initialize_dept_dict(dept_list_path)
