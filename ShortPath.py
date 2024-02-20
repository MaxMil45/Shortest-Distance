graph = {
    '1': {'2': {'distance': 6, 'time': 2}, '3': {'distance': 5, 'time': 3}, '6': {'distance': 3, 'time': 1}, '7': {'distance': 4, 'time': 2}, '8': {'distance': 4, 'time': 1}},
    '2': {'1': {'distance': 6, 'time': 2}, '4': {'distance': 1, 'time': 1}, '9': {'distance': 3, 'time': 2}},
    '3': {'1': {'distance': 5, 'time': 3}, '5': {'distance': 1, 'time': 2}, '10': {'distance': 4, 'time': 3}},
    '4': {'2': {'distance': 1, 'time': 1}, '11': {'distance': 3, 'time': 2}},
    '5': {'3': {'distance': 1, 'time': 2}, '12': {'distance': 3, 'time': 1}},
    '6': {'1': {'distance': 3, 'time': 1}, '7': {'distance': 1, 'time': 1}, '8': {'distance': 1, 'time': 1}, '13': {'distance': 3, 'time': 2}},
    '7': {'1': {'distance': 4, 'time': 2}, '9': {'distance': 5, 'time': 3}, '14': {'distance': 4, 'time': 2}},
    '8': {'1': {'distance': 4, 'time': 1}, '6': {'distance': 1, 'time': 1}, '10': {'distance': 3, 'time': 2}, '15': {'distance': 3, 'time': 1}},
    '9': {'2': {'distance': 2, 'time': 1}, '7': {'distance': 5, 'time': 3}, '11': {'distance': 2, 'time': 2}, '16': {'distance': 3, 'time': 1}},
    '10': {'3': {'distance': 4, 'time': 3}, '8': {'distance': 3, 'time': 1}, '12': {'distance': 4, 'time': 2}, '15': {'distance': 3, 'time': 2}, '17': {'distance': 3, 'time': 1}},
    '11': {'4': {'distance': 3, 'time': 2}, '9': {'distance': 2, 'time': 1}, '18': {'distance': 3, 'time': 2}},
    '12': {'5': {'distance': 3, 'time': 1}, '10': {'distance': 4, 'time': 2}, '19': {'distance': 3, 'time': 1}},
    '13': {'6': {'distance': 3, 'time': 2}, '14': {'distance': 2, 'time': 1}, '15': {'distance': 3, 'time': 2}, '20': {'distance': 5, 'time': 3}},
    '14': {'7': {'distance': 4, 'time': 2}, '13': {'distance': 2, 'time': 1}, '16': {'distance': 3, 'time': 2}, '21': {'distance': 5, 'time': 3}},
    '15': {'8': {'distance': 3, 'time': 1}, '10': {'distance': 3, 'time': 2}, '17': {'distance': 1, 'time': 1}, '22': {'distance': 5, 'time': 3}},
    '16': {'9': {'distance': 3, 'time': 1}, '14': {'distance': 3, 'time': 2}, '18': {'distance': 3, 'time': 2}, '21': {'distance': 4, 'time': 2}, '25': {'distance': 3, 'time': 1}},
    '17': {'10': {'distance': 3, 'time': 1}, '15': {'distance': 1, 'time': 1}, '19': {'distance': 2, 'time': 2}, '31': {'distance': 2, 'time': 2}},
    '18': {'11': {'distance': 3, 'time': 2}, '16': {'distance': 3, 'time': 2}, '25': {'distance': 2, 'time': 1}},
    '19': {'12': {'distance': 3, 'time': 1}, '17': {'distance': 2, 'time': 2}, '31': {'distance': 2, 'time': 2}},
    '20': {'13': {'distance': 5, 'time': 3}, '21': {'distance': 4, 'time': 2}, '22': {'distance': 1, 'time': 1}, '29': {'distance': 3, 'time': 2}},
    '21': {'14': {'distance': 5, 'time': 3}, '16': {'distance': 4, 'time': 2}, '20': {'distance': 4, 'time': 2}, '23': {'distance': 3, 'time': 1}, '28': {'distance': 3, 'time': 1}},
    '22': {'15': {'distance': 5, 'time': 3}, '20': {'distance': 1, 'time': 1}, '24': {'distance': 3, 'time': 2}, '29': {'distance': 3, 'time': 2}},
    '23': {'21': {'distance': 3, 'time': 1}, '25': {'distance': 1, 'time': 2}, '27': {'distance': 2, 'time': 1}, '28': {'distance': 3, 'time': 1}},
    '24': {'22': {'distance': 3, 'time': 2}, '31': {'distance': 2, 'time': 2}, '26': {'distance': 2, 'time': 1}, '30': {'distance': 1, 'time': 1}},
    '25': {'16': {'distance': 3, 'time': 1}, '18': {'distance': 2, 'time': 1}, '23': {'distance': 1, 'time': 2}, '27': {'distance': 2, 'time': 1}},
    '26': {'24': {'distance': 2, 'time': 1}, '30': {'distance': 4, 'time': 2}, '31': {'distance': 2, 'time': 2}},
    '27': {'23': {'distance': 2, 'time': 1}, '25': {'distance': 2, 'time': 1}},
    '28': {'21': {'distance': 3, 'time': 1}, '23': {'distance': 3, 'time': 1}, '29': {'distance': 5, 'time': 3}},
    '29': {'20': {'distance': 3, 'time': 2}, '22': {'distance': 3, 'time': 2}, '28': {'distance': 5, 'time': 3}, '30': {'distance': 4, 'time': 2}},
    '30': {'24': {'distance': 1, 'time': 1}, '26': {'distance': 4, 'time': 2}, '29': {'distance': 4, 'time': 2}},
    '31': {'17': {'distance': 2, 'time': 2}, '19': {'distance': 2, 'time': 2}, '24': {'distance': 2, 'time': 2}, '26': {'distance': 2, 'time': 2}},
}


def dijkstra(graph, start, end):
    distances = {node: {'distance': float('infinity'), 'time': float('infinity')} for node in graph}
    distances[start] = {'distance': 0, 'time': 0}
    priority_queue = [(0, start)]
    predecessors = {start: None}

    while priority_queue:
        min_index = 0
        for i in range(1, len(priority_queue)):
            if priority_queue[i][0] < priority_queue[min_index][0]:
                min_index = i

        total_distance, current_node = priority_queue.pop(min_index)

        for neighbor, values in graph[current_node].items():
            distance = total_distance + (values['distance'] * values['time'])

            if distance < distances[neighbor]['distance']:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                priority_queue.append((distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    return distances[end]['distance'], path

# Example usage
start_node = '1'
end_node = '29'
distance, path = dijkstra(graph, start_node, end_node)

print("The distance between node", start_node, "and node", end_node, "is:", distance)
print("The path is", path)