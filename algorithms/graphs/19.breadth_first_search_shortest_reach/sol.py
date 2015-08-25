import sys
file = open('in.txt')
sys.stdin = file

from collections import defaultdict


def print_seq(seq):
    print(' '.join('{}'.format(v) for v in seq))


def component(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for adj in graph[node] - set(path):
            if adj == goal:
                return path + [adj]
            else:
                queue.append((adj, path + [adj]))
    return []

T = int(input())

for _ in range(T):

    N, M = [int(x) for x in input().split()]
    graph = defaultdict(set)

    for _ in range(M):
        x, y = [int(x) for x in input().split()]
        graph[x].add(y)
        graph[y].add(x)

    S = int(input())
    nodes_to_reach = list(range(1, N + 1))
    nodes_to_reach.remove(S)

    component_set = component(graph, S)

    res = []
    for n in nodes_to_reach:
        if n in component_set:
            path = list(bfs(graph, S, n))
            if not path:
                res.append(-1)
            else:
                res.append((len(path) - 1) * 6)
        else:
            res.append(-1)
    print_seq(res)
