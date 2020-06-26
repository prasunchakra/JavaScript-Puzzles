"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
Given the number of tasks and a list of prerequisite pairs,
write a method to find the ordering of tasks we should pick to finish all tasks.
"""


def find_order(tasks, prerequisites):
    sortedOrder = []
    inDegree = {i: 0 for i in range(tasks)}
    adjList = {i: [] for i in range(tasks)}

    for parent, child in prerequisites:
        inDegree[child] += 1
        adjList[parent].append(child)

    source = [i for i in inDegree if inDegree[i] == 0]

    while source:
        vertex = source.pop(0)
        sortedOrder.append(vertex)
        for child in adjList[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                source.append(child)
    return sortedOrder


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()