from collections import deque


def bfs(vertex, graph, visited):
    queue = deque([(vertex, None)])
    while queue:
        vertex, parent = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor != parent:
                    queue.append((neighbor, vertex))
        else:
            return True
    return False


def is_contain_cycle(graph):
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            if bfs(vertex, graph, visited):
                return True
    return False


def read_txt_file(file_name):
    with open(file_name, "r") as file:
        graph = {}
        for row in file:
            vertex, *neighbors = map(int, row.split())
            graph[vertex] = neighbors
    return graph


def generate_output(file_name, result):
    with open(file_name, "w") as file:
        file.write(str(result))


# if __name__ == "__main__":
#     graph = read_txt_file('input.txt')
#     result = is_contain_cycle(graph)
#     generate_output('output.txt', result)
