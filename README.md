README

Introduction
This code implements Dijkstra's algorithm to find the shortest distance between two nodes in a graph. It calculates the shortest distance and the path between a specified start and end node.

How to Use
Input: The graph is represented as a dictionary where each key is a node, and its corresponding value is another dictionary containing neighbor nodes as keys and the distance and time to reach them as values.

Function: dijkstra(graph, start, end) takes three parameters:
graph: The graph represented as a dictionary.
start: The starting node.
end: The ending node.

Output: The function returns the shortest distance between the start and end nodes, along with the path.
